import bs4
import requests
import htmlmin

url = "https://www.scrapethissite.com/pages/forms/"
soup = bs4.BeautifulSoup(requests.get(url).text, 'html.parser')
minified_html = htmlmin.minify(str(soup), remove_empty_space=True)
print(minified_html)