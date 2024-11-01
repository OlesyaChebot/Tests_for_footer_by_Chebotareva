from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.common.exceptions import NoSuchElementException
driver.maximize_window()
driver.implicitly_wait(15)


# Поиск элемента VK в футере на Главной странице
driver.get('https://only.digital/')
try:
    footer_vk=driver.find_element_by_css_selector('.sc-1d5e4d59-3.KKIrH.sc-222969c7-7.dhLjUQ>.sc-1d5e4d59-2:nth-child(2)')
except NoSuchElementException:
    print("Ошибка! Элемент VK в футере на Главной НЕ НАЙДЕН!")
else: print('Успешно. Элемент "VK" в футере на Главной найден')

# Поиск элемента "Телеграм" в футере на странице "Вакансии"
driver.get('https://only.digital/job/')
try:
    footer_tg=driver.find_element_by_css_selector('.sc-1d5e4d59-3.KKIrH.sc-222969c7-7.dhLjUQ>.sc-1d5e4d59-2:nth-child(3)')
except NoSuchElementException:
    print('Ошибка! Элемент Телеграм в футере на странице "Вакансии" НЕ НАЙДЕН!')
else: print('Успешно. Элемент "Телеграм" в футере на странице "Вакансии" найден')

# Поиск и проверка значения номера телефона в футере на странице "Компания"
driver.get('https://only.digital/company/')
try:
    tel_form = driver.find_element_by_css_selector('.sc-222969c7-5.dHBZCP>a')
except NoSuchElementException:
    print('Ошибка! Номер телефона в футере на странице "Компания" НЕ НАЙДЕН!')
else: print('Успешно. Номер телефона в футере на странице "Компания" найден')
tel_num = tel_form.get_attribute("href")
if tel_num == 'tel:+74957409979':
    print('Успешно. Номер телефона в футере на странице "Компания" верен')
else:
    print('Ошибка! Номер телефона в футере на странице "Компания" неверен')
driver.quit()

# Сообщить звуковым сигналом о завершении проверки
import winsound
duration = 1500
frequency = 2000
winsound.Beep(frequency, duration)


