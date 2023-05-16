import requests
from bs4 import BeautifulSoup
from daum_news_fnc import get_news_title_and_content

url = "https://news.daum.net/breakingnews/digital"


result = requests.get(url)
title = doc.select("h3.tit_view")[0].get_text()
contents = doc.select("section > p")
soup = BeautifulSoup(result.text, "html.parser")

title_list = soup.select("ul.list_news2 a.link_txt")
for i, tag in enumerate(title_list):
    new_url = tag["href"]
    title, content = get_news_title_and_content(new_url)
    print("=" * 100)
    print(f"URL: {new_url}")
    print(f"{i+1} 뉴스 제목: {title}")
    print("=" * 100)
    print(f"{i+1} 뉴스 본문: {content}")

# TODO: 태그 목록에서 URL 추출 + 단건뉴스 수집