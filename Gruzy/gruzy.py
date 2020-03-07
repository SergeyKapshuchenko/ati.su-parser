from selenium import webdriver
import time
from datetime import date
import csv

months = ['', 'янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
current_month = "доб " + date.today().strftime("%d") + " " + months[int(date.today().strftime("%m"))]

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_setting_values': {
    'plugins': 2, 'popups': 2, 'geolocation': 2,
    'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2,
    'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
    'media_stream_mic': 2, 'media_stream_camera': 2,
    'protocol_handlers': 2,
    'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
    'push_messaging': 2, 'ssl_cert_decisions': 2,
    'metro_switch_to_desktop': 2,
    'protected_media_identifier': 2, 'app_banner': 2,
    'site_engagement': 2,
    'durable_storage': 2}}
options.add_experimental_option('prefs', prefs)
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")

driver = webdriver.Chrome('/Users/sergeykapshuchenko/Downloads/chromedriver', options=options)

center_names = [
    "Белгородская область", "Брянская область",
    "Ивановская область",
    "Калужская область", "Костромская область", "Смоленская область", "Орловская область",
    "Ярославская область", "Липецкая область", "Владимирская область", "Воронежская область",
    "Рязанская область", "Тамбовская область", "Тверская область", "Тульская область", "Курская область",
    "Московская область", "Москва (регион)", "Ленинградская область", "Санкт-Петербург (регион)",
    "Пермский край", "Нижегородская область", "Оренбургская область", "Саратовская область",
    "Татарстан республика", "Кировская область", "Пензенская область", "Самарская область",
    "Ульяновская область", "Марий Эл республика", "Башкортостан республика", "Мордовия республика",
    "Удмуртская Республика", "Чувашия республика", "Волгоградская область", "Краснодарский край",
    "Калмыкия республика", "Ростовская область", "Астраханская область", "Адыгея республика",
    "Крым республика",
]

