import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import smtplib

load_dotenv()

gmail_access = os.environ.get("GMAIL_APP_PASSWORD")
from_mail_id = os.environ.get("FROM_MAIL")
to_mail_id = os.environ.get("TO_MAIL")
h = os.environ.get("HEAD")

url = ""#<<<Amazon product link
response = requests.get(url, headers={"Accept-Language":"en-US,en;q=0.9"})
soup = BeautifulSoup(response.text, "html.parser")
price = soup.find(class_="a-price aok-align-center reinventPricePriceToPayMargin priceToPay").getText().split("₹")[1].replace(",","")
price = float(price)



#m=f"Subject: Time to buy \n\nThe price dropped for the product {url}\nThe price is {price}"
buy_price = 45000 #change your desired low price according to the product

if price<buy_price:
    m = f"Subject: Time to buy \n\nThe price dropped for the product {url}\nThe price is {price}"
    with smtplib.SMTP(os.environ.get("SMTP_ADDRESS")) as conn:
        conn.starttls()
        result = conn.login(user=from_mail_id, password=gmail_access)
        conn.sendmail(from_addr=from_mail_id,
                      to_addrs=to_mail_id,
                      msg=m)
