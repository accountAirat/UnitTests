from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


def main():
    # Создание экземпляра драйвера Chrome
    driver = webdriver.Chrome()

    # Переход на веб-сайт Google
    driver.get("http://www.google.com/")

    # Нахождение элемента по имени
    search_box = driver.find_element(By.NAME, "q")

    # Ввод текста "GeekBrains" в поисковую строку
    search_box.send_keys("GeekBrains")

    # Отправка формы (нажатие клавиши Enter)
    search_box.send_keys(Keys.RETURN)

    # Добавьте задержку для того, чтобы страница успела загрузиться (необязательно)
    time.sleep(2)


if __name__ == "__main__":
    main()
