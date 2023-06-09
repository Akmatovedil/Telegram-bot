from pprint import pprint
import requests
from bs4 import BeautifulSoup as BS

URL = "https://rezka.ag/cartoons/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}


def get_html(url, params=""):
    req = requests.get(url=url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BS(html, "html.parser")
    items = soup.find_all("div", class_="b-content__inline_item")
    cartoons = []
    for item in items:
        desc = item.find("div", class_="b-content__inline_item-link").find('div').getText().split(", ")
        if len(desc) != 3:
            desc.insert(1, "Неизвестно!")
        cartoons.append({
            "title": item.find("div", class_="b-content__inline_item-link").find('a').getText(),
            "date": desc[0],
            "country": desc[1],
            "genre": desc[2],
            "link": item.find("div", class_="b-content__inline_item-link").find('a').get("href"),
            "info": item.find("span", class_="info").getText() if item.find("span",
                                                                            class_="info") is not None else "Полнометражный Фильм"
        })
    return cartoons


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        answer = []
        for page in range(1, 2):
            html = get_html(f"{URL}page/{page}/")
            answer.extend(get_data(html.text))
        return answer
    else:
        raise Exception("Error in parser!")


pprint(parser())
# get_data(html.text)
