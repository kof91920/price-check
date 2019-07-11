import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/Apple-MacBook-Retina-2-3GHz-Quad-Core/dp/B072QG8BX6/ref=sr_1_2_sspa?keywords=mac+pro&qid=1562882066&s=gateway&sr=8-2-spons&psc=1'

header = {'User':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def check_price(URL):
    page = requests.get(URL, headers=header)
    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(id="priceblock_ourprice").get_text()

    to_num = float(''.join(price[1:].split(',')))
    if to_num < 1000:
        send_email()

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    #insert your email, password
    server.login('email', 'password')
    subject = "price gone down"
    body = "chekc this " + URL
    msg = f"Subject:{subject}\n\n{body}"
    #insert from, to email
    server.sendmail('from', 'to',msg)
    print('sent')
    server.quit()

if __name__ == "__main__":
    while (True):
        check_price(URL)
        time.sleep(60*60*8)