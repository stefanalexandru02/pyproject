import urllib.request
from html.parser import HTMLParser
from queue_writter import publish_msg
import uuid

# url = 'https://www.amazon.com/Best-Sellers/zgbs?language=en_US' -> I am getting throtteled error message on amazon links
# url = 'https://www.amazon.com/gp/goldbox?ref_=nav_cs_gb'
url = 'https://www.bing.com/search?q=python+programming&first={x}'

id = 0
scheduled_urls = []
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "a":
           for name, value in attrs:
               if name == "href" and value.startswith("http"):
                   if value in scheduled_urls:
                       continue
                   scheduled_urls.append(value)
                   global id
                   print (name, "=", value)
                   payload = {
                       "link": value,
                       "path": f"/Users/stefanalexandru/Desktop/pyproject/output/{uuid.uuid4()}"
                   }
                   id += 1
                   publish_msg(payload)


parser = MyHTMLParser()
if '{x}' in url:
    for i in range(0, 50000, 100):
        html_text = urllib.request.urlopen(url.replace('{x}', f"{i}")).read()
        html_text = f"{html_text}"
        parser.feed(html_text)
else:
    html_text = urllib.request.urlopen(url).read()
    html_text = f"{html_text}"
    parser.feed(html_text)

print("DONE. START AGAIN OR WITH ANOTHER URL.")