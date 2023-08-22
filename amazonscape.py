import requests
from bs4 import BeautifulSoup
import csv

# URL of the Amazon search page for bags
base_url = ' https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1'

# Create a CSV file to store the scraped data
csv_file = open('amazon_bags.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Product Name', 'Product Price', 'Rating', 'Number of Reviews', 'Product URL'])

# Scrape product listings from multiple pages
for page_num in range(1, 21):  # Scrape 20 pages
    url = base_url + str(page_num)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    product_cards = soup.find_all('div', class_='s-result-item')

    for card in product_cards:
        try:
            product_name = card.find('span', class_='a-text-normal').get_text()
        except AttributeError:
            product_name = 'N/A'

        try:
            product_price = card.find('span', class_='a-offscreen').get_text()
        except AttributeError:
            product_price = 'N/A'

        try:
            rating = card.find('span', class_='a-icon-alt').get_text().split()[0]
        except AttributeError:
            rating = 'N/A'

        try:
            num_reviews = card.find('span', class_='a-size-base').get_text().replace(',', '').split()[0]
        except AttributeError:
            num_reviews = 'N/A'

        try:
           product_link = card.find('a', class_='a-link-normal')
           if product_link is not None:
               product_url = 'https://www.amazon.com' + product_link['href']
            # Rest of your code (make sure it's indented correctly)
           else:
               print("Product link not found for this card")
        except AttributeError:
               product_url = 'N/A'


        csv_writer.writerow([product_name, product_price, rating, num_reviews, product_url])

csv_file.close()

# Now read the CSV file, visit each product URL and scrape additional information
with open('amazon_bags.csv', 'r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row

    for row in csv_reader:
        product_url = row[4]
        response = requests.get(product_url)
        soup = BeautifulSoup(response.content, 'html.parser')


    # Extract additional information based on the structure of the product detail page
    try:
        description = soup.find('div', id='productDescription').get_text().strip()
    except AttributeError:
        description = 'N/A'

    try:
        asin = soup.find('th', string='ASIN').find_next('td').get_text()
    except AttributeError:
        asin = 'N/A'

    # Continue extracting other information as needed

    # Append all information to the row
    row.append(description)
    row.append(asin)
    # Append other information

    # Write the combined information to the CSV file
    # Write the combined information to the CSV file
    with open('amazon_bags_updated.csv', 'a', newline='', encoding='utf-8') as updated_csv_file:
      updated_csv_writer = csv.writer(updated_csv_file)
      updated_csv_writer.writerow(row)

# ... Your previous code ...

# Now read the CSV file, visit each product URL and scrape additional information
with open('amazon_bags.csv', 'r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row

    for row in csv_reader:
        product_url = row[4]
        response = requests.get(product_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract additional information based on the structure of the product detail page
        try:
            description = soup.find('div', id='productDescription').get_text().strip()
        except AttributeError:
            description = 'N/A'

        try:
            asin = soup.find('th', string='ASIN').find_next('td').get_text()
        except AttributeError:
            asin = 'N/A'

        # Continue extracting other information as needed

        # Append all information to the row
        row.append(description)
        row.append(asin)
        # Append other information

# Write the combined information to the CSV file
        with open('amazon_bags_updated.csv', 'a', newline='', encoding='utf-8') as updated_csv_file:
            updated_csv_writer = csv.writer(updated_csv_file)
            updated_csv_writer.writerow(row)

    
