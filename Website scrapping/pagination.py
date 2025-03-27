from selenium import webdriver
import time
from selenium.webdriver.common.by import By 
from math import ceil
import re

driver = webdriver.Chrome()  # This line is for opening the Chrome web browser
driver.get('https://www.daraz.com.bd/mens-eyeglasses/')  # This line is for going to the link of the page we will scrape

# Extract the number of products
page_num = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/span[1]').text
print(page_num)

# Extract the number from the page text
pattern = r"\d+"
match = re.search(pattern, page_num)
number = int(match.group()) if match else None
print("Extracted Number:", number)

# Calculate number of pages and round up
pages = ceil(number / 40)
print(pages)

product_img = []  # Array to store the image URLs

# Loop through pages and scrape images
for page in range(1, pages + 1):  # Loop from page 1 to the last page
    p = str(page)
    driver.get(f'https://www.daraz.com.bd/mens-eyeglasses/?page={p}')  # Go to the page to scrape
    driver.maximize_window()  # Maximize window

    for i in range(1, 6):  # Loop to get 5 images per page
        j = str(i)  # Convert the index to string
        img = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[' + j + ']/div/div/div[1]/div/a/div/img').get_attribute('src')
        product_img.append(img)  # Append the image URL to the array

# Print the list of image URLs
print(product_img, '\n')

time.sleep(50)  # Delay to view results before closing
driver.quit()