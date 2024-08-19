# pricetracker
Product Price Tracker
This script tracks the prices of specified products from Snapdeal and compares them against a target price. If the current price of the product is lower than the target price, it records the product information in a result file.
------------------------------------------------------------
Features
Scrapes the current price of products from their Snapdeal URLs.
Compares the current price with a predefined target price.
Records products that meet the target price criteria into a result file.
-----------------------------------------------------
Prerequisites
Python 3.x
requests library
beautifulsoup4 library
----------------------------------------------------
How It Works
The script uses the requests library to fetch the product page from Snapdeal.
It uses BeautifulSoup to parse the HTML and extract the product price.
The script checks if the current price is lower than the target price.
If it is, the product details are written to myresultfile.txt.
---------------------------------------------------------------------
