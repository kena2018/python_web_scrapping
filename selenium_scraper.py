from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH
driver.get('https://techifysolutions.com/')

time.sleep(5)  # wait for JavaScript to load the content

products = []

product_elements = driver.find_elements(By.CLASS_NAME, 'product')

for product in product_elements:
    title = product.find_element(By.CLASS_NAME, 'title').text
    price = product.find_element(By.CLASS_NAME, 'price').text
    rating = product.find_element(By.CLASS_NAME, 'rating').text
    
    products.append({
        'title': title,
        'price': price,
        'rating': rating
    })

driver.quit()

df = pd.DataFrame(products)
df.to_csv('selenium_products.csv', index=False)

print("Data saved to selenium_products.csv")
