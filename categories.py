from cgitb import handler
import requests
from bs4 import BeautifulSoup
import json

def parser():
    url = 'https://www.alibaba.com/Products'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    name_dict = {}
    for l in soup.find_all('li'):
        content = l.find('a')
        if content:
            href = content.get('href')
            raw_name = content.get_text().replace('\n',"")
            name = raw_name.lstrip(" ")
            if(href.find("_cid")) != -1:
                name_dict[name.rstrip()] = href
            if href.find('_pid') != -1:
                name_dict[name.rstrip()] = href
    return name_dict



with open('categories.json', 'w') as f:
    json.dump(parser(), f)