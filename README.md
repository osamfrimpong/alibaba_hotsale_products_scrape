*Instructions*

1. Install selenium, requests and beautifulSoup packages with

pip install selenium, requests, beautifulsoup4

2. Running the following files

*categories.py* will scrape all the product categories from alibaba.com into the *categories.json* file which will be used later.

*products_by_categories.py* will start scraping the products one category after the other

*products_by_search.py* takes in a url and scrapes all the products.
There is a function in the file

findProducts("https://www.alibaba.com/catalog/alcoholic-beverages_cid204?spm=a2700.galleryofferlist_catalog.0.0.5c6434bcKhKZ4e&page=1&CatId=204&viewtype=G")

ensure to replace the url *findProducts("your list of products url goes here")*