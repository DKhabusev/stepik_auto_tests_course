import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def calc(param):
    return str(math.log(abs(12*math.sin(int(param)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h5[id="price"]'), "$100")
    )
    button = browser.find_element(By.CSS_SELECTOR, 'button[id="book"]')
    button.click()
    x_element = browser.find_element(By.CSS_SELECTOR, "span[id=input_value]")
    x = x_element.text
    y = calc(x)
    answer_input = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer_input.send_keys(y)
    button2 = browser.find_element(By.CSS_SELECTOR, 'button[id="solve"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
    button2.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

