## 뉴스·채권·금융통화위원회 의사록 감정분석 기반 금리 방향성 예측 

**Deciphering Monetary Policy Board Minutes with Text Mining : The Case of South Korea** 논문을 구현하는 프로젝트로, 한국은행 금융통화위원회 의사록, 뉴스기사, 채권분석 리포트를 크롤링하여 텍스트 데이터를 수집하고, 이를 자연어 처리, 토픽모델링, 감성 분석을 통해 분석합니다. 최종적으로 머신 러닝 모델에 학습시켜 다음 금리의 방향성을 예측홥니다.




<br>



## 멤버

- [김은지](https://github.com/eunji983dd)
- [장준혁](https://github.com/JangJune)
- [최준혁](https://github.com/kimbap918)
- [허홍](https://github.com/0820hong)



<br>

## Tech Stack
<img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=Pandas&logoColor=ffffff"/> <img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=NumPy&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Scrapy-770000?style=flat-square&logo=Scrapy&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Matplotlib-11557c?style=flat-square&logo=Matplotlib&logoColor=ffffff"/> <img src="https://img.shields.io/badge/eKoNLPy-3776AB?style=flat-square&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Seaborn-4C7DAF?style=flat-square&logo=Seaborn&logoColor=ffffff"/>



<br>


## Project Roadmap

![](https://i.imgur.com/wh7YiFV.png)

1. [분석·기획](#1-분석기획)

   * 프로젝트 목표 정의
   * 프로젝트 계획 수립

2. [데이터 준비](#2-데이터-준비)
   * 데이터 수집 및 클렌징
   * 데이터 전처리

3. [모델링](#3-모델링)
   * 모델 개발
   * 모델 검증 및 평가
   * 시각화

4. [평가](#4-평가)

   * 결론
   * 기대효과
   * 한계점 및 개선 방안

   

<br>



## 1. 분석·기획

### 프로젝트 목표 정의

**"Deciphering Monetary Policy Board Minutes with Text Mining: The Case of South Korea"** 논문 구현 프로젝트로, 뉴스기사, 채권분석 리포트, 한국은행 금융통화 위원회 의사록을 크롤링하여 텍스트 데이터를 수집합니다. 

수집된 데이터를 자연어 처리(NLP)를 통해 정제한 후, Naive Bayes Classifier를 활용하여 감정(긍정, 중립, 부정)을 분석합니다. 이 감정 분석 결과를 바탕으로 통계 기반 모델링을 통해 다음 금리의 방향성을 예측하고자 합니다.



<br>



### 프로젝트 계획 수립

1) **필요 데이터 정의**

   데이터 수집 기간 : 2024-08-09 ~ 2024-08-19

   1) 금융통화위원회 의사록 : 한국은행에서 제공하는 공식 문서로, 정책 결정과 관련된 주요 논의를 포함합니다.
   2) 채권분석 리포트 : 금융 기관 및 전문가들이 작성한 보고서로, 채권 시장의 동향 및 전망을 다룹니다.
   3) 뉴스 기사 : 2005년 부터 2024년까지 기준금리 발표일을 기준으로 주요 경제 뉴스 기사를 수집합니다.
   4) 콜 금리 : 단기 금융 시장에서의 금리 데이터입니다.
   5) 기준 금리 : 한국은행이 설정한 기준금리 데이터입니다.

   

2) **크롤링 역할 분담**

   1.  금융통화위원회 의사록 : 크롤링 및 데이터 수집(허홍)
   2. 채권분석 리포트 : 주요 채권 리포트 크롤링(장준혁)
   3. 뉴스기사 :
      * 한국경제(104,438건) : 크롤링(최준혁)
      * 메일경제(114,739) : 크롤링(허홍)
      * 이데일리(177,096) : 크롤링(장준혁)
   4. 콜 금리 및 기준 금리 : 관련 데이터 수집(허홍)

   

3) **데이터 전처리**

   eKoNLPy의 MPKO활용

   * 문서 N-gram 토큰화를 통해 텍스트 데이터를 정제하고, 분서에 적합한 형태로 변환합니다.

   

4) **통계 기반 모델링**

   1. Naive Bayes Classification

      * 시장 접근 방식 : 콜 금리 데이터를 활용하여 금리 변동을 예측합니다.

        1. N-gram 토큰 극성 임의 결정 : 콜 금리 변동을 기준으로 토큰의 극성(긍정/부정/중립)을 라벨링합니다.

        2. Naive Bayes 확률 계산 : 라벨링된 극성을 기반으로 Naive Bayes 모델을 학습, 각 토큰이 문서 내에서 해당 극성에 대한 확률을 계산합니다.

        3. 문서 극성 카운팅 및 금리 예측 : 특정 기간 동안의 문서에서 가장 빈번한 극성을 바탕으로 금리의 상승, 하락, 동결 여부를 예측합니다.

           

5. **모델 검증**

   실제 기준 금리와 비교

   * 모델이 예측한 금리 방향성과 실제 발표된 기준 금리를 비교하여 성능을 평가합니다.

     

6. **시각화**

   * Word Cloud : 주요 키워드와 빈도수를 시각적으로 표현합니다.

   * Text Data Visualization : 문서별 극성 및 금리 변동 예측 결과를 시각화합니다.

     

