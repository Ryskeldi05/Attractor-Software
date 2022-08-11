from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com')
driver.maximize_window()

form_authentication = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[21]/a').click()
user_name = driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('Ryskeldi')
paswrd = driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Ryskeldi')
login_button = driver.find_element(By.XPATH, '//*[@id="login"]/button/i').click()
check_correct = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="flash"]'))).text
correct = 'Your username is invalid!\n×'
assert check_correct == correct, f'Тест не пройден: {check_correct}'
driver.quit()

# Код проверяет на обработку неправильно введенных данных






