from selenium import webdriver
import time
from selenium.webdriver.common.by import By 
from math import ceil
import re

driver = webdriver.Chrome() 
driver.get('https://www.daraz.com.bd/mens-eyeglasses/')  


page_num = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/span[1]').text
print(page_num)

pattern = r"\d+"
match = re.search(pattern, page_num)
number = int(match.group()) if match else None
print("Extracted Number:", number)

pages = ceil(number / 40)
print(pages)

product_img = []  


for page in range(1, pages + 1):  
    p = str(page)
    driver.get(f'https://www.daraz.com.bd/mens-eyeglasses/?page={p}')  
    driver.maximize_window()  
    for i in range(1, 6):  
        j = str(i) 
        img = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[' + j + ']/div/div/div[1]/div/a/div/img').get_attribute('src')
        product_img.append(img)  


print(product_img, '\n')

time.sleep(50)  
driver.quit()