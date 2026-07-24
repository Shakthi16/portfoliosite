import sys
sys.stdout.reconfigure(encoding='utf-8')
import bs4

soup = bs4.BeautifulSoup(open('index.html','r',encoding='utf-8').read(), 'html.parser')
for string in soup.find_all(string=True):
    if '>' in string:
        parent_name = string.parent.name if string.parent else 'None'
        print(f'Text: {repr(string)} | Parent: {parent_name}')