7. **평가**

   시장 접근 방식 평가

   * 평가 기준 : 매파(금리 인상 혹은 동결)와 비둘기파(금리 인하) 각각에 대해 다음과 같은 지표로 모델 성능을 평가합니다.
     1. Accuracy : 예측의 정확도
     2. Precision : 예측한 상승 또는 하락 중 실제로 해당하는 비율
     3. Recall : 실제 상승 또는 하락 중 예측에 성공한 비율
     4. F1 Score : Precision과 Recall의 조화 평균을 통한 평가



<br>



## 2. 데이터 준비

### 데이터 수집 및 클렌징

1. 금융통화위원회 의사록 크롤링

   2005년도 제 12차 의사록(2005.06.09) 부터 2024년도 제 14차 의사록(2024.07.18)까지 총 390개의 PDF파일을 크롤링 했습니다.

   <details>
     <summary>Python Code</summary>


     ```python
     import requests
     from bs4 import BeautifulSoup
     from selenium import webdriver
     from selenium.webdriver.common.by import By
     from selenium.webdriver.support.ui import WebDriverWait
     from selenium.webdriver.support import expected_conditions as EC
     from selenium.common.exceptions import TimeoutException, NoSuchElementException
     import time
     import pandas as pd
     import pymupdf as pm
     # %pip install PyMuPDF
     # %pip install requests_html
   
     webpage_num = [i for i in range(1, 40)]
     url_page_list = [f"https://www.bok.or.kr/portal/singl/newsData/listCont.do?pageIndex={i}&targetDepth=3&menuNo=201154&syncMenuChekKey=2&depthSubMain=&subMainAt=&searchCnd=1&searchKwd=&depth2=200038&depth3=201154&depth4=200789" for i in webpage_num]
     url = url_page_list[0]
     res = requests.get(url)
     soup = BeautifulSoup(res.text, 'html.parser')
     hrefs = soup.select("div.bd-line > ul > li.bbsRowCls")
     href_list = [href.select('.title')[0].attrs.get('href') for href in hrefs]
     "https://www.bok.or.kr"+href_list[0]
   
     # 의사록 날짜 list
     minute_date_list = []
     for url_page in url_page_list:
         dateres = requests.get(url_page, 'html.parser')
         datesoup = BeautifulSoup(dateres.text)
         titlelist = datesoup.select('li.bbsRowCls > div.set')
         for title in titlelist:
             text_split = title.text.split('\n')
             text_strip = [i.strip() for i in text_split if i.strip()][0]
             minute_date = text_strip[text_strip.index(')') + 2:-1]
             minute_date_list.append(minute_date)
   
     minute_date_list
     len(minute_date_list)
   
     # pdf 링크가 있는 사이트 추출(2024년 7월 18일 ~ 2005년 6월 9일)
     link_list = []
     webpage_num = [i for i in range(1,40)]
     url_page_list = [f"https://www.bok.or.kr/portal/singl/newsData/listCont.do?pageIndex={i}&targetDepth=3&menuNo=201154&syncMenuChekKey=2&depthSubMain=&subMainAt=&searchCnd=1&searchKwd=&depth2=200038&depth3=201154&depth4=200789" for i in webpage_num]
     for url in url_page_list:
         res = requests.get(url)
         soup = BeautifulSoup(res.text, 'html.parser')
         hrefs = soup.select("div.bd-line > ul > li.bbsRowCls")
         href_list = [href.select('.title')[0].attrs.get('href') for href in hrefs]
         link_list.extend(["https://www.bok.or.kr"+sub_href for sub_href in href_list])
   
     link_list
   
     # pdf 링크 추출
     pdf_link_list = []
     for sub_link in link_list:
         res2 = requests.get(sub_link, 'html.parser')
         soup2 = BeautifulSoup(res2.text)
         sub_pdf_link = soup2.select_one(".viewer").attrs.get('href')
         pdf_link_list.append("https://www.bok.or.kr"+sub_pdf_link)
     len(pdf_link_list)
     pdf_test_link = pdf_link_list[0]
     res3 = requests.get(pdf_test_link, 'html.parser')
     soup3 = BeautifulSoup(res3.text)
     pdf_test_link
     import fitz
   
     pdf_file_list = []
     for link in link_list:
         res4 = requests.get(link, 'html.parser')
         soup4 = BeautifulSoup(res4.text)
         if soup4.select('.file')[0].attrs.get('href')[-3:] == 'hwp':
             pdf_file_link = soup4.select('.file')[1]
         else:
             pdf_file_link = soup4.select('.file')[0]
         pdf_file_list.append("https://www.bok.or.kr" + pdf_file_link.attrs.get('href'))
   
     # for i in range(len(pdf_file_list)):
     #     if pdf_file_list[i][-3:] == 'hwp':
     #         pdf_file_list[i] = pdf_file_list[i].replace('hwp', 'pdf')
             
     pdf_file_list
     len(pdf_file_list)
     pdf_dict = {}
     for minute_date, pdf_file in zip(minute_date_list, pdf_file_list):
         try:
             pdf_res = requests.get(pdf_file)
             pdf_data = fitz.io.BytesIO(pdf_res.content)
             doc = fitz.open(stream=pdf_data, filetype="pdf")
             full_text = ""
             for page_num in range(len(doc)):
                 page = doc.load_page(page_num)  # Load the page
                 text = page.get_text("text")    # Extract text as a string
                 full_text += text+"\n"
                 
             keyword = "회의경과"
             keyword_index = full_text.index(keyword)
             full_text[keyword_index:]
             pdf_dict[minute_date] = full_text[keyword_index:]
   
         except Exception as e:
             # print('>>>', e)
             print(pdf_file)
             
   
     pdf_dict.keys()
     minute_df = pd.DataFrame(pdf_dict.values(), index=pdf_dict.keys())
     minute_df.rename(columns={0:'content'}, inplace=True)
     minute_df = minute_df.iloc[::-1]
     idxlist = []
     for item in minute_df.index:
         idxlist.append(item.replace('.','-'))
   
     minute_df.index = idxlist
     minute_df.reset_index(inplace=True)
     idxlist
     x = idxlist[0].split('-')
     for i in range(len(x)):
         if int(x[i]) < 10:
             x[i] = '0'+x[i]
   
     ''.join(x)
     final_idxlist = []
     for idx in idxlist:
         temp = idx.split('-')
         temp = [v for v in temp if v]
         for i in range(len(temp)):
             if int(temp[i])<10:
                 temp[i] = '0'+temp[i]
   
         final_idxlist.append(''.join(temp))
   
     final_idxlist
     minute_df['index'] = final_idxlist
     minute_df.rename(columns={'index' : 'date'}, inplace=True)
     minute_df
     minute_df.to_csv("C:/Users/SesacPython/Desktop/workspace/Team2/hong/mpc_minute.csv")
     ```

   </details>

   

   

