from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Set Chrome options with unique user data directory
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=/tmp/chrome-data-{}".format(int(time.time())))
chrome_options.add_argument("--no-sandbox")  # Required for Linux VM
chrome_options.add_argument("--disable-dev-shm-usage")  # Avoids memory issues
chrome_options.add_argument("--headless")  # Run in headless mode for VM

driver = webdriver.Chrome(options=chrome_options)
url = "https://sodhis.in/product/sodhis-magaj-kharbooja-100-gm"

try:
    driver.get(url)
    time.sleep(3)  # Wait for JavaScript
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    name_div = soup.find('div', class_='sc-e5555ddc-22 kfCvMK')
    price_div = soup.find('div', class_='sc-e5555ddc-29 jcDNlL')

    if name_div and price_div:
        name = name_div.text.strip()
        price = price_div.text.strip()
        print(f"{name:<40} {price}")
    else:
        print("Could not find data.")
        with open('page_selenium.html', 'w', encoding='utf-8') as f:
            f.write(soup.prettify())
        print("Saved HTML to page_selenium.html.")

finally:
    driver.quit()
