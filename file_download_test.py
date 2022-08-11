from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com')
driver.maximize_window()

file_download = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[17]/a').click()
download_url = 'https://the-internet.herokuapp.com/download/0405.txt'
req = requests.get(download_url)
file_name = req.url[download_url.rfind('/')+1:]

with open(file_name, 'wb+') as f:
    for chunk in req.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)

with open('0405.txt', 'r') as file:
    text = file.read()
    if text == 'File Upload':
        print('Файл загружен коректно')
    else:
        print('Файл не загружен')

driver.quit()

# Код загружает файл с сайта и проверяет на наличие содержимого