from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get("https://appbrewery.github.io/Zillow-Clone/", headers=header)
data = response.text
soup = BeautifulSoup(data, "html.parser")

all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
all_links = [link["href"] for link in all_link_elements]

all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
all_address = [address.get_text().replace("|", " ").strip() for address in all_address_elements]

all_price_element = soup.select(".PropertyCardWrapper__StyledPriceLine")
all_price = [price.get_text().replace("/mo", " ").split("+")[0] for price in all_price_element if "$" in price.text]

# filling out the google form using selenium

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

google_form_link = "https://docs.google.com/forms/d/e/1FAIpQLScrMPEZdL1oaP8x_eb4lS4CETlIqaWRjWpTZymO0EBZK62z1w/viewform?usp=sf_link"

for n in range(len(all_links)):
    driver.get(google_form_link)
    time.sleep(2)

    address = driver.find_element(By.XPATH,
                value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH,
                value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH,
                value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH,
                value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    address.send_keys(all_address[n])
    price.send_keys(all_price[n])
    link.send_keys(all_links[n])
    submit_button.click()

