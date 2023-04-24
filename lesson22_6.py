from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(param):
    return str(math.log(abs(12*math.sin(int(param)))))


try:
    browser = webdriver.Chrome()
    browser.get("https://SunInJuly.github.io/execute_script.html")
    x_element = browser.find_element(By.CSS_SELECTOR, "span[id=input_value]")
    x = x_element.text
    y = calc(x)
    answer_input = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer_input.send_keys(y)
    checkbox_input = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    checkbox_input.click()
    radio_input = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_input)
    radio_input.click()
    button = browser.find_element(By.CSS_SELECTOR, '.btn-primary')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()