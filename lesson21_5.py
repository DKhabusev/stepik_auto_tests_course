from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(param):
    return str(math.log(abs(12*math.sin(int(param)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    x_element = browser.find_element(By.CSS_SELECTOR, "img[id=treasure]")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    answer_input = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer_input.send_keys(y)
    checkbox_input = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    checkbox_input.click()
    radio_input = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio_input.click()
    button = browser.find_element(By.CSS_SELECTOR, '.btn-default')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()