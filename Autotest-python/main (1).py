import os
import re
import random
import pyautogui
from pathlib import Path
from time import sleep


import self as self
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


def init_browser():
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    # Инициируем экземляр браузера Google Chorme, указав путь до его драйвера
    browser = webdriver.Chrome(service=Service(str(Path(__file__).parent / 'chromedriver.exe')))

    return browser

def test_button(browser):
    browser.get('https://demoqa.com/buttons')
    # Поиск кнопки по названию на ней, последующее нажатие
    button = browser.find_element(By.XPATH, '//button[text()="Click Me"]')
    button.click()

    result = browser.find_element(By.ID, 'dynamicClickMessage')
    print(f'Вывожу то, что у меня в переменной result: {result}')
    result_text = result.text
    print(f'Вывожу то, что у меня в переменной result_text: {result_text}')

    # Верификация того, что после нажатия отображается соответствующий текст
    assert result_text == 'You have done a dynamic click'


def test_dynamic_btn(browser):
    browser.get('https://demoqa.com/dynamic-properties')
    # Явное ожидание видимости кнопки до 10 секунд с периодичностью в 2.3
    btn = WebDriverWait(browser, timeout=10, poll_frequency=2.3).until(
        EC.visibility_of_element_located((By.ID, 'visibleAfter'))
    )
    btn.click()

def test_getting_to_textbox(browser):
    # Переходим на страницу, где необходимо ввести данные
    browser.get('https://demoqa.com/text-box')
    # Локатор по аттрибуту id
    fullname_form = browser.find_element(By.ID, 'userName')
    # Введем в элемент поля ввода запроса следующий запрос
    fullname_form.send_keys('Arnold Schwarzenegger')
    # Локатор по аттрибуту id
    email_form = browser.find_element(By.ID, 'userEmail')
    # Введем в элемент поля ввода запроса следующий запрос
    email_form.send_keys('arnold@schwarzenegger.com')
    # Локатор по аттрибуту id
    caddress_form = browser.find_element(By.ID, 'currentAddress')
    # Введем в элемент поля ввода запроса следующий запрос
    caddress_form.send_keys('Santa Monica')
    # Локатор по аттрибуту id
    paddress_form = browser.find_element(By.ID, 'permanentAddress')
    # Введем в элемент поля ввода запроса следующий запрос
    paddress_form.send_keys('USA')
    # Отправим запрос
    submit_click = browser.find_element(By.ID, 'submit')
    submit_click.location_once_scrolled_into_view
    submit_click.click()

    # Убедимся, что вводимые данные в поле Full Name соответствуют выводимым внизу
    result1 = browser.find_element(By.ID, 'name')
    print(f'Вывожу то, что у меня в переменной result: {result1}')
    result1_text = result1.text
    print(f'Вывожу то, что у меня в переменной result_text: {result1_text}')

    # Верификация того, что после нажатия отображается соответствующий текст
    assert result1_text == 'Name:Arnold Schwarzenegger'

    # Убедимся, что вводимые данные в поле Email соответствуют выводимым внизу

    result2 = browser.find_element(By.ID, 'email')
    print(f'Вывожу то, что у меня в переменной result: {result2}')
    result2_text = result2.text
    print(f'Вывожу то, что у меня в переменной result_text: {result2_text}')
    assert result2_text == 'Email:arnold@schwarzenegger.com'

    # Убедимся, что вводимые данные в поле Current Address соответствуют выводимым внизу

    result3 = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[6]/div/p[3]')
    print(f'Вывожу то, что у меня в переменной result: {result3}')
    result3_text = result3.text
    print(f'Вывожу то, что у меня в переменной result_text: {result3_text}')
    assert result3_text == 'Current Address :Santa Monica'

    result4 = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[6]/div/p[4]')
    print(f'Вывожу то, что у меня в переменной result: {result4}')
    result4_text = result4.text
    print(f'Вывожу то, что у меня в переменной result_text: {result4_text}')
    assert result4_text == 'Permananet Address :USA'


def test_uploading_files(browser):
    browser.get('https://demoqa.com/upload-download')
    upload_button = browser.find_element(By.XPATH, '//*[@id="uploadFile"]')
    # Загрузим файл, который скачали по кнопке выше
    upload_button.send_keys(os.getcwd() + '/main_koveshnikov.py')

    file_name_verification = browser.find_element(By.XPATH, r'//p[text()="C:\fakepath\main_koveshnikov.py"]')
    file_name_verification_text = file_name_verification.text
    assert file_name_verification_text == r'C:\fakepath\main_koveshnikov.py'
    print(f'Название загруженного файла указано верно {file_name_verification_text}')

