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
            url = f'https://www.edaily.co.kr/search/news/?source=total&keyword=%ea%b8%88%eb%a6%ac&include=&exclude=&jname=&start={start_date}&end={end_date}&sort=&date=pick&exact=false&page=1'
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
        next_page_url = f'https://www.edaily.co.kr/search/news/?source=total&keyword=%ea%b8%88%eb%a6%ac&include=&exclude=&jname=&start={response.meta["start_date"]}&end={response.meta["end_date"]}&sort=&date=pick&exact=false&page={next_page}'
        
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