from idlelib.browser import file_open

import requests
from bs4 import BeautifulSoup


trackprod = [
    {
    "produrl": "https://www.snapdeal.com/product/coregenix-spider-enc-bluetooth-true/674646514342#bcrumbLabelId:46102452",
    "name": "COREGENIX SPIDER",
    "targetprice":700
    },
    {
        "produrl": "https://www.snapdeal.com/product/vertical9-bluetooth-calling-type-c/673063480213#bcrumbLabelId:46102452",
        "name": "Vertical9 Bluetooth",
        "targetprice":350
    },
    {
        "produrl": "https://www.snapdeal.com/product/portronics-radian-soundbar/659262572317#bcrumbLabelId:46102431",
        "name": "Portronics Bluetooth",
        "targetprice": 500
    },
    {
        "produrl": "https://www.snapdeal.com/product/portronics-decibel-23-soundbar/658937140099#bcrumbLabelId:46102431",
        "name": "Portronics Decibel ",
        "targetprice": 1450
    },
    {
        "produrl": "https://www.snapdeal.com/product/vehop-douro-12hrs-playtime-with/628851890519#bcrumbLabelId:46102452",
        "name": "VEhop DOURO",
        "targetprice":400
    }
]



def giveprice(URL):

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 OPR/70.0.3728.106"
    }

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    prodprice = soup.find("span", {"class": "payBlkBig"})

    if (prodprice is None):
        prodprice = soup.find("div", {"class": "pdpCutPrice "})

    return prodprice.getText()



resultfile= open('myresultfile.txt','w')

try:
    for everyprod in trackprod:
        realprice = giveprice(everyprod.get("produrl"))
        realprice = realprice.replace(',', '')
        print(realprice + "-" + everyprod.get("name"))

        newprice = int(realprice)
        if (newprice < everyprod.get("targetprice")):
            print("Avaliable at offer price \n")
            resultfile.write(everyprod.get("name") + '-\t' + 'Availiable at target Price' + '\t' +'Current Price' +'-\t' + str(newprice) + '\n')
        else:
            print("not at offer price \n")

finally:
    resultfile.close()