def test_clickable_buttons(browser):
    browser.get('https://demoqa.com/dynamic-properties')
    # pyautogui.hotkey('win', 'up')
    sleep(6)
    enable_button = browser.find_element(By.XPATH, '//button[text()="Will enable 5 seconds"]')
    enable_button.click()
    sleep(3)
    visible_button = browser.find_element(By.XPATH, '//button[text()="Visible After 5 Seconds"]')
    visible_button.click()

def test_waiting_for_element(browser):
    browser.get('https://demoqa.com/dynamic-properties')
    wait = WebDriverWait(browser, timeout=6, poll_frequency=2.5)
    element = wait.until(
        EC.visibility_of_element_located((By.ID , 'enableAfter')))
    print(f'Элемент обнаружен')

def test_adding_user(browser):
    browser.get('https://demoqa.com/webtables')
    add_button = browser.find_element(By.ID, 'addNewRecordButton')
    add_button.click()
    firstname_form = browser.find_element(By.ID, 'firstName')
    firstname_form.send_keys('Arnold')
    lastname_form = browser.find_element(By.ID, 'lastName')
    lastname_form.send_keys('Schwarzenegger')
    email_form = browser.find_element(By.ID, 'userEmail')
    email_form.send_keys('arnold@schwarzenegger.com')
    age_form = browser.find_element(By.ID, 'age')
    age_form.send_keys('74')
    salary_form = browser.find_element(By.ID, 'salary')
    salary_form.send_keys('20000')
    department_form = browser.find_element(By.ID, 'department')
    department_form.send_keys('Marketing')
    # Отправим запрос
    submit_button = browser.find_element(By.ID, 'submit')
    submit_button.location_once_scrolled_into_view
    submit_button.click()

    result1 = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[1]')
    print(f'Вывожу то, что у меня в переменной result: {result1}')
    result1_text = result1.text
    print(f'Вывожу то, что у меня в переменной result_text: {result1_text}')
    assert result1_text == 'Arnold'

    result2 = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[2]')
    print(f'Вывожу то, что у меня в переменной result: {result2}')
    result2_text = result2.text
    print(f'Вывожу то, что у меня в переменной result_text: {result2_text}')
    assert result2_text == 'Schwarzenegger'

    result3 = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[3]')
    print(f'Вывожу то, что у меня в переменной result: {result3}')
    result3_text = result3.text
    print(f'Вывожу то, что у меня в переменной result_text: {result3_text}')
    assert result3_text == '74'

    result4 = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[4]')
    print(f'Вывожу то, что у меня в переменной result: {result4}')
    result4_text = result4.text
    print(f'Вывожу то, что у меня в переменной result_text: {result4_text}')
    assert result4_text == 'arnold@schwarzenegger.com'

    result5 = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[5]')
    print(f'Вывожу то, что у меня в переменной result: {result5}')
    result5_text = result5.text
    print(f'Вывожу то, что у меня в переменной result_text: {result5_text}')
    assert result5_text == '20000'

    result6 = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[6]')
    print(f'Вывожу то, что у меня в переменной result: {result6}')
    result6_text = result6.text
    print(f'Вывожу то, что у меня в переменной result_text: {result6_text}')
    assert result6_text == 'Marketing'
    sleep(3)

