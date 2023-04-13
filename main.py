import requests
from bs4 import BeautifulSoup

query = "금융보안"
url = f"https://search.naver.com/search.naver?where=news&query={query}&sm=tab_opt&sort=1&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3Aall&is_sug_officeid=0"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.select('div.news_wrap.api_ani_send')
for article in articles:
    title = article.select_one('a.news_tit')['title']
    link = article.select_one('a.news_tit')['href']
    title = article.select_one('a.news_tit').text
    date = article.select_one('span.info').text
    source = article.select_one('a.info.press').text
    print(title)
    print(link)
    print(date)
    print(source)
    type(article.select_one('a.news_tit'))
    break


