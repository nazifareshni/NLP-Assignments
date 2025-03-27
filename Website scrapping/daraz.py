from selenium import webdriver
import time
from selenium.webdriver.common.by import By 


driver= webdriver.Chrome()


driver.get('https://www.daraz.com.bd/mens-fashion-glasses/')

driver.maximize_window()
product_title=[]
for i in range(1,41):
    j=str(i)
    text = driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div['+j+']/div/div/div[2]/div[2]/a').text
    product_title.append(text)
print (product_title)
print(text)
time.sleep(10)
driver.quit()
