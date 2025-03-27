from selenium import webdriver
import time
from selenium.webdriver.common.by import By 


driver = webdriver.Chrome()
driver.get('https://www.daraz.com.bd/products/new-stylish-eyewear-frames-for-men-and-women-trendy-durable-and-comfortable-i490604933-s2373248417.html')

time.sleep(3)  
driver.refresh()
driver.maximize_window()

time.sleep(2)  
height = driver.execute_script('return document.body.scrollHeight')
print("height:", height)


for i in range(0, height + 200, 30):
    driver.execute_script(f'window.scrollTo(0,{i});')
    time.sleep(0.5)


time.sleep(3)


comments = driver.find_elements(By.CLASS_NAME, 'content')  

if comments:
    for i in comments:
        print(i.text)
else:
    print("No comments found!")

time.sleep(30) 
driver.quit()