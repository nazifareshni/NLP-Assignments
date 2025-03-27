from selenium import webdriver
import time
from selenium.webdriver.common.by import By 

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get('https://www.daraz.com.bd/products/new-stylish-eyewear-frames-for-men-and-women-trendy-durable-and-comfortable-i490604933-s2373248417.html')

time.sleep(3)  # Allow page to load before refreshing
driver.refresh()
driver.maximize_window()

time.sleep(2)  # Ensure page loads
height = driver.execute_script('return document.body.scrollHeight')
print("height:", height)

# Scroll down to load all comments
for i in range(0, height + 200, 30):
    driver.execute_script(f'window.scrollTo(0,{i});')
    time.sleep(0.5)

# Wait for comments to load
time.sleep(3)

# Find comment elements (Ensure the correct class name is used)
comments = driver.find_elements(By.CLASS_NAME, 'content')  # Change 'content' to actual class

# Print extracted comments
if comments:
    for i in comments:
        print(i.text)
else:
    print("No comments found!")

time.sleep(30)  # Delay to view results before closing
driver.quit()