def test_edit_user(browser):
    browser.get('https://demoqa.com/webtables')
    add_button = browser.find_element(By.ID, 'addNewRecordButton')
    add_button.click()
    firstname_form = browser.find_element(By.ID, 'firstName')
    firstname_form.send_keys('Arnold')
    lastname_form = browser.find_element(By.ID, 'lastName')
    lastname_form.send_keys('Schwarzenegger')
    email_form = browser.find_element(By.ID, 'userEmail')
    email_form.send_keys('arnold@schwarzenegger.com')
    age_form = browser.find_element(By.ID, 'age')
    age_form.send_keys('74')
    salary_form = browser.find_element(By.ID, 'salary')
    salary_form.send_keys('20000')
    department_form = browser.find_element(By.ID, 'department')
    department_form.send_keys('Marketing')
    # Отправим запрос
    submit_button = browser.find_element(By.ID, 'submit')
    submit_button.location_once_scrolled_into_view
    submit_button.click()

    result1 = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[1]')
    print(f'Вывожу то, что у меня в переменной result: {result1}')
    result1_text = result1.text
    print(f'Вывожу то, что у меня в переменной result_text: {result1_text}')
    assert result1_text == 'Arnold'

    result2 = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[2]')
    print(f'Вывожу то, что у меня в переменной result: {result2}')
    result2_text = result2.text
    print(f'Вывожу то, что у меня в переменной result_text: {result2_text}')
    assert result2_text == 'Schwarzenegger'

    result3 = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[3]')
    print(f'Вывожу то, что у меня в переменной result: {result3}')
    result3_text = result3.text
    print(f'Вывожу то, что у меня в переменной result_text: {result3_text}')
    assert result3_text == '74'

    result4 = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[4]')
    print(f'Вывожу то, что у меня в переменной result: {result4}')
    result4_text = result4.text
    print(f'Вывожу то, что у меня в переменной result_text: {result4_text}')
    assert result4_text == 'arnold@schwarzenegger.com'

    result5 = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[5]')
    print(f'Вывожу то, что у меня в переменной result: {result5}')
    result5_text = result5.text
    print(f'Вывожу то, что у меня в переменной result_text: {result5_text}')
    assert result5_text == '20000'

    result6 = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[6]')
    print(f'Вывожу то, что у меня в переменной result: {result6}')
    result6_text = result6.text
    print(f'Вывожу то, что у меня в переменной result_text: {result6_text}')
    assert result6_text == 'Marketing'
    sleep(3)
    edit = browser.find_element(By.ID, 'edit-record-4')
    edit.click()
    edit_firstname = browser.find_element(By.ID, 'firstName')
    edit_firstname.click()
    sleep(4)
    pyautogui.hotkey('ctrl', 'a')
    sleep(3)
    pyautogui.press('backspace')
    edit_firstname.send_keys('SuperArnold')
    submit_btn2 = browser.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]/form/div[7]/div/button')
    submit_btn2.click()

    edit_verification = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[1]')
    print(f'Вывожу то, что у меня в переменной result: {edit_verification}')
    edit_verification = edit_verification.text
    print(f'Вывожу то, что у меня в переменной result_text: {edit_verification}')
    assert edit_verification == 'SuperArnold'

def test_search_box(browser):
    searchbox = browser.find_element(By.ID, 'searchBox')
    searchbox.send_keys('SuperArnold')

    search_verification = browser.find_element(By.XPATH, '//div[text()="SuperArnold"]')
    print(f'Вывожу то, что у меня в переменной result: {search_verification}')
    search_verification = search_verification.text
    print(f'Вывожу то, что у меня в переменной result_text: {search_verification}')
    assert search_verification == 'SuperArnold'

def test_deleting_user(browser):
    # Первый способ удаления
    browser.get('https://demoqa.com/webtables')
    delete_button = browser.find_element(By.ID, 'delete-record-3')
    delete_button.click()
    try:
     delete_verification = browser.find_element(By.XPATH, '//div[text()="Kierra"]')
     delete_verification_text = delete_verification.text
     print("Element exist -")
    except NoSuchElementException: print("Element does not exist")