2. 채권분석 리포트 크롤링

   총 6,334개의 네이버 채권분석 리포트 PDF 파일을 크롤링했습니다. 크롤링한 리포트 PDF 파일 내 텍스트만 출력해서 날짜별로 텍스트 데이터만 저장했습니다.

   <details>
     <summary>Python Code</summary>


     ```python
   from bs4 import BeautifulSoup
   import requests
   import time
   import re
   from requests import get
   from urllib import request
   from PyPDF2 import PdfReader
   import os
   import csv
   from pykospacing import Spacing
   import os.path
   import shutil
   from tika import parser
   from datetime import datetime
   
   today = datetime.today().strftime("%Y-%m-%d")
   
   target_day = "2013-05-09"
   
   url = f"https://finance.naver.com/research/debenture_list.naver?keyword=&brokerCode=&searchType=writeDate&writeFromDate={target_day}&writeToDate={today}&x=0&y=0&page=1"
   temp_url = "https://finance.naver.com/"
   headers = {
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36', 
       'Referer': 'https://www.naver.com/'
       }
   
   response = requests.get(url, headers=headers)
   
   soup = BeautifulSoup(response.text, 'html.parser')
   
   last_page = soup.select_one('td.pgRR>a').attrs['href']
   temp = "/research/debenture_list.naver?keyword=&brokerCode=&searchType=writeDate&writeFromDate=2013-05-09&writeToDate=2023-09-01&x=0&y=0&page="
   pages = int(last_page.replace(temp,''))
   
   for page in range(1,pages+1):
       page_url = f"https://finance.naver.com/research/debenture_list.naver?keyword=&brokerCode=&searchType=writeDate&writeFromDate={target_day}&writeToDate={today}&x=0&y=0&page={page}"
   
       headers = {
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36', 
           'Referer': 'https://www.naver.com/'
           }
   
       response = requests.get(page_url, headers=headers)
   
       soup = BeautifulSoup(response.text, 'html.parser')
   
       stock_links = soup.select('table.type_1> tr')
   
       nomal_page = "https://finance.naver.com/research/"
       print(f"{page} 번 페이지 진행중입니다")
       for link in stock_links:
           taget = link.select("a")
           if taget == []:
               pass
           else:
               url_link = taget[0].attrs['href']
               crawling_link = nomal_page+url_link
               total_url = crawling_link
   
               headers = {
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36', 
                   'Referer': 'https://www.naver.com/'
                   }
   
               response = requests.get(total_url, headers=headers)
               print(total_url)
               soup = BeautifulSoup(response.text, 'html.parser')
   
               maket = soup.select_one('p.source').text
               maket = maket.replace("\n",'')
               maket = maket.replace("\t",'')
               maket = maket.split("|")
               maket_name = maket[0]
               date = maket[1]
   
               stock_title = soup.select_one('th.view_sbj').text
   
               title = stock_title.replace("\n",'')
               title = title.replace("\t",'')
               title = title.split(maket_name)
               title = title[0]
               title = title.replace('  ','') #리서치 제목
               for idx in range(len(title)): #공백제거
                   if title[idx] != ' ':
                       target_idx = idx
               title = title[:target_idx+1]
               new_title = ''
               for i in title:
                   if i == "/":
                       new_title += "_"
                   else:
                       new_title += i
   
               title = new_title
               print(f"리서치 제목 : {title}")
               info = soup.select_one("td.view_cnt").text
               info = info.replace('\n','')
               pdf = soup.select("a.con_link")[1].text
               if pdf == '':
                   print("PDF 파일이 없습니다 이 경우엔 수집하지 않습니다")
                   pass
               else:
                   print("PDF 파일이 존재 합니다")
                   info = info.split(pdf)
                   info = info[0]
                   pdf_link = soup.select_one("a.con_link").attrs['href'] #pdf 다운로드 링크
                   pdf = soup.select("a.con_link")[1].text #pdf파일 이름
                   if "/" in pdf:
                       pdf = pdf.replace('/','_')
                   pdf_name = soup.select("a.con_link")[1].text[:-4]
                   print(pdf)
                   with open(pdf, "wb") as file:   # open in binary mode
                       response = get(pdf_link)               # get request
                       time.sleep(1)
                       file.write(response.content) 
   
                   PDF_FILE_PATH = pdf
   
                   # reader = PdfReader(PDF_FILE_PATH)
                   # pages = reader.pages
                   # text = ''
                   # for page in pages:
                   #     sub = page.extract_text()
                   #     text += sub
                   parsed = parser.from_file(PDF_FILE_PATH)
                   text = parsed['content']
                   if text is None:
                       print("pdf 파일을 읽을 수 없습니다")
                   else:
                       str_text = text
                       new_str = re.sub("\n", "", str_text)
                       new_str = re.sub(" ", "", new_str)
   
                       spacing = Spacing()
                       kospacing_result = spacing(new_str) 
   
                       directory = f'./dataset/{date}'
   
                       if os.path.isdir(directory):
                           print(directory)
                           print("저장경로 있습니다")
                           time.sleep(1)
                       else:
                           print("저장경로가 없습니다")
                           current_path = os.getcwd()
                           os.mkdir(directory)
                           time.sleep(2)
                           if os.path.isdir(directory):
                               print("저장경로 생성하였습니다")
                           else:
                               print("저장경로 생성 실패하였습니다")
                       with open(f'{directory}/{title}_{maket_name}_{date}.text', 'w', encoding='utf-8') as f:
                           f.write('제목\n')
                           f.write(f'{title}\n')
                           f.write('\n')
                           f.write('요약\n')
                           f.write(f'{info}\n')
                           f.write('\n')
                           f.write('내용\n')
                           f.write(f'{kospacing_result}\n')
                       time.sleep(1)
                   # 파일 삭제
                   remove_file_path = PDF_FILE_PATH # 제거할 파일
                   os.remove(remove_file_path)
     ```

   </details>

   

   

   

