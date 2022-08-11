from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com')
driver.maximize_window()


key_press = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[31]/a').click()
entered_key = driver.find_element(By.XPATH, '//*[@id="target"]').send_keys("K")
result_key = driver.find_element(By.XPATH, '//*[@id="result"]').text

assert result_key == 'You entered: K', f'Тест не пройден: {entered_key}'


driver.quit()

# Код оценивает коректность работы key press страницы