def generate_user(browser):
    # Выведем данные, которые будем использовать для заполнения таблицы
    # Имя
    first_name = ['Rachel', 'Amanda', 'Amber', 'John', 'Nikolai', 'Max', 'Rob', 'Ricky', 'Chris', 'Keisha', 'Dmitri', 'Alexander', 'Dennis', 'Lebron', 'Brandon', 'Juan', 'Alex', 'Oleksandr', 'Tasha', 'Tatiana', 'Olivia', 'Curtis', 'Emma', 'Ava', 'Charlotte', 'Elijah','Mary', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Jennifer', 'Maria', 'Susan', 'Margaret', 'Dorothy', 'Lisa', 'Nancy', 'Karen', 'Betty', 'Sharon', 'Carol', 'Sandra', 'Ruth', 'Michelle', 'Angela', 'Melissa', 'Virginia']
    # Фамилия
    last_name = ['Clamps', 'Nunes', 'Rex', 'Doe', 'Vachovski', 'Garcia', 'Font', 'Rubio', 'Tucker', 'Green', 'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Davis', 'Miller', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson', 'White', 'Curry', 'Harris', 'Leonard', 'Sanchez', 'Clark', 'Lewis', 'Robinson', 'Walker', 'Young', 'Allen', 'King', 'Wright', 'Scott', 'Torres']
    # Почта
    email = ['ro@ro.com', 'ta@cos.com', 'com@misar.com', 'ro@pz.com', 'true@crime.com', 'never@surrender.com',
             'heavy@meansreliable.com', 'bas@sketball.com', 'gor@ra.com', 'chance@gmail.com', 'fault@gmail.com', 'rickyrock@outlook.com', 'rpp@outlook.com', 'shiftforever@mail.ru', 'shift2022@gmail.com', 'shiftvsegda@yandex.ru', 'cftvpered@gmail.com', 'teethtooth@miller.com', 'feetihave@gmail.com', 'handsihave@gmail.com', 'headihave@gmail.com', 'earsihave@gmail.com', 'fingersihave@gmail.com', 'scissorsihave@mail.ru', 'eyesihave@gmail.com', 'eyelids@gmail.com', 'drum@mail.ru', 'pocketsempty@gmail.com', 'needinsurance@gmail.com', 'damnitsbrian@gmail.com', 'quepasohota@gmail.com', 'dominick@gmail.com', 'tobeoornottobe@outlook.com', 'healthynot@outlook.com', 'believeachievefail@outlook.com', 'bombaster@mail.ru', 'shipychka@mail.ru', 'scramble@book.com', 'reeadit@gmail.com', 'rememberforget@gmail.com', 'roundone@gmail.com', 'roundtwo@gmail.com']
    # Возраст
    age_random = random.randint(18, 75)
    # Заработная плата
    salary_random = random.randint(2000, 20000)
    # Отдел
    department = ['Insurance', 'Compliance', 'Legal', 'Marketing']
    browser.get('https://demoqa.com/webtables')
    pyautogui.hotkey('win', 'up')
    add_button = browser.find_element(By.ID, 'addNewRecordButton')
    add_button.click()
    first_name_form = browser.find_element(By.ID, 'firstName')
    first_name_random = random.choices(first_name)
    first_name_form.send_keys(first_name_random)
    last_name_form = browser.find_element(By.ID, 'lastName')
    last_name_random = random.choices(last_name)
    last_name_form.send_keys(last_name_random)
    email_form = browser.find_element(By.ID, 'userEmail')
    email_random = random.choices(email)
    email_form.send_keys(email_random)
    age_form = browser.find_element(By.ID, 'age')
    age_form.send_keys(age_random)
    salary_form = browser.find_element(By.ID, 'salary')
    salary_form.send_keys(salary_random)
    department_form = browser.find_element(By.ID, 'department')
    department_random = random.choices(department)
    department_form.send_keys(department_random)
    submit_button = browser.find_element(By.ID, 'submit')
    submit_button.location_once_scrolled_into_view
    submit_button.click()

def adding_10_users(browser):
    # Выведем данные, которые будем использовать для заполнения таблицы
    # Имя
        first_name = ['Rachel', 'Amanda', 'Amber', 'John', 'Nikolai', 'Max', 'Rob', 'Ricky', 'Chris', 'Keisha',
                      'Dmitri',
                      'Alexander', 'Dennis', 'Lebron', 'Brandon', 'Juan', 'Alex', 'Oleksandr', 'Tasha', 'Tatiana',
                      'Olivia',
                      'Curtis', 'Emma', 'Ava', 'Charlotte', 'Elijah', 'Mary', 'Patricia', 'Linda', 'Barbara',
                      'Elizabeth',
                      'Jennifer', 'Maria', 'Susan', 'Margaret', 'Dorothy', 'Lisa', 'Nancy', 'Karen', 'Betty', 'Sharon',
                      'Carol', 'Sandra', 'Ruth', 'Michelle', 'Angela', 'Melissa', 'Virginia']
        # Фамилия
        last_name = ['Clamps', 'Nunes', 'Rex', 'Doe', 'Vachovski', 'Garcia', 'Font', 'Rubio', 'Tucker', 'Green',
                     'Smith',
                     'Johnson', 'Williams', 'Brown', 'Jones', 'Davis', 'Miller', 'Rodriguez', 'Martinez', 'Hernandez',
                     'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee',
                     'Perez', 'Thompson', 'White', 'Curry', 'Harris', 'Leonard', 'Sanchez', 'Clark', 'Lewis',
                     'Robinson',
                     'Walker', 'Young', 'Allen', 'King', 'Wright', 'Scott', 'Torres']
        # Почта
        email = ['ro@ro.com', 'ta@cos.com', 'com@misar.com', 'ro@pz.com', 'true@crime.com', 'never@surrender.com',
                 'heavy@meansreliable.com', 'bas@sketball.com', 'gor@ra.com', 'chance@gmail.com', 'fault@gmail.com',
                 'rickyrock@outlook.com', 'rpp@outlook.com', 'shiftforever@mail.ru', 'shift2022@gmail.com',
                 'shiftvsegda@yandex.ru', 'cftvpered@gmail.com', 'teethtooth@miller.com', 'feetihave@gmail.com',
                 'handsihave@gmail.com', 'headihave@gmail.com', 'earsihave@gmail.com', 'fingersihave@gmail.com',
                 'scissorsihave@mail.ru', 'eyesihave@gmail.com', 'eyelids@gmail.com', 'drum@mail.ru',
                 'pocketsempty@gmail.com', 'needinsurance@gmail.com', 'damnitsbrian@gmail.com', 'quepasohota@gmail.com',
                 'dominick@gmail.com', 'tobeoornottobe@outlook.com', 'healthynot@outlook.com',
                 'believeachievefail@outlook.com', 'bombaster@mail.ru', 'shipychka@mail.ru', 'scramble@book.com',
                 'reeadit@gmail.com', 'rememberforget@gmail.com', 'roundone@gmail.com', 'roundtwo@gmail.com']
        # Возраст
        age_random = random.randint(18, 75)
        # Заработная плата
        salary_random = random.randint(2000, 20000)
        # Отдел
        department = ['Insurance', 'Compliance', 'Legal', 'Marketing']

        browser.get('https://demoqa.com/webtables')
        pyautogui.hotkey('win', 'up')
        # Проверим текущее количество страниц
        page_number1 = browser.find_element(By.XPATH, "//span[@class='-totalPages' and text()='1']")
        page_number1_text = page_number1.text
        print(f'Количество страниц: {page_number1_text}')
        # Добавляем юзеров
        add_button = browser.find_element(By.ID, 'addNewRecordButton')
        add_button.click()
        first_name_form = browser.find_element(By.ID, 'firstName')
        first_name_random = random.choices(first_name)
        first_name_form.send_keys(first_name_random)
        last_name_form = browser.find_element(By.ID, 'lastName')
        last_name_random = random.choices(last_name)
        last_name_form.send_keys(last_name_random)
        email_form = browser.find_element(By.ID, 'userEmail')
        email_random = random.choices(email)
        email_form.send_keys(email_random)
        age_form = browser.find_element(By.ID, 'age')
        age_form.send_keys(random.randint(18, 75))
        salary_form = browser.find_element(By.ID, 'salary')
        salary_form.send_keys(random.randint(2000, 20000))
        department_form = browser.find_element(By.ID, 'department')
        department_random = random.choices(department)
        department_form.send_keys(department_random)
        submit_button = browser.find_element(By.ID, 'submit')
        submit_button.location_once_scrolled_into_view
        submit_button.click()

        add_button = browser.find_element(By.ID, 'addNewRecordButton')
        add_button.click()
        first_name_form = browser.find_element(By.ID, 'firstName')
        first_name_random = random.choices(first_name)
        first_name_form.send_keys(first_name_random)
        last_name_form = browser.find_element(By.ID, 'lastName')
        last_name_random = random.choices(last_name)
        last_name_form.send_keys(last_name_random)
        email_form = browser.find_element(By.ID, 'userEmail')
        email_random = random.choices(email)
        email_form.send_keys(email_random)
        age_form = browser.find_element(By.ID, 'age')
        age_form.send_keys(random.randint(18, 75))
        salary_form = browser.find_element(By.ID, 'salary')
        salary_form.send_keys(random.randint(2000, 20000))
        department_form = browser.find_element(By.ID, 'department')
        department_random = random.choices(department)
        department_form.send_keys(department_random)
        submit_button = browser.find_element(By.ID, 'submit')
        submit_button.location_once_scrolled_into_view
        submit_button.click()

        add_button = browser.find_element(By.ID, 'addNewRecordButton')
        add_button.click()
        first_name_form = browser.find_element(By.ID, 'firstName')
        first_name_random = random.choices(first_name)
        first_name_form.send_keys(first_name_random)
        last_name_form = browser.find_element(By.ID, 'lastName')
        last_name_random = random.choices(last_name)
        last_name_form.send_keys(last_name_random)
        email_form = browser.find_element(By.ID, 'userEmail')
        email_random = random.choices(email)
        email_form.send_keys(email_random)
        age_form = browser.find_element(By.ID, 'age')
        age_form.send_keys(random.randint(18, 75))
        salary_form = browser.find_element(By.ID, 'salary')
        salary_form.send_keys(random.randint(2000, 20000))
        department_form = browser.find_element(By.ID, 'department')
        department_random = random.choices(department)
        department_form.send_keys(department_random)
        submit_button = browser.find_element(By.ID, 'submit')
        submit_button.location_once_scrolled_into_view
        submit_button.click()

        add_button = browser.find_element(By.ID, 'addNewRecordButton')
        add_button.click()
        first_name_form = browser.find_element(By.ID, 'firstName')
        first_name_random = random.choices(first_name)
        first_name_form.send_keys(first_name_random)
        last_name_form = browser.find_element(By.ID, 'lastName')
        last_name_random = random.choices(last_name)
        last_name_form.send_keys(last_name_random)
        email_form = browser.find_element(By.ID, 'userEmail')
        email_random = random.choices(email)
        email_form.send_keys(email_random)
        age_form = browser.find_element(By.ID, 'age')
        age_form.send_keys(random.randint(18, 75))
        salary_form = browser.find_element(By.ID, 'salary')
        salary_form.send_keys(random.randint(2000, 20000))
        department_form = browser.find_element(By.ID, 'department')
        department_random = random.choices(department)
        department_form.send_keys(department_random)
        submit_button = browser.find_element(By.ID, 'submit')
        submit_button.location_once_scrolled_into_view
        submit_button.click()

        add_button = browser.find_element(By.ID, 'addNewRecordButton')
        add_button.click()
        first_name_form = browser.find_element(By.ID, 'firstName')
        first_name_random = random.choices(first_name)
        first_name_form.send_keys(first_name_random)
        last_name_form = browser.find_element(By.ID, 'lastName')
        last_name_random = random.choices(last_name)
        last_name_form.send_keys(last_name_random)
        email_form = browser.find_element(By.ID, 'userEmail')
        email_random = random.choices(email)
        email_form.send_keys(email_random)
        age_form = browser.find_element(By.ID, 'age')
        age_form.send_keys(random.randint(18, 75))
        salary_form = browser.find_element(By.ID, 'salary')
        salary_form.send_keys(random.randint(2000, 20000))
        department_form = browser.find_element(By.ID, 'department')
        department_random = random.choices(department)
        department_form.send_keys(department_random)
        submit_button = browser.find_element(By.ID, 'submit')
        submit_button.location_once_scrolled_into_view
        submit_button.click()

        add_button = browser.find_element(By.ID, 'addNewRecordButton')
        add_button.click()
        first_name_form = browser.find_element(By.ID, 'firstName')
        first_name_random = random.choices(first_name)
        first_name_form.send_keys(first_name_random)
        last_name_form = browser.find_element(By.ID, 'lastName')
        last_name_random = random.choices(last_name)
        last_name_form.send_keys(last_name_random)
        email_form = browser.find_element(By.ID, 'userEmail')
        email_random = random.choices(email)
        email_form.send_keys(email_random)
        age_form = browser.find_element(By.ID, 'age')
        age_form.send_keys(random.randint(18, 75))
        salary_form = browser.find_element(By.ID, 'salary')
        salary_form.send_keys(random.randint(2000, 20000))
        department_form = browser.find_element(By.ID, 'department')
        department_random = random.choices(department)
        department_form.send_keys(department_random)
        submit_button = browser.find_element(By.ID, 'submit')
        submit_button.location_once_scrolled_into_view
        submit_button.click()

        add_button = browser.find_element(By.ID, 'addNewRecordButton')
        add_button.click()
        first_name_form = browser.find_element(By.ID, 'firstName')
        first_name_random = random.choices(first_name)
        first_name_form.send_keys(first_name_random)
        last_name_form = browser.find_element(By.ID, 'lastName')
        last_name_random = random.choices(last_name)
        last_name_form.send_keys(last_name_random)
        email_form = browser.find_element(By.ID, 'userEmail')
        email_random = random.choices(email)
        email_form.send_keys(email_random)
        age_form = browser.find_element(By.ID, 'age')
        age_form.send_keys(random.randint(18, 75))
        salary_form = browser.find_element(By.ID, 'salary')
        salary_form.send_keys(random.randint(2000, 20000))
        department_form = browser.find_element(By.ID, 'department')
        department_random = random.choices(department)
        department_form.send_keys(department_random)
        submit_button = browser.find_element(By.ID, 'submit')
        submit_button.location_once_scrolled_into_view
        submit_button.click()

        add_button = browser.find_element(By.ID, 'addNewRecordButton')
        add_button.click()
        first_name_form = browser.find_element(By.ID, 'firstName')
        first_name_random = random.choices(first_name)
        first_name_form.send_keys(first_name_random)
        last_name_form = browser.find_element(By.ID, 'lastName')
        last_name_random = random.choices(last_name)
        last_name_form.send_keys(last_name_random)
        email_form = browser.find_element(By.ID, 'userEmail')
        email_random = random.choices(email)
        email_form.send_keys(email_random)
        age_form = browser.find_element(By.ID, 'age')
        age_form.send_keys(random.randint(18, 75))
        salary_form = browser.find_element(By.ID, 'salary')
        salary_form.send_keys(random.randint(2000, 20000))
        department_form = browser.find_element(By.ID, 'department')
        department_random = random.choices(department)
        department_form.send_keys(department_random)
        submit_button = browser.find_element(By.ID, 'submit')
        submit_button.location_once_scrolled_into_view
        submit_button.click()

        add_button = browser.find_element(By.ID, 'addNewRecordButton')
        add_button.click()
        first_name_form = browser.find_element(By.ID, 'firstName')
        first_name_random = random.choices(first_name)
        first_name_form.send_keys(first_name_random)
        last_name_form = browser.find_element(By.ID, 'lastName')
        last_name_random = random.choices(last_name)
        last_name_form.send_keys(last_name_random)
        email_form = browser.find_element(By.ID, 'userEmail')
        email_random = random.choices(email)
        email_form.send_keys(email_random)
        age_form = browser.find_element(By.ID, 'age')
        age_form.send_keys(random.randint(18, 75))
        salary_form = browser.find_element(By.ID, 'salary')
        salary_form.send_keys(random.randint(2000, 20000))
        department_form = browser.find_element(By.ID, 'department')
        department_random = random.choices(department)
        department_form.send_keys(department_random)
        submit_button = browser.find_element(By.ID, 'submit')
        submit_button.location_once_scrolled_into_view
        submit_button.click()

        add_button = browser.find_element(By.ID, 'addNewRecordButton')
        add_button.click()
        first_name_form = browser.find_element(By.ID, 'firstName')
        first_name_random = random.choices(first_name)
        first_name_form.send_keys(first_name_random)
        last_name_form = browser.find_element(By.ID, 'lastName')
        last_name_random = random.choices(last_name)
        last_name_form.send_keys(last_name_random)
        email_form = browser.find_element(By.ID, 'userEmail')
        email_random = random.choices(email)
        email_form.send_keys(email_random)
        age_form = browser.find_element(By.ID, 'age')
        age_form.send_keys(random.randint(18, 75))
        salary_form = browser.find_element(By.ID, 'salary')
        salary_form.send_keys(random.randint(2000, 20000))
        department_form = browser.find_element(By.ID, 'department')
        department_random = random.choices(department)
        department_form.send_keys(department_random)
        submit_button = browser.find_element(By.ID, 'submit')
        submit_button.location_once_scrolled_into_view
        submit_button.click()

        add_button = browser.find_element(By.ID, 'addNewRecordButton')
        add_button.click()
        first_name_form = browser.find_element(By.ID, 'firstName')
        first_name_random = random.choices(first_name)
        first_name_form.send_keys(first_name_random)
        last_name_form = browser.find_element(By.ID, 'lastName')
        last_name_random = random.choices(last_name)
        last_name_form.send_keys(last_name_random)
        email_form = browser.find_element(By.ID, 'userEmail')
        email_random = random.choices(email)
        email_form.send_keys(email_random)
        age_form = browser.find_element(By.ID, 'age')
        age_form.send_keys(random.randint(18, 75))
        salary_form = browser.find_element(By.ID, 'salary')
        salary_form.send_keys(random.randint(2000, 20000))
        department_form = browser.find_element(By.ID, 'department')
        department_random = random.choices(department)
        department_form.send_keys(department_random)
        submit_button = browser.find_element(By.ID, 'submit')
        submit_button.location_once_scrolled_into_view
        submit_button.click()

        # Убедимся, что количество страниц увеличилось
        page_number2 = browser.find_element(By.XPATH, "//span[@class='-totalPages' and text()='2']")
        page_number2_text = page_number2.text
        print(f'Количество страниц: {page_number2_text}')

        # Убедимся, что номер текущей страницы - 1
        current_page = browser.find_element(By.XPATH, "//input[@value='1']")
        try:
            current_page = browser.find_element(By.XPATH, "//input[@value='1']")
            current_page_text = current_page.text
            print("Страница 1 -")
        except NoSuchElementException:
            print("Element does not exist")


def test_new_tab(browser):
    browser.get('https://google.com/')
    browser.execute_script("window.open('https://demoqa.com/browser-windows');")
    browser.switch_to.window(browser.window_handles[1])
    new_tab = browser.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/button[1]')
    new_tab.click()
    browser.switch_to.window(browser.window_handles[2])
    sleep(3)
    new_tab_verification = browser.find_element(By.ID, 'sampleHeading')
    new_tab_verification_text = new_tab_verification.text
    assert new_tab_verification_text == 'This is a sample page'
    print(f' Открыта вкладка New Tab: {new_tab_verification_text}')
    browser.close()
    browser.switch_to.window(browser.window_handles[1])

    # Первый способ убедиться, что открыта прошлая вкладка
    get_title2 = browser.title
    print(f'Открыта прошлая вкладка: {get_title2}')

    assert get_title2 == 'ToolsQA'
    # Второй способ убедиться, что открыта прошлая вкладка
    previous_tab_verification = browser.find_element(By.XPATH, "//div[@class='main-header' and text()='Browser Windows']")
    previous_tab_verification_text = previous_tab_verification.text
    print(f'Открыта прошлая вкладка: {previous_tab_verification}')

    assert previous_tab_verification_text == 'Browser Windows'
    print(f'Открытая прошлая вкладка: {previous_tab_verification_text}')

    # Выводим список активных кнопок. Первый способ
    enabled_btns = browser.find_elements(By.TAG_NAME, 'button')
    for value in enabled_btns:
        if value.is_enabled() and value.is_displayed():
         print(value.text)

    # Выводим список активных кнопок. Второй способ
    new_tab_btn = browser.find_element(By.XPATH, '//button[text()="New Tab"]')
    if new_tab_btn.is_enabled() and new_tab_btn.is_displayed():
        print(f'The new tab button is enabled and displayed')
    else:
        print('Failed')
    new_tab_btn_text = new_tab_btn.text
    print(f' Название активной кнопки: {new_tab_btn_text}')

    new_window_btn = browser.find_element(By.XPATH, '//button[text()="New Window"]')
    if new_window_btn.is_enabled() and new_window_btn.is_displayed():
        print(f'The new window button is enabled and displayed')
    else:
        print('Failed')
    new_window_btn_text = new_window_btn.text
    print(f' Название активной кнопки: {new_window_btn_text}')

    new_window_msg_btn = browser.find_element(By.XPATH, '//button[text()="New Window Message"]')
    if new_window_msg_btn.is_enabled() and new_window_msg_btn.is_displayed():
        print(f'The new window message button is enabled and displayed')
    else:
        print('Failed')
    new_window_msg_btn_text = new_window_msg_btn.text
    print(f' Название активной кнопки: {new_window_msg_btn_text}')


def test_alert_buttons(browser):
    browser.get('https://demoqa.com/alerts')
    click_button1 = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/button')
    click_button1.click()
    sleep(3)
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    assert alert_text == 'You clicked a button'
    alert.accept()

    click_button2 = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/button')
    click_button2.click()
    alert2 = WebDriverWait(browser, 10).until(EC.alert_is_present())
    alert2_text = alert2.text
    print(alert2_text)
    assert alert2_text == 'This alert appeared after 5 seconds'
    alert2.accept()

    click_button3 = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/button')
    click_button3.click()
    alert3 = WebDriverWait(browser, 10).until(EC.alert_is_present())
    alert3_text = alert3.text
    print(alert3_text)
    assert alert3_text == 'Do you confirm action?'
    alert3.accept()

    click_button4 = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[4]/div[2]/button')
    click_button4.click()
    alert4 = WebDriverWait(browser, 10).until(EC.alert_is_present())
    alert4_text = alert4.text
    print(alert4_text)
    assert alert4_text == 'Please enter your name'
    alert4.accept()
    my_browser.quit()

my_browser = init_browser()

test_button(my_browser)
test_dynamic_btn(my_browser)
test_getting_to_textbox(my_browser)
test_uploading_files(my_browser)
test_clickable_buttons(my_browser)
test_waiting_for_element(my_browser)
test_adding_user(my_browser)
test_edit_user(my_browser)
test_search_box(my_browser)
test_deleting_user(my_browser)
generate_user(my_browser)
adding_10_users(my_browser)
test_new_tab(my_browser)
test_alert_buttons(my_browser)
my_browser.close()