center_links = [
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22to%22:%22Белгородская%20обл.,%20РФ%22,%22toGeo_tmp%22:%221_64%22,%22toGeo%22:%221_64%22,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22to%22:%22Брянская%20обл.,%20РФ%22,%22toGeo_tmp%22:%221_65%22,%22toGeo%22:%221_65%22,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22to%22:%22Ивановская%20обл.,%20РФ%22,%22toGeo%22:%221_69%22,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22to%22:%22Калужская%20обл.,%20РФ%22,%22toGeo_tmp%22:%221_36%22,%22toGeo%22:%221_36%22,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22to%22:%22Костромская%20обл.,%20РФ%22,%22toGeo_tmp%22:%221_39%22,%22toGeo%22:%221_39%22,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22to%22:%22Смоленская%20обл.,%20РФ%22,%22toGeo_tmp%22:%221_13%22,%22toGeo%22:%221_13%22,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22to%22:%22Орловская%20обл.,%20РФ%22,%22toGeo_tmp%22:%221_83%22,%22toGeo%22:%221_83%22,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22to%22:%22Ярославская%20обл.,%20РФ%22,%22toGeo_tmp%22:%221_88%22,%22toGeo%22:%221_88%22,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22to%22:%22Липецкая%20обл.,%20РФ%22,%22toGeo_tmp%22:%221_75%22,%22toGeo%22:%221_75%22,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22to%22:%22Владимирская%20обл.,%20РФ%22,%22toGeo_tmp%22:%221_66%22,%22toGeo%22:%221_66%22,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22to%22:%22Воронежская%20обл.,%20РФ%22,%22toGeo_tmp%22:%221_26%22,%22toGeo%22:%221_26%22,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22to%22:%22Рязанская%20обл.,%20РФ%22,%22toGeo_tmp%22:%221_8%22,%22toGeo%22:%221_8%22,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22to%22:%22Тамбовская%20обл.,%20РФ%22,%22toGeo_tmp%22:%221_19%22,%22toGeo%22:%221_19%22,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22,%22to%22:%22Тверская%20обл.,%20РФ%22,%22toGeo_tmp%22:%221_121%22,%22toGeo%22:%221_22%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22,%22to%22:%22Тульская%20обл.,%20РФ%22,%22toGeo_tmp%22:%221_24%22,%22toGeo%22:%221_24%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22,%22to%22:%22Курская%20обл.,%20РФ%22,%22toGeo%22:%221_74%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22,%22to%22:%22Московская%20обл.,%20РФ%22,%22toGeo_tmp%22:%221_1%22,%22toGeo%22:%221_1%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22,%22to%22:%22Москва%20(регион),%20РФ%22,%22toGeo_tmp%22:%221_151%22,%22toGeo%22:%221_151%22%7D',

    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22,%22to%22:%22Ленинградская%20обл.,%20РФ%22,%22toGeo_tmp%22:%222_2453%22,%22toGeo%22:%221_2%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22,%22to%22:%22Санкт-Петербург%20(регион),%20РФ%22,%22toGeo_tmp%22:%221_153%22,%22toGeo%22:%221_153%22%7D',

    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22,%22to%22:%22Пермский%20край,%20РФ%22,%22toGeo_tmp%22:%221_3%22,%22toGeo%22:%221_3%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22,%22to%22:%22Нижегородская%20обл.,%20РФ%22,%22toGeo_tmp%22:%220_26%22,%22toGeo%22:%221_78%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22,%22to%22:%22Оренбургская%20обл.,%20РФ%22,%22toGeo_tmp%22:%221_82%22,%22toGeo%22:%221_82%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22,%22to%22:%22Саратовская%20обл.,%20РФ%22,%22toGeo_tmp%22:%221_11%22,%22toGeo%22:%221_11%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22,%22to%22:%22Татарстан%20республика,%20РФ%22,%22toGeo%22:%221_54%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22,%22to%22:%22Кировская%20обл.,%20РФ%22,%22toGeo_tmp%22:%221_38%22,%22toGeo%22:%221_38%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22,%22to%22:%22Пензенская%20обл.,%20РФ%22,%22toGeo_tmp%22:%221_445%22,%22toGeo%22:%221_84%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22,%22to%22:%22Самарская%20обл.,%20РФ%22,%22toGeo_tmp%22:%221_9%22,%22toGeo%22:%221_9%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22,%22to%22:%22Ульяновская%20обл.,%20РФ%22,%22toGeo_tmp%22:%221_25%22,%22toGeo%22:%221_25%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22,%22to%22:%22Марий%20Эл%20республика,%20РФ%22,%22toGeo_tmp%22:%222_17353%22,%22toGeo%22:%221_51%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22,%22to%22:%22Башкортостан%20республика,%20РФ%22,%22toGeo_tmp%22:%221_43%22,%22toGeo%22:%221_43%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22,%22to%22:%22Мордовия%20республика,%20РФ%22,%22toGeo_tmp%22:%221_10%22,%22toGeo%22:%221_10%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22,%22to%22:%22Удмуртская%20Республика,%20РФ%22,%22toGeo_tmp%22:%221_56%22,%22toGeo%22:%221_56%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22,%22to%22:%22Чувашия%20республика,%20РФ%22,%22toGeo_tmp%22:%222_12037%22,%22toGeo%22:%221_59%22%7D',

    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22,%22to%22:%22Волгоградская%20обл.,%20РФ%22,%22toGeo_tmp%22:%221_67%22,%22toGeo%22:%221_67%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22,%22to%22:%22Краснодарский%20край,%20РФ%22,%22toGeo_tmp%22:%222_4203%22,%22toGeo%22:%221_40%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22,%22to%22:%22Калмыкия%20республика,%20РФ%22,%22toGeo_tmp%22:%221_49%22,%22toGeo%22:%221_49%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22,%22to%22:%22Ростовская%20обл.,%20РФ%22,%22toGeo_tmp%22:%221_7%22,%22toGeo%22:%221_7%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22,%22to%22:%22Астраханская%20обл.,%20РФ%22,%22toGeo%22:%221_63%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22,%22to%22:%22Адыгея%20республика,%20РФ%22,%22toGeo_tmp%22:%221_42%22,%22toGeo%22:%221_42%22%7D',
    'https://loads.ati.su/#?filter=%7B%22exactFromGeos%22:true,%22exactToGeos%22:true,%22from%22:%22Россия%22,%22fromGeo_tmp%22:%220_1%22,%22fromGeo%22:%220_1%22,%22to%22:%22Крым%20республика,%20РФ%22,%22toGeo_tmp%22:%221_54%22,%22toGeo%22:%221_131%22%7D'
]


def login_to(driver):
    login = "Ваши данные от аккаунта"
    password = "Ваши данные от аккаунта"

    driver.get("https://id.ati.su/login/?next=https%3A%2F%2Fati.su%2F")

    time.sleep(2)

    driver.find_element_by_id("login").send_keys(login)

    time.sleep(1)

    driver.find_element_by_id("password").send_keys(password)

    time.sleep(1)

    driver.find_element_by_id("action-login").click()

    time.sleep(40)

    print("Logged in DONE")


