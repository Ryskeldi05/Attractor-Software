from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com')
driver.maximize_window()


dropdown = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[11]/a').click()
options = driver.find_element(By.XPATH, '//*[@id="dropdown"]').click()
selected_option = driver.find_element(By.XPATH, '//*[@id="dropdown"]/option[3]').click()

check_option = driver.find_element(By.XPATH, '//*[@id="dropdown"]/option[3]').text
correct_option = 'Option 2'

assert check_option == correct_option, f'Тест не пройден: {check_option}'

driver.quit()

# Код определяет корректность выбора из выпадающей строчки