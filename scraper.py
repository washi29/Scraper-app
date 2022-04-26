import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.ebay.com/itm/133609600870?hash=item1f1bc0b766:g:NAcAAOSw6DBf3AyP:sc:ShippingMethodExpress!19446!US!-1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}


def check_price():
    page=requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(id="prcIsum").get_text()

    converted_price = float(price[4:7])


    if(converted_price > 900.0):
        send_mail()

    print(converted_price)

def send_mail():
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('abrarwashi4@gmail.com','mxwhmtpzzipotjgl')
    
    subject='Price fell down!'
    body = 'check ebay link https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1311&_nkw=macbook+pro&_sacat=0'
    
    msg = f"subject: {subject}\n\n{body}"
    
    server.sendmail(
        'abrarwashi4@gmail.com',
        'aw3366@drexel.edu',
        msg
    )
    print("Hey email has been sent.")
    
    server.quit()
    
    
while(True):
    check_price()
    time.sleep(60*60)
    