3. 뉴스 크롤링 - 검색창에 ‘금리’ 검색

   - **이데일리**

     - **크롤링 개요**

       이데일리에서 2005년 05월 13일부터 2024년 07월 10일까지 제목과 본문을 크롤링 했습니다. 2005년 06월 09일이 금융통화위원회 의사록의 pdf 파일을 최초로 크롤링 가능한 날짜기 때문에 기준으로 정했습니다. 총 177,096건의 뉴스를 수집했습니다.

     - **크롤링 코드**

        <details>
          <summary>Python Code</summary>
        
        
          ```python
        import scrapy
        import pandas as pd
        
        # CSV 파일 읽기
        df = pd.read_csv('edaily_date.csv')
        
        class EdailySpider(scrapy.Spider):
            name = 'edaily'
            allowed_domains = ["edaily.co.kr"]
        
            def start_requests(self):
                x = 0
                for index, row in df.iterrows():
                    start_date = row['start']
                    end_date = row['end']
                    announce_date = int(row['announce_date'])
                    url = f'<https://www.edaily.co.kr/search/news/?source=total&keyword=%ea%b8%88%eb%a6%ac&include=&exclude=&jname=&start={start_date}&end={end_date}&sort=&date=pick&exact=false&page=1>'
                    yield scrapy.Request(url, self.parse, meta={'start_date': start_date, 'end_date': end_date, 'page': 1, 'announce_date': announce_date})
        
            def parse(self, response):
                # 뉴스 목록 페이지에서 각 뉴스 기사의 링크를 추출
                article_links = response.css('div.newsbox_04 a::attr(href)').getall()
                
                # 만약 기사 링크가 없으면 더 이상 페이지가 없다고 판단
                if not article_links:
                    self.logger.info(f"No articles found on page {response.url}. No more pages.")
                    return
        
                for link in article_links:
                    yield response.follow(link, self.parse_article, meta={'announce_date': response.meta['announce_date']})
                
                # 다음 페이지로 이동
                current_page = response.meta['page']
                next_page = current_page + 1
                next_page_url = f'<https://www.edaily.co.kr/search/news/?source=total&keyword=%ea%b8%88%eb%a6%ac&include=&exclude=&jname=&start={response.meta["start_date"]}&end={response.meta["end_date"]}&sort=&date=pick&exact=false&page={next_page}>'
                
                # 페이지에 기사 링크가 있으면 다음 페이지로 이동
                if article_links:
                    yield scrapy.Request(next_page_url, self.parse, meta={'start_date': response.meta['start_date'], 'end_date': response.meta['end_date'], 'page': next_page, 'announce_date': response.meta['announce_date']})
        
            def parse_article(self, response):
                # 뉴스 본문과 제목 추출
                title = response.css('div.news_titles h1::text').get()
                content = response.css('div.news_body::text').getall()
                
                # 데이터가 없을 경우 처리
                if not title:
                    self.logger.error(f"Missing title for URL: {response.url}")
                    return
                
                title = title.strip()
                content = ''.join(content).strip()
                announce_date = response.meta['announce_date']
                
                if '재송' in title:
                    self.logger.info(f"Skipping duplicated article: {title}")
                    return
                
                yield {
                    'announce_date': announce_date,
                    'title': title,
                    'content': content,
                    'url': response.url
                }
          ```
        
        </details>

   - **한국경제**

     - **크롤링 개요**

       한국경제에서 2005년 06월 09일 부터 2024년 07월 11일까지 뉴스 기사 건의 본문을 scrapy를 이용하여 104,438건 크롤링 했습니다. 금융통화위원회 의사록의 pdf크롤링 가능한 일자와 맞추기 위해 2005년 06월 09년을 시작일 기준으로 잡았습니다.

     - **크롤링 코드**
        <details>
          <summary>Python Code</summary>
        
          ```python
        import pandas as pd
        import subprocess
        import os
        
        # CSV 파일 읽기
        date_ranges = pd.read_csv('/content/date_range.csv', sep=',')
        
        # 열 이름 확인 (첫 번째 몇 줄 출력)
        print(date_ranges.head())
        
        # 실제 헤더 이름을 확인하여 'start'와 'end'가 맞는지 확인
        # 만약 헤더가 다르다면 다음과 같이 수정
        # date_ranges.columns = ['start', 'end']  # 실제 파일의 헤더에 맞춰 수정
        
        # 날짜를 파싱하여 datetime 형식으로 변환
        date_ranges['start'] = pd.to_datetime(date_ranges['start'], format='%Y.%m.%d')
        date_ranges['end'] = pd.to_datetime(date_ranges['end'], format='%Y.%m.%d')
        
        # 출력 디렉토리 생성
        output_dir = 'output'
        os.makedirs(output_dir, exist_ok=True)
        
        # 각 날짜 범위를 순회하며 Scrapy 명령 실행
        for index, row in date_ranges.iterrows():
            start_date = row['start'].strftime('%Y.%m.%d')
            end_date = row['end'].strftime('%Y.%m.%d')
        
            # 날짜 범위에 따라 출력 파일 이름 정의
            output_file = os.path.join(output_dir, f'hankyung_news_{start_date}_to_{end_date}.json')
        
            # 실행할 Scrapy 명령어
            command = [
                'scrapy', 'runspider', 'hankyung.py',
                '-a', f'search_term=금리',
                '-a', f'start_date={start_date}',
                '-a', f'end_date={end_date}',
                '-o', output_file,
                '--loglevel=DEBUG'  # 로그 레벨을 DEBUG로 설정
            ]
        
            # 명령어 실행 및 로그 캡처
            result = subprocess.run(command, capture_output=True, text=True)
        
            # 표준 출력 및 오류 출력 로그 표시
            print(f"Output for {start_date} to {end_date}:")
            print(result.stdout)
            if result.stderr:
                print(f"Errors for {start_date} to {end_date}:")
                print(result.stderr)
        
            # 오류 발생 시 예외 처리
            if result.returncode != 0:
                print(f"Scrapy command failed for {start_date} to {end_date}.")
          ```
        
        </details>

   - **매일경제**

     - **크롤링 개요**

       연합인포맥스에서 2013년 05월 09일 부터 2013년 09월 01일까지 크롤링 했습니다. 학습을 위한 적절한 데이터를 수집하기 위해 10년 이상 정보를 추출하려 했습니다. 2013년 05월 09일을 기준으로 잡은 이유는 기준금리 변경일이었기 때문에 기준점으로 정했습니다. 총 114,739건의 뉴스를 수집했습니다.

     - **크롤링 코드**
      
        <details>
          <summary>Python Code</summary>
        
          ```python
          import requests
          from bs4 import BeautifulSoup
          import os
          
          # 크롤링할 페이지의 수를 추출
          url = f"<https://news.einfomax.co.kr/news/articleList.html?page=1&total=6417&sc_section_code=&sc_sub_section_code=&sc_serial_code=&sc_area=A&sc_level=&sc_article_type=&sc_view_level=&sc_sdate=2019-01-01&sc_edate=2019-12-31&sc_serial_number=&sc_word=%EA%B8%88%EB%A6%AC&box_idxno=&sc_multi_code=&sc_is_image=&sc_is_movie=&sc_user_name=&sc_order_by=E&view_type=sm>"
          headers = {
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
              'Referer': '<https://www.naver.com/>'
              }
          base = '<https://news.einfomax.co.kr>'
          response = requests.get(url, headers=headers)
          soup = BeautifulSoup(response.text, 'html.parser')
          total = soup.select_one('#sections > section > header > h3 > small').text
          total_num = ''
          for i in total:
              if i.isdigit():
                  total_num += i
          total_num = int(total_num)
          page_num_0 = total_num / 20
          page_num_1 = total_num // 20
          if page_num_0 != page_num_1:
              pages = page_num_1 + 1
          else:
              pages = page_num_1
          pages #1~페이지부터 pages 까지 크롤링
          for page in range(1,pages+1):
              url = f"<https://news.einfomax.co.kr/news/articleList.html?page={page}&total=6417&sc_section_code=&sc_sub_section_code=&sc_serial_code=&sc_area=A&sc_level=&sc_article_type=&sc_view_level=&sc_sdate=2019-01-01&sc_edate=2019-12-31&sc_serial_number=&sc_word=%EA%B8%88%EB%A6%AC&box_idxno=&sc_multi_code=&sc_is_image=&sc_is_movie=&sc_user_name=&sc_order_by=E&view_type=sm>"
              headers = {
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                  'Referer': '<https://www.naver.com/>'
                  }
              base = '<https://news.einfomax.co.kr>'
              response = requests.get(url, headers=headers)
              soup = BeautifulSoup(response.text, 'html.parser')
              li_tg = soup.select('ul.type2>li>h4.titles>a') #해당 페이지에 있는 뉴스기사 링크 리스트
              for i in li_tg:
                  target = i.attrs['href']
                  crawling_url = base + target
                  response = requests.get(crawling_url, headers=headers)
                  crawling_soup = BeautifulSoup(response.text, 'html.parser') # 해당 뉴스기사 링크의 html 정보 추출
                  title = crawling_soup.select_one('h3.heading').text
                  new_title = '' #타이틀 전처리 결과
                  for i in title:
                      if i == "/":
                          new_title += "_"
                      else:
                          new_title += i
                  date_li = crawling_soup.select('ul.infomation>li')[1].text
                  date_li = date_li.split("입력")
                  date = date_li[-1]
                  date = date.replace('.','_')
                  date = date.replace(':','_')
                  
                  date #날짜
                  info = crawling_soup.select_one('#article-view-content-div').text
                  info = info.replace('\\n','')
                  info = info.replace('\\r','')
                  info = info.replace('\\t','')
                  info #내용
                  
                  #파일 작성
                  print(f'./news/2019{date}_연합인포맥스.text')
                  with open(f'./news/2019/{date}_연합인포맥스.text', 'w', encoding='utf-8') as f:
                      f.write('제목\\n')
                      f.write(f'{new_title}\\n')
                      f.write('\\n')
                      f.write('내용\\n')
                      f.write(f'{info}\\n')
          ```
        
        
      </details>

