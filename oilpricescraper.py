from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import csv


options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


url = 'https://oilprice.com/oil-price-charts/#prices'
driver.get(url)

try:
    wait = WebDriverWait(driver, 15)  # Max 15 seconds wait
    table = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'table')))


    rows = table.find_elements(By.TAG_NAME, 'tr')


    with open('oil_prices.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Futures', 'Last Price', 'Percentage Change'])  # Header row


        for row in rows[1:]:
            columns = row.find_elements(By.TAG_NAME, 'td')
            if len(columns) >= 3:
                futures = columns[0].text.strip()
                last_price = columns[1].text.strip()
                percentage_change = columns[2].text.strip()
                writer.writerow([futures, last_price, percentage_change])

    print("Data has been successfully written to oil_prices.csv")

except Exception as e:
    print("Error:", e)


driver.quit()



