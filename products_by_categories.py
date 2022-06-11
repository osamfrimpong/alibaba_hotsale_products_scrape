import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import json



def findProducts(productListUrl):
    opts = Options()
    opts.headless = True
    driver = webdriver.Chrome(options=opts)

    driver.get(productListUrl)

    time.sleep(2)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    time.sleep(5)

    items = driver.find_elements(by=By.CLASS_NAME, value="elements-title-normal")

    print("Items Length: {}".format(len(items)))


    for i in items:
        appendUrl(i.get_attribute("href"))

    driver.close()


def appendUrl(url):
    print("Getting URL: {}".format(url))
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    tag_wrap = soup.find('div', class_='ma-tag-wrap')

    try:
        hot_sale_div = tag_wrap.find('div', class_='hot-sale-tag-1')
    except:
        hot_sale_div = None

    if(hot_sale_div != None):
        if hot_sale_div.attrs['style'] == 'display:none':
            print("Not a hot sale product")
        else:
            print("Hot sale product")
            # append url
            f = open('urls.txt', "a+")
            f.write(url+',\n')
            f.close()
            print("Url Added")
        

def loadCategories():
    with open('categories.json') as json_file:
        data = json.load(json_file)
        i = 0
        for key, value in data.items():
            i += 1
            print("Finding Item {} of {}".format(i,len(data)))
            findProducts(value)
        

# findProducts("https://www.alibaba.com/catalog/other-agriculture-products_cid135")

loadCategories()