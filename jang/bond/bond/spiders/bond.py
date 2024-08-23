import scrapy
import pandas as pd
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
        
        if not links:  # 아무것도 없을 경우
            return
        
        for link in links:
            yield response.follow(link, self.parse_page, meta={'announce_date': response.meta['announce_date']})

    def parse_page(self, response):
        pdf_links = response.css('td.file a::attr(href)').getall()  # PDF가 있는 table 지정

        for pdf_link in pdf_links:
            if pdf_link:
                yield scrapy.Request(pdf_link, self.save_pdf, meta={'announce_date': response.meta['announce_date']})

    def save_pdf(self, response):
        self.log(f"Attempting to save PDF for {response.meta['announce_date']}")
        announce_date = response.meta['announce_date']

        # 디렉토리 확인 및 생성
        os.makedirs("downloaded_pdfs", exist_ok=True)
        
        # 파일 이름에 고유 번호 추가
        base_name = f"{announce_date}.pdf"
        file_path = os.path.join("downloaded_pdfs", base_name)
        
        # 파일이 이미 존재하면 번호 추가
        counter = 1
        while os.path.exists(file_path):
            file_path = os.path.join("downloaded_pdfs", f"{announce_date}_{counter}.pdf")
            counter += 1

        # PDF 파일 저장
        with open(file_path, 'wb') as pdf_file:
            pdf_file.write(response.body)

        self.log(f"Saved file {file_path}")