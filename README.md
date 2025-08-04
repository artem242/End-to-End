Автоматизированное тестирование Ozon Bank
Описание проекта
Данный проект представляет собой набор автоматизированных тестов для веб-сайта Ozon Bank, реализованный с использованием Selenium WebDriver.

Требования
Python версии 3.8 или выше

Selenium для автоматизации

ChromeDriver для работы с Chrome

WebDriver Manager для автоматического управления драйверами

Установка
Клонируйте репозиторий:

git clone <ссылка_на_репозиторий>
Установите зависимости:

pip install -r requirements.txt
Структура проекта
 - основной файл с тестовым кодом

requirements.txt - список зависимостей

logs - папка для хранения логов

Основные компоненты
Импорты и настройки
import logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
Настройка драйвера
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver
Запуск тестов
Для запуска тестов выполните:

python main.py
Обработка ошибок
Система включает:

Обработку исключений

Логирование ошибок

Корректное закрытие браузера

Возможности расширения
Добавление новых тестовых сценариев

Внедрение параметризации

Интеграция с CI/CD

Добавление дополнительных проверок

Рекомендации
Регулярно обновляйте зависимости

Следите за изменениями на целевой странице

Документируйте изменения в коде

Используйте систему контроля версий

Контактная информация
По вопросам и предложениям обращайтесь:

Email: streltsovtema@yandex.ru

GitHub:https://github.com/artem242
