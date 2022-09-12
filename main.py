import bs4
import requests
from fake_headers import Headers
import re

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
url = 'https://habr.com/ru/all/'
url_1 = 'https://habr.com'

def page_scrap(url):
    response = requests.get(url, headers = Headers(os='lin',headers=True ).generate())
    response.raise_for_status()
    text = response.text
    soup = bs4.BeautifulSoup(text, features = 'html.parser')
    articles = soup.find_all('article')
    # print(articles)
    for article in articles:
        title = article.find('h2').find('span').text
        # print(title)
        date = article.find(class_='tm-article-snippet__meta').find('time').attrs['title'].split(',')
        # print(date[0])
        href= article.find(class_='tm-article-snippet__title-link').attrs['href']
        link = url_1+href
        search_words(date, title, link)
        # print(link)
        # print(f'<{date[0]}>-<{title}>-<{link}>')
        # print('-----')

def search_words(date, title, link, list_words=KEYWORDS):
    KEYWORDS = '|'.join(list_words)
    response = requests.get(link, headers = Headers(os='lin',headers=True ).generate())
    response.raise_for_status()
    text = response.text
    soup = bs4.BeautifulSoup(text, features = 'html.parser')
    art_text = soup.find(class_='tm-article-body')
    # print(art_text.text)
    if re.search(KEYWORDS, art_text.text) ==None:
        print('The article does not have necessary words')
    else:
        print(f'<{date[0]}>-<{title}>-<{link}>')



    
if __name__ == '__main__':
    page_scrap(url)
  