4. **콜 금리 / 기준 금리 크롤링**
   - 한국은행 경제통계시스템에서 일별 콜 금리 및 기준 금리 데이터 파일 다운로드 했습니다.


<br>

### 데이터 전처리
* 사용 라이브러리 : eKoNLPy [GitHub - entelecheia/eKoNLPy: Korean NLP Python Library for Economic Analysis](https://github.com/entelecheia/eKoNLPy)
* 사용 모듈 : MPKO


<br>

1. **크롤링한 데이터 전처리**:
    - 수집한 데이터에서 영어와 특수기호를 제거하고 한글만을 남겨 토큰화를 진행했습니다. 이 단계에서 불필요한 텍스트 요소들을 정리하여 분석에 필요한 부분만을 남겼습니다.
2. **필요한 품사의 토큰만 추출**:
    - 논문 분석 결과에 따라 "NNG" (명사 일반), "VA" (형용사), "VAX" (형용사 특수), "MAG" (부사 일반), "VV" (동사) 등 5가지 품사의 토큰만을 추출했습니다. 이 품사들은 경제 텍스트에서 중요한 의미를 가지는 요소들로, 이후 감정 분석 및 모델링에 활용되었습니다.
3. **자료 통합**:
    - 추출한 각각의 토큰 데이터를 하나의 자료로 통합하여, 분석에 필요한 모든 텍스트를 하나의 데이터 프레임으로 관리했습니다. 이를 통해 데이터를 효율적으로 처리하고, 분석 결과의 일관성을 유지했습니다.
4. **관련 용어 n-gram 토큰화**
   * 크롤링한 데이터를 ekonlpy의 MPKO모듈을 사용하여 경제 관련 용어를 n-gram 토큰으로 저장하였습니다.        
5. **라벨링**
   * 기준 금리 발표일을 기준으로 단위기간 설정했습니다.(약 1개월)
   * 이전 단위기간 대비 콜 금리 변동이 0.1이상 상승/하락시 1(상승)/2(하락)으로 라벨링, 그 외에는 0(변동없음)으로 라벨링했습니다.
      <img width="563" alt="Screenshot 2024-11-17 at 5 27 37 PM" src="https://github.com/user-attachments/assets/a7e0fa61-7ce1-4838-ae75-90fe951a21b9">





<br>

## 3. 모델링

### 모델 개발
  1. **Naive Bayes Classifier 감정 분류 코드 구현**
     1. **부분 언더샘플링 적용 및 토큰 집계**
       * **문서 간 레이블의 불균형을 해결**하기 위해, 하락 레이블을 기준으로 80%인 40,343개씩 각 레이블(상승, 동결, 하락)에서 랜덤 샘플링을 진행했습니다.
       * 각 샘플에서 **n-gram 토큰의 유니크 집합**을 생성하고, 각 토큰이 특정 극성의 문서에 몇 번 등장했는지 집계합니다.
       * 학습 데이터는 1~5-gram으로 변환되었으며, 최소 빈도수 15 이상인 n-gram만을 사용합니다. 이 과정에서 **자주 사용되지 않는 n-gram**은 학습에서 제외하여 노이즈를 줄입니다.
     2. **Naive Bayes 확률 계산**
       * 각 샘플 내의 **토큰별로 극성에 대한 확률을 계산**하여, 문서가 특정 극성(상승, 동결, 하락)으로 분류될 확률을 구합니다.
     3. **문서 극성 라벨링**
       * 모든 문서에 대해 계산된 확률을 기반으로 **문서의 극성을 결정**하며, 가장 높은 확률을 가지는 극성으로 문서를 리라벨링합니다.
     4. **시장 접근법**
       * 극성(상승, 동결, 하락)으로 분류된 문서들을 **Naive Bayes Classifier** 모델에 학습시킵니다.
       * 모든 문서에 대해 Naive Bayes 분류기를 사용해 **극성을 상승, 동결, 하락으로 다시 삼진 분류**한 후, 한 기간 동안 가장 많이 등장한 극성을 기준으로 실제 기준 금리 변동과 비교합니다.
    

<br>

### 모델 검증
* cm1: 뉴스&채권분석보고서 기반 예측 결과 
* cm2: 의사록 기반 예측 결과


#### 코드
  <details>
    <summary>Python Code</summary>
  
    ```python
  	import csv
  	import pandas as pd
  	
  	df = pd.read_csv('updated_df_token.csv')
  	interest_rate = pd.read_csv("interest_rate.csv") 
  	base_rate = pd.read_csv('base_rate.csv')
  	
  	x0 = df[df['predicted_rate_change'] == 0]
  	x1 = df[df['predicted_rate_change'] == 1]
  	x2 = df[df['predicted_rate_change'] == 2]
  	
  	x0_count =  x0.groupby(x0.index).size()
  	x1_count =  x1.groupby(x1.index).size()
  	x2_count =  x2.groupby(x2.index).size()
  	
  	interest_rate['0'] = x0_count.reindex(interest_rate.index).fillna(0).astype(int)
  	interest_rate['1'] = x1_count.reindex(interest_rate.index).fillna(0).astype(int)
  	interest_rate['2'] = x2_count.reindex(interest_rate.index).fillna(0).astype(int)
  	
  	interest_rate['polarity'] = base_rate['polarity']
  	interest_rate['pred'] = interest_rate[['0', '1', '2']].idxmax(axis=1)
  	
  	
  	correct_predictions = (interest_rate['pred'] == interest_rate['polarity']).sum()
  	total_predictions = len(interest_rate)
  	
  	accuracy = correct_predictions / total_predictions
  	print(f"'pred'와 'polarity'의 정확도: {accuracy:.2f}")
    ```
  
  
  </details>
  
  **accuracy:0.55**
  
  
  <details>
    <summary>Python Code</summary>
  
    ```python
  	import pandas as pd
  	import numpy as np
  	import seaborn as sns
  	import matplotlib.pyplot as plt
  	from sklearn.metrics import confusion_matrix
  	
  	
  	base_rate = pd.read_csv("C:/Users/SesacPython/Desktop/dataset/금리예측프로젝트/base_rate.csv")
  	
  	# confusion matrix
  	# cm1 - 뉴스 기반 예측 기준
  	# cm2 - 의사록 기반 예측 기준
  	y_true = list(base_rate.polarity)
  	y_pred_by_news = list(base_rate.pred)
  	y_pred_by_mpc = list(base_rate.mpc_pol_pred)
  	cm1 = confusion_matrix(y_true, y_pred_by_news)
  	cm2 = confusion_matrix(y_true, y_pred_by_mpc)
  	
  	# accuracy, precision, recall, f1 score 계산
  	cm1_accuracy = sum([cm1[i][i] for i in range(3)]) / sum(sum(cm1))
  	cm2_accuracy = sum([cm2[i][i] for i in range(3)]) / sum(sum(cm2))
  	
  	cm1_precision_0 = cm1[0][0] / sum([cm1[i][0] for i in range(3)])
  	cm1_precision_1 = cm1[1][1] / sum([cm1[i][1] for i in range(3)])
  	cm1_precision_2 = cm1[2][2] / sum([cm1[i][2] for i in range(3)])
  	
  	
  	cm2_precision_0 = cm2[0][0] / sum([cm2[i][0] for i in range(3)])
  	cm2_precision_1 = cm2[1][1] / sum([cm2[i][1] for i in range(3)])
  	cm2_precision_2 = cm2[2][2] / sum([cm2[i][2] for i in range(3)])
  	
  	
  	cm1_recall_0 = cm1[0][0] / sum(cm1[0])
  	cm1_recall_1 = cm1[1][1] / sum(cm1[1])
  	cm1_recall_2 = cm1[2][2] / sum(cm1[2])
  	
  	
  	cm2_recall_0 = cm2[0][0] / sum(cm2[0])
  	cm2_recall_1 = cm2[1][1] / sum(cm2[1])
  	cm2_recall_2 = cm2[2][2] / sum(cm2[2])
  	
  	cm1_f1_0 = 2*cm1_precision_0*cm1_recall_0 / (cm1_precision_0 + cm1_recall_0)
  	cm1_f1_1 = 2*cm1_precision_1*cm1_recall_1 / (cm1_precision_1 + cm1_recall_1)
  	cm1_f1_2 = 2*cm1_precision_2*cm1_recall_2 / (cm1_precision_2 + cm1_recall_2)
  	
  	cm2_f1_0 = 2*cm2_precision_0*cm2_recall_0 / (cm2_precision_0 + cm2_recall_0)
  	cm2_f1_1 = 2*cm2_precision_1*cm2_recall_1 / (cm2_precision_1 + cm2_recall_1)
  	cm2_f1_2 = 2*cm2_precision_2*cm2_recall_2 / (cm2_precision_2 + cm2_recall_2)
  	
  	# sklearn 활용(cm1)
  	from sklearn.metrics import classification_report
  	print(classification_report(y_true, y_pred_by_news))
    ```
  
  
  </details>


<br>

#### cm1&cm2 Confusion Matrix
![](https://i.imgur.com/fe9h8na.png)

<br>

#### cm1(뉴스&채권분석 보고서 기반 예측 결과)
![](https://i.imgur.com/R12hQ42.png)
![](https://i.imgur.com/FS4NJev.png)

<br>

#### cm2(의사록 기반 예측 결과)
![](https://i.imgur.com/PIT2SqV.png)
![](https://i.imgur.com/19k9GM6.png)

<br>

### 시각화

#### 1. 금리 동결 직전 기간(극성=0)의 Wordcloud
![3_WC2](https://github.com/user-attachments/assets/f0559f66-057b-4d1f-b00a-86d30d2af9d0)

<br>

#### 1-1. 금리 동결 직전 기간(극성=0)의 Top 20 토큰
![4_top20token_0](https://github.com/user-attachments/assets/b9fdcc55-5895-4c69-9d4b-d1a18a29dec4)

<br>

#### 2. 금리 상승 직전 기간(극성=1)의 Wordcloud
![2_WC1](https://github.com/user-attachments/assets/5f177bc6-55b1-4208-a5df-04529d9cabdd)

<br>

#### 2-1. 금리 상승 직전 기간(극성=1)의 Top 20 토큰
![6_top20token_2](https://github.com/user-attachments/assets/b1620882-209d-4272-ad4e-73620d5f7809)

<br>

#### 3. 금리 하락 직전 기간(극성=2)의 Wordcloud
![1_WC0](https://github.com/user-attachments/assets/40f2b3f7-111c-49f7-b42c-d373842bdc5e)

<br>

#### 3-1. 금리 하락 직전 기간(극성=2)의 Top 20 토큰

![5_top20token_1](https://github.com/user-attachments/assets/2a84155c-0fce-4804-9372-7428fd8e40c4)


<br>

#### 4. category별 문서 수(BD:채권분석보고서, ED:이데일리, HAN:한경, MK:매일경제)
![7_number_of_category](https://github.com/user-attachments/assets/27b76b3b-2fcb-4187-81ac-3184d99a7c5a)


<br>

#### 5. 극성 및 카테고리 별 문서 수
![8_num_by_ratechange](https://github.com/user-attachments/assets/68e330bb-0a14-4509-86bd-fdefc98c8f5e)

<br>

#### 6. 극성 및 카테고리 별 단위기간당 문서 수
![9_num_by_ratechange_per_period](https://github.com/user-attachments/assets/7f4220cd-327c-41e2-8f3b-ebbdeff29615)

<br>

#### 7. 극성 별 단위 기간 당 총 문서 수
![10_total_num_by_ratechange_per_period](https://github.com/user-attachments/assets/087e09c3-6425-44c7-a7fc-e8c828e18ad2)

<br>

#### 8. 콜 금리 & 기준금리 추이
![11_base_rate_and_call_rate](https://github.com/user-attachments/assets/370c5e91-3e57-4a25-9159-95000c7cde58)


<br>

#### 9. 기준금리 & 극성 예측(뉴스&채권 기반)
![12_base_rate_and_pred_by_news](https://github.com/user-attachments/assets/9ad45380-0e4f-4e80-9b80-0a7535bbffa4)


<br>



#### 10. 기준금리 & 극성 예측(의사록 기반)
![13_base_rate_and_pred_by_mpc](https://github.com/user-attachments/assets/26202319-24af-498c-b95b-5f6eb739c606)


<br>


## 4. 평가

### 결론
전체 극성(0: 동결, 1: 상승, 2: 하락)에 대한 정확도는 각각 0.55(cm1)와 0.45(cm2)로 높은 편은 아니지만, 상승(1)과 하락(2)에 대한 Recall 값이 매우 높은 것으로 나타났습니다.

<br>


### 기대 효과
상승과 하락에 대해 높은 Recall 값을 보인 점을 고려할 때, 다른 요소에서의 정확도를 보완한다면 금리 방향성을 보다 높은 신뢰도로 예측할 수 있을 것으로 기대됩니다.

<br>


### 한계점 및 개선 방안
현재 모델은 상승과 하락에 대해 높은 Recall 값을 보이나, 전반적인 예측 정확도가 낮아 모든 극성에 대해 균형 잡힌 성능을 제공하지 못하고 있습니다. 이는 텍스트 분석 과정에서 Ekonlpy의 MPKO를 사용해 문서를 통째로 토큰화하여 계산한 방식의 한계로 보입니다.

<br>

이를 개선하기 위해 문서를 세부적으로 나누어 정밀한 분석을 수행하고, 추가적인 특징(feature)을 추출하여 모델에 반영하는 방안을 고려할 필요가 있습니다.
