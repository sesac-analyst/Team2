import scrapy
import pdfplumber
import pandas as pd
from io import BytesIO
from multiprocessing import Pool, cpu_count
import os

df = pd.read_csv('bond_date.csv')


class BondSpider(scrapy.Spider):
    name = "bond"
    
    def start_requests(self):

        for index, row in df.iterrows():
            start_date = row['start']
            end_date = row['end']
            announce_date = row['announce_date']  
            url = f'https://finance.naver.com/research/debenture_list.naver?keyword=&brokerCode=&searchType=writeDate&writeFromDate={start_date}&writeToDate={end_date}'
            yield scrapy.Request(url, self.parse, meta={'announce_date': announce_date})

    def parse(self, response):

        links = response.css('table.Nnavi td a::attr(href)').getall()
        
        if not links :  #아무것도 없을 경우
          return
        
        for link in links:
              yield response.follow(link, self.parse_page, meta={'announce_date': response.meta['announce_date']})

  # 현재 페이지를 parse
    def parse_page(self, response):

        pdf_links = response.css('td.file a::attr(href)').getall()  # pdf가 있는 table 지정

        for pdf_link in pdf_links:
            if pdf_link:
                yield scrapy.Request(pdf_link, self.parse_pdf, meta={'announce_date': response.meta['announce_date']})

    def parse_pdf(self, response):
        announce_date = response.meta['announce_date']

        pdf_bytes = BytesIO(response.body)
        with pdfplumber.open(pdf_bytes) as pdf:
            pdf_text = ""
            for page in pdf.pages:
              pdf_text += page.extract_text()
        pdf_text = pdf_text.replace("\n", " ").strip()
        
        if pdf_text:
            yield {
                'date': announce_date,
                'content': pdf_text
            }
            
    