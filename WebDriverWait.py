
import os
import time
# os.system("python /Users/vit/Downloads/mundus_2020_summer.py")
# time.sleep(340)
# os.system("python /Users/vit/Downloads/decanter_2019.py")
# time.sleep(340)
# os.system("python /Users/vit/Downloads/")

from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Firefox()
    browser.get(link)



    # Отправляем заполненную форму

    # time.sleep(5)
    # new_window = browser.window_handles[1]
    # browser.switch_to.window(new_window)


    # Ваш код, который заполняет обязательные поля

    # lastname = browser.find_element_by_name('lastname')
    # lastname.send_keys('solomonov')
    # email = browser.find_element_by_name('email')
    # email.send_keys('adsf@fksl.com')


    button = WebDriverWait(browser, 25).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )
    print (type(button))
    browser.find_element_by_id('book').click()

    x = browser.find_element_by_id('input_value').text
    print (x)
    x = calc(int(x))
    print (x)
    inpu1 = browser.find_element_by_id('answer')
    inpu1.send_keys(x)


    # current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    # file_path = os.path.join(current_dir, 't.txt')  # добавляем к этому пути имя файла

    # file_att.send_keys(file_path)


    button = browser.find_element_by_id("solve")


    # Отправляем заполненную форму

    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(0)
    # закрываем браузер после всех манипуляций
    browser.quit()



# не забываем оставить
