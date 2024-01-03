import requests
from bs4 import BeautifulSoup
from queue_writter import publish_msg
import uuid

# https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
params = {
    "q": "web scraping",
    "hl": "en",
    "gl": "uk",
    "start": 0,
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

page_limit = 500
page_num = 0

data = []

while True:
    page_num += 1
    print(f"page: {page_num}")
        
    html = requests.get("https://www.google.com/search", params=params, headers=headers, timeout=30)
    soup = BeautifulSoup(html.text, 'lxml')
    
    for result in soup.select(".tF2Cxc"):
        title = result.select_one(".DKV0Md").text
        try:
           snippet = result.select_one(".lEBKkf span").text
        except:
           snippet = None
        links = result.select_one(".yuRUbf a")["href"]
      
        # data.append({
        #   "title": title,
        #   "snippet": snippet,
        #   "links": links
        # })

        payload = {
            "link": links,
            "path": f"/Users/stefanalexandru/Desktop/pyproject/output/{uuid.uuid4()}"
        }
        publish_msg(payload)

    if page_num == page_limit:
        break

# print(json.dumps(data, indent=2, ensure_ascii=False))
print("DONE")