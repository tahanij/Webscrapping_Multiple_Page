#!/usr/bin/env python
# coding: utf-8

# In[8]:


from bs4 import BeautifulSoup
import openpyxl

# Function to scrape data from a single page
def scrape_page(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    product_divs = soup.find_all('div', class_='a-section a-spacing-small a-spacing-top-small')

    product_names = []
    product_prices = []
    product_reviews = []

    for div in product_divs:
        # Find product name
        product_name_tag = div.find('span', class_='a-size-medium a-color-base a-text-normal')
        product_name = product_name_tag.text.strip() if product_name_tag else ""

        # Find product price
        product_price_tag = div.find('span', class_='a-offscreen')
        product_price = product_price_tag.text.strip() if product_price_tag else ""

        # Find product reviews
        product_reviews_tag = div.find('i', class_='a-icon a-icon-star-small a-star-small-4 aok-align-bottom')
        product_review = product_reviews_tag.text.strip() if product_reviews_tag else ""

        # Append data to lists
        product_names.append(product_name)
        product_prices.append(product_price)
        product_reviews.append(product_review)

    return product_names, product_prices, product_reviews

# Function to write data to Excel
def write_to_excel(product_data, excel_file):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Product_Name", "Product_Price", "Product_Reviews"])

    for name, price, review in zip(*product_data):
        ws.append([name, price, review])

    wb.save(excel_file)

# Main function to scrape multiple pages
def scrape_multiple_pages(html_files, excel_file):
    all_product_data = ([], [], [])
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as file:
            html_content = file.read()
            product_data = scrape_page(html_content)
            for i, data in enumerate(product_data):
                all_product_data[i].extend(data)
    
    write_to_excel(all_product_data, excel_file)

# Example usage
html_files = ["Amazon_page1.html", "Amazon_page2.html","Amazon_page3.html"]  
excel_file = "Amazon_Multiple_Products.xlsx"  
scrape_multiple_pages(html_files, excel_file)


# In[ ]:




