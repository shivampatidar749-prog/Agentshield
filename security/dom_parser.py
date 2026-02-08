from bs4 import BeautifulSoup

def parse_dom(html):
    soup = BeautifulSoup(html, "lxml")

    return {
        "visible_text": soup.get_text().lower(),
        "hidden_elements": soup.find_all(style=lambda x: x and "display:none" in x),
        "forms": soup.find_all("form"),
        "buttons": soup.find_all("button"),
        "scripts": soup.find_all("script")
    }