def single_url(url, link_):
    driver.get(url)

    time.sleep(10)
    try:
        number_of_page = int(driver.find_element_by_xpath("//li[@class='pagination-page pagination-last-page']").text)
    except Exception:
        number_of_page = 1

    counter = 1
    flag = True
    while counter <= number_of_page:

        if counter % 5 == 0:
            number_of_page = int(
                driver.find_element_by_xpath("//li[@class='pagination-page pagination-last-page']").text)
            print(number_of_page)

        if flag:
            single_parse(link_)

        try:
            driver.find_element_by_xpath("//i[@class='fa fa-chevron-right']").click()
            counter += 1
            flag = True
        except Exception:
            print("Next page error")
            flag = False


def single_parse(link_):
    time.sleep(1)
    data = []

    buttons = driver.find_elements_by_xpath("//a[@data-ng-click='vm.showPriorityInfo(e)']")
    for button in buttons:
        try:
            button.click()
            time.sleep(0.1)
        except Exception as e:
            print("button exc")

    oblast = center_names[link_ - 1]

    for i in range(1, 107):

        try:
            route = driver.find_element_by_xpath(
                f"(//div[@class='load-main-info-block'])[{i}]//div[@class='geo-col grid-column']").text
        except Exception as e:
            # print("No route", type(e))
            route = ""

        try:
            transport = driver.find_element_by_xpath(
                f"(//div[@class='load-row load-info'])[{i}]//div[@class='transport-col grid-column']").text
        except Exception as e:
            # print("No transport", type(e))
            transport = ""

        try:
            weight = driver.find_elements_by_xpath(
                f"(//div[@class='load-row load-info'])[{i}]//div[@class='load-weight-volume cell-header' or @class='load-cargo-type']")
            weight = ', '.join([i.text for i in weight if weight])
        except Exception as e:
            # print("No weight", type(e))
            weight = ""

        try:
            loading = driver.find_element_by_xpath(
                f"(//div[@class='load-main-info-block'])[{i}]//div[@class='loading-col grid-column']").text
        except Exception as e:
            # print("No loading", type(e))
            loading = ""

        try:
            unloading = driver.find_element_by_xpath(
                f"(//div[@class='load-main-info-block'])[1]//div[@class='unloading-col grid-column']").text
        except Exception as e:
            # print("No unloading", type(e))
            unloading = ""

        try:
            name = driver.find_element_by_xpath(
                f"(//div[@class='load-main-info-block'])[{i}]//a[@class='load-firm-name'][1]").text
        except Exception as e:
            # print("No name", type(e))
            name = ""

        try:
            added = driver.find_element_by_xpath(
                f"(//div[@class='load-additional-info-block normal'])[{i}]//span[@class='ng-scope']").text
            if ":" in added:
                added = current_month
            elif "Отпр" in added:
                added = ""
        except Exception as e:
            # print("No data", type(e))
            added = ""

        try:
            stavka = driver.find_element_by_xpath(f"(//div[@class='rate-col grid-paddings'])[{i}]").text
            if "Отправить предложение" in stavka:
                stavka = ' '.join([i for i in stavka.split()[:-2]])
        except Exception as e:
            # print("No stavka", type(e))
            stavka = ""

        try:
            contacts = driver.find_elements_by_xpath(
                f"(//div[@class='load-main-info-block'])[{i}]//span[@data-ng-repeat='p in c.phones' or @class='contactNameStatus']")
            contacts = ', '.join([contact.text for contact in contacts])
        except Exception as e:
            # print("No Contacts", type(e))
            contacts = ""

        data.append({
            'Область': oblast,
            'Направление': route,
            'Транспорт': transport,
            'Вес': weight,
            'Загрузка': loading,
            'Разгрузка': unloading,
            'Дата добавления': added,
            'Название компании': name,
            'Ставка': stavka,
            'Контакты': contacts
        })

    print("Page Done")

    with open(f"{link_}.csv", mode='a') as write_file:
        fieldnames = [
            'Область',
            'Направление',
            'Транспорт',
            'Вес',
            'Загрузка',
            'Разгрузка',
            'Дата добавления',
            'Название компании',
            'Ставка',
            'Контакты'
        ]
        writer = csv.DictWriter(write_file, delimiter=';', fieldnames=fieldnames)
        writer.writerows(data)


def crawler():
    # login_to(driver)
    link_ = 1
    for link in center_links:
        print(link_, link)
        single_url(link, link_)
        link_ += 1


crawler()
