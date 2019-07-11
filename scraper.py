import requests
from bs4 import BeautifulSoup
import smtplib
import time
#insert URL
URL = 'URL'
#google header agent then insert header agent
header = {'User':'header agent'}

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
