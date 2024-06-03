import requests
from bs4 import BeautifulSoup
import pandas as pd

# Let's scrape techify website services

url = 'https://techifysolutions.com/what-we-do/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

services = []

# Find the class for which data you want to scrap
if soup.find_all('div', class_="content_main three-col"):

    for product in soup.find_all('div', class_="media-body"):
        
        title = product.find('h5').get_text()
        service_detail = product.find('p').get_text()
        
        services.append({
            'title': title,
            'service_detail': service_detail
        })

# write data into csv
df = pd.DataFrame(services)
df.to_csv('beautifulsoup_services.csv', index=False)

print("Data saved to beautifulsoup_services.csv")
