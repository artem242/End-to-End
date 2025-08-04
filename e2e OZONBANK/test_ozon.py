import logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# -*- coding: utf-8 -*-
import sys
import os

# Установка кодировки консоли
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

import os
import sys

print("Текущая директория:", os.getcwd())
print("Python версия:", sys.version)
print("Python путь:", sys.executable)

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def setup_driver():
    try:
        # Настройка Chrome
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")  # Окно на весь экран
        chrome_options.add_argument("--disable-notifications")  # Отключить уведомления
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)

        # Автоматическое управление ChromeDriver
        service = Service(ChromeDriverManager().install())
        
        logging.info("Инициализация драйвера...")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        logging.info("Драйвер успешно инициализирован")
        return driver
    
    except Exception as e:
        logging.error(f"Ошибка при инициализации драйвера: {e}")
        raise

def main():
    try:
        # Инициализация драйвера
        driver = setup_driver()
        
        # Открытие страницы
        logging.info("Открытие страницы Ozon Bank")
        driver.get("https://finance.ozon.ru/lk")
        
        # Ожидание загрузки страницы
        WebDriverWait(driver, 20).until(
            EC.title_is("Ozon Банк")
        )
        logging.info("Страница успешно загружена")
        
        # Пример действия (можно добавить свои действия)
        logging.info("Выполнение действий на странице...")
        time.sleep(5)  # Пауза для демонстрации
        
        # Получение заголовка страницы
        page_title = driver.title
        logging.info(f"Заголовок страницы: {page_title}")
        
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")
    
    finally:
        logging.info("Закрытие браузера")
        driver.quit()
        logging.info("Браузер закрыт")

if __name__ == "__main__":
    main()
