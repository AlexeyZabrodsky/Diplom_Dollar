import time
import pytest_check as check
import allure

from diplom.pages.locators.header_page_locators import HeaderBtn
from diplom.pages.locators.futer_page_locators import FuterBtn
from diplom.pages.locators.сatalog_page_locators import CatalogBtn
from diplom.pages.locators.home_page_locators import HomeBtn
from diplom.conftest import web_browser


# <--------------------------------------------HEADER---------------------------------------------->
@allure.feature('Смоук тест')
@allure.story('Имитация скролла в низ экрана и нажатия кнопок Хедера')
def test_header_btn(web_browser):
    """ Убеждаемся, что ссылки/кнопки хедера
        кликабельные и переход на страницу корректный. """

    page = HeaderBtn(web_browser)

    with allure.step("Проверка кнопки 'О магазине'"):
        # elements = [('О магазине', page.button_o_magazine, 'https://www.dollar.by/about'),
        #             ('Доставка и оплата', page.button_dostavka_i_oplata, 'https://www.dollar.by/orders'),
        #             ('Гарантия', page.button_garantiya, 'https://www.dollar.by/garantiya'),
        #             ('Корзина:', page.button_korzina, 'https://www.dollar.by/shopcart'),
        #             ]
        #
        # for name, elem, url in elements:
        #     if check.equal(elem.get_text(), name):
        #         check.equal(elem.get_attribute('href'), url)
        #         elem.click()
        #         page1 = page.get_current_url()
        #         check.equal(page1, url)
        #         check.is_true(elem.wait_for_visibility())
        #         check.is_true(elem.wait_to_be_clickable())
        #
        if check.equal(page.button_o_magazine.get_text(), 'О магазине'):
            check.equal(page.button_o_magazine.get_attribute('href'),
                        'https://www.dollar.by/about')
            page.button_o_magazine.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/about')
            check.is_true(page.button_o_magazine.wait_for_visibility())
            check.is_true(page.button_o_magazine.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Доставка и оплата'"):
        if check.equal(page.button_dostavka_i_oplata.get_text(), 'Доставка и оплата'):
            check.equal(page.button_dostavka_i_oplata.get_attribute('href'),
                        'https://www.dollar.by/orders')
            page.button_dostavka_i_oplata.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/orders')
            check.is_true(page.button_dostavka_i_oplata.wait_for_visibility())
            check.is_true(page.button_dostavka_i_oplata.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Гарантия'"):
        if check.equal(page.button_garantiya.get_text(), 'Гарантия'):
            check.equal(page.button_garantiya.get_attribute('href'),
                        'https://www.dollar.by/garantiya')
            page.button_garantiya.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/garantiya')
            check.is_true(page.button_garantiya.wait_for_visibility())
            check.is_true(page.button_garantiya.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Корзина'"):
        if check.equal(page.button_korzina.get_text(), 'Корзина:'):
            check.equal(page.button_korzina.get_attribute('href'),
                        'https://www.dollar.by/shopcart')
            page.button_korzina.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/shopcart')
            check.is_true(page.button_korzina.wait_for_visibility())
            check.is_true(page.button_korzina.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Лого'"):
        if check.equal(page.button_logo.get_attribute('href'), 'https://www.dollar.by/'):
            page.button_logo.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/')
            check.is_true(page.button_logo.wait_for_visibility())
            check.is_true(page.button_logo.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Поиск'"):
        if check.equal(page.button_poisk.get_text(), 'Поиск'):
            page.button_poisk.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/search?q=')
            check.is_true(page.button_poisk.wait_for_visibility())
            check.is_true(page.button_poisk.wait_to_be_clickable())
            time.sleep(4)

    with allure.step("Проверка кнопки Header-mini 'Лого'"):
        page.execute_script("window.scrollTo(0, 200)")
        time.sleep(4)
        if check.equal(page.button_logo_mini.get_attribute('href'), 'https://www.dollar.by/'):
            check.is_true(page.button_logo_mini.wait_for_visibility())
            check.is_true(page.button_logo_mini.wait_to_be_clickable())
            page.button_logo_mini.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/')

    with allure.step("Проверка кнопки Header-mini 'Поиск'"):
        page.execute_script("window.scrollTo(0, 200)")
        if check.equal(page.button_poisk_mini.get_text(), 'Поиск'):
            check.is_true(page.button_poisk_mini.wait_for_visibility())
            check.is_true(page.button_poisk_mini.wait_to_be_clickable())
            page.button_poisk_mini.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/search?q=')

    with allure.step("Проверка кнопки Header-mini 'Корзина'"):
        page.execute_script("window.scrollTo(0, 200)")
        if check.equal(page.button_korzina_mini.get_attribute('href'),
                       'https://www.dollar.by/shopcart'):
            check.equal(page.button_korzina_mini.get_text(), 'Корзина:')
            check.is_true(page.button_korzina_mini.wait_for_visibility())
            check.is_true(page.button_korzina_mini.wait_to_be_clickable())
            page.button_korzina_mini.click(1)
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/shopcart')

    with allure.step("Проверка раскрывающего окна при наведении Header-mini "
                     "'Информация с номерами'"):
        page.execute_script("window.scrollTo(0, 200)")
        if check.is_true(page.button_info_mini.wait_for_visibility()):
            check.is_true(page.button_info_mini.wait_to_be_clickable())
            page.button_info_mini.move_to()
            page.button_info_mini.wait_for_clickability_and_visibility()


@allure.feature('Смоук тест')
@allure.story('Проверка номеров Header с Header-mini')
def test_header_numbers(web_browser):
    """ Убеждаемся, что номера отображаются корректно. """

    page = HeaderBtn(web_browser)

    with allure.step("Проверка номера 'А1' Header and Header-mini"):
        if check.equal(page.number_A1.get_attribute('title'), '+375296041133'):
            check.is_true(page.number_A1.wait_for_visibility())
            num = page.number_A1.get_attribute('title')
            page.execute_script("window.scrollTo(0, 200)")
            page.button_info_mini.move_to()
            check.is_true(page.number_A1_mini.wait_for_visibility())
            check.equal(num, page.number_A1_mini.get_attribute('title'))

    with allure.step("Проверка номера 'mts' Header and Header-mini"):
        if check.equal(page.number_mts.get_attribute('title'), '+375298821133'):
            check.is_true(page.number_mts.wait_for_visibility())
            num = page.number_mts.get_attribute('title')
            page.execute_script("window.scrollTo(0, 200)")
            page.button_info_mini.move_to()
            check.is_true(page.number_mts_mini.wait_for_visibility())
            check.equal(num, page.number_mts_mini.get_attribute('title'))

    with allure.step("Проверка номера 'city' Header and Header-mini"):
        if check.equal(page.number_city.get_attribute('title'), '+375172423777'):
            check.is_true(page.number_city.wait_for_visibility())
            num = page.number_city.get_attribute('title')
            page.execute_script("window.scrollTo(0, 200)")
            page.button_info_mini.move_to()
            check.is_true(page.number_city_mini.wait_for_visibility())
            check.equal(num, page.number_city_mini.get_attribute('title'))


@allure.feature('Смоук тест')
@allure.story('Имитация скролла в низ экрана и нажатие кнопоки Инстаграм')
def test_header_btn_inst(web_browser):
    """ Убеждаемся, что ссылка/кнопка Инстаграм
        кликабельна и переход на страницу корректный. """

    page = HeaderBtn(web_browser)

    with allure.step("Проверка кнопки 'Инстаграм'"):
        if check.equal(page.button_instagram.get_attribute('href'),
                       'https://www.instagram.com/dollar_by'):
            check.is_true(page.button_instagram.wait_for_visibility())
            check.is_true(page.button_instagram.wait_to_be_clickable())
            page.button_instagram.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.instagram.com/dollar_by/')


@allure.feature('Смоук тест')
@allure.story('Имитация скролла в низ экрана и нажатие кнопоки Фейсбук')
def test_header_btn_facebook(web_browser):
    """ Убеждаемся, что ссылка/кнопка Фейсбук
        кликабельна и переход на страницу корректный. """

    page = HeaderBtn(web_browser)
    with allure.step("Проверка кнопки 'Фейсбук'"):
        if check.equal(page.button_facebook.get_attribute('href'),
                       'https://web.facebook.com/shop.dollarby'):
            check.is_true(page.button_facebook.wait_for_visibility())
            check.is_true(page.button_facebook.wait_to_be_clickable())
            page.button_facebook.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.facebook.com/shop.dollarby?_rdc=1&_rdr')
            time.sleep(3)


@allure.feature('Смоук тест')
@allure.story('Имитация скролла в низ экрана и нажатие кнопоки Телеграм')
def test_header_btn_telegram(web_browser):
    """ Убеждаемся, что ссылка/кнопка Телеграм
        кликабельна и переход на страницу корректный. """

    page = HeaderBtn(web_browser)
    with allure.step("Проверка кнопки 'Телеграм'"):
        if check.equal(page.button_telegram.get_attribute('href'), 'https://t.me/dollar_by'):
            check.is_true(page.button_telegram.wait_for_visibility())
            check.is_true(page.button_telegram.wait_to_be_clickable())
            page.button_telegram.click()
            page.switch_to_window(1)
            page1 = page.get_current_url()
            check.equal(page1, 'https://t.me/dollar_by')


@allure.feature('Смоук тест')
@allure.story('Имитация скролла в низ экрана и нажатие кнопоки Вайбер')
def test_header_btn_viber(web_browser):
    """ Убеждаемся, что ссылка/кнопка Вайбер
        кликабельна и переход на страницу корректный. """

    page = HeaderBtn(web_browser)
    with allure.step("Проверка кнопки 'Вайбер'"):
        if check.equal(page.button_viber.get_attribute('href'), 'https://invite.viber.com/'
                                                                '?g2=AQBIWbyAVgCbg0%2B1SCjEk6'
                                                                'Bag5eggt%2FlNWuDPWLjmgnpuFeM'
                                                                'EH5DJmQf93uWJwJK'):
            check.is_true(page.button_viber.wait_for_visibility())
            check.is_true(page.button_viber.wait_to_be_clickable())
            page.button_viber.click()
            page.switch_to_window(1)
            page1 = page.get_current_url()
            check.equal(page1, 'https://invite.viber.com/?g2=AQBIWbyAVgCbg0%2B'
                               '1SCjEk6Bag5eggt%2FlNWuDPWLjmgnpuFeMEH5DJmQf93uWJwJK&lang=ru')


@allure.feature('Смоук тест')
@allure.story('Имитация скролла в низ экрана и нажатие кнопоки Ватцап')
def test_header_btn_whatsapp(web_browser):
    """ Убеждаемся, что ссылка/кнопка Ватцап
        кликабельна и переход на страницу корректный. """

    page = HeaderBtn(web_browser)
    with allure.step("Проверка кнопки 'Ватцап'"):
        if check.equal(page.button_watsapp.get_attribute('href'), 'https://wa.me/+375296041133'):
            check.is_true(page.button_watsapp.wait_for_visibility())
            check.is_true(page.button_watsapp.wait_to_be_clickable())
            page.button_watsapp.click()
            page.switch_to_window(1)
            page1 = page.get_current_url()
            check.equal(page1, 'https://api.whatsapp.com/send/?phone=%2B375296041133&text&type'
                               '=phone_number&app_absent=0')


# <--------------------------------------------FUTER----------------------------------------------->
@allure.feature('Смоук тест')
@allure.story('Имитация скролла в низ экрана и нажатия кнопок Футера')
def test_futer_btn(web_browser):
    """ Убеждаемся, что ссылки/кнопки футера
        кликабельные и переход на страницу корректный. """

    page = FuterBtn(web_browser)

    with allure.step("Проверка кнопки 'Главная'"):
        if check.equal(page.button_glavnaya_foot.get_text(), 'Главная'):
            check.equal(page.button_glavnaya_foot.get_attribute('href'),
                        'https://www.dollar.by/')
            page.button_glavnaya_foot.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/')
            check.is_true(page.button_glavnaya_foot.wait_for_visibility())
            check.is_true(page.button_glavnaya_foot.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Новости'"):
        if check.equal(page.button_novosti_foot.get_text(), 'Новости'):
            check.equal(page.button_novosti_foot.get_attribute('href'),
                        'https://www.dollar.by/news')
            page.button_novosti_foot.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/news')
            check.is_true(page.button_novosti_foot.wait_for_visibility())
            check.is_true(page.button_novosti_foot.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Статьи'"):
        if check.equal(page.button_stati_foot.get_text(), 'Статьи'):
            check.equal(page.button_stati_foot.get_attribute('href'),
                        'https://www.dollar.by/articles')
            page.button_stati_foot.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/articles')
            check.is_true(page.button_stati_foot.wait_for_visibility())
            check.is_true(page.button_stati_foot.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'О магазине'"):
        if check.equal(page.button_o_magazine_foot.get_text(), 'О магазине'):
            check.equal(page.button_o_magazine_foot.get_attribute('href'),
                        'https://www.dollar.by/about')
            page.button_o_magazine_foot.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/about')
            check.is_true(page.button_o_magazine_foot.wait_for_visibility())
            check.is_true(page.button_o_magazine_foot.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Доставка и оплата'"):
        if check.equal(page.button_dostavka_i_oplata_foot.get_text(), 'Доставка и оплата'):
            check.equal(page.button_dostavka_i_oplata_foot.get_attribute('href'),
                        'https://www.dollar.by/orders')
            page.button_dostavka_i_oplata_foot.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/orders')
            check.is_true(page.button_dostavka_i_oplata_foot.wait_for_visibility())
            check.is_true(page.button_dostavka_i_oplata_foot.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Контакты'"):
        if check.equal(page.button_kontakty_foot.get_text(), 'Контакты'):
            check.equal(page.button_kontakty_foot.get_attribute('href'),
                        'https://www.dollar.by/contact')
            page.button_kontakty_foot.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/contact')
            check.is_true(page.button_kontakty_foot.wait_for_visibility())
            check.is_true(page.button_kontakty_foot.wait_to_be_clickable())


@allure.feature('Смоук тест')
@allure.story('Имитация скролла в низ экрана и нажатие кнопоки Инстаграм')
def test_futer_inst(web_browser):
    """ Убеждаемся, что ссылка/кнопка Инстаграм
        кликабельна и переход на страницу корректный (Футер). """

    page = FuterBtn(web_browser)

    with allure.step("Проверка кнопки футера 'Инстаграм'"):
        if check.equal(page.inst_foot.get_attribute('href'),
                       'https://www.instagram.com/dollar_by'):
            check.is_true(page.inst_foot.wait_for_visibility())
            check.is_true(page.inst_foot.wait_to_be_clickable())
            page.inst_foot.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.instagram.com/dollar_by/')


@allure.feature('Смоук тест')
@allure.story('Имитация скролла в низ экрана и нажатие кнопоки Фейсбук')
def test_futer_btn_facebook(web_browser):
    """ Убеждаемся, что ссылка/кнопка Фейсбук
        кликабельна и переход на страницу корректный. """

    page = FuterBtn(web_browser)

    with allure.step("Проверка кнопки футера 'Фейсбук'"):
        if check.equal(page.face_foot.get_attribute('href'),
                       'https://web.facebook.com/shop.dollarby'):
            check.is_true(page.face_foot.wait_for_visibility())
            check.is_true(page.face_foot.wait_to_be_clickable())
            page.face_foot.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.facebook.com/shop.dollarby?_rdc=1&_rdr')
            time.sleep(3)


@allure.feature('Смоук тест')
@allure.story('Имитация скролла в низ экрана и нажатие кнопоки VK')
def test_futer_btn_vk(web_browser):
    """ Убеждаемся, что ссылка/кнопка ВК
        кликабельна и переход на страницу корректный. """

    page = FuterBtn(web_browser)

    with allure.step("Проверка кнопки футера 'ВК'"):
        if check.equal(page.vk_foot.get_attribute('href'), 'https://vk.com/dollar_by'):
            check.is_true(page.vk_foot.wait_for_visibility())
            check.is_true(page.vk_foot.wait_to_be_clickable())
            page.vk_foot.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://vk.com/dollar_by')


# <------------------------------------------CATALOG----------------------------------------------->
@allure.feature('Смоук тест')
@allure.story('Имитация скролла в низ экрана и нажатия кнопок Каталога')
def test_catalog_btn(web_browser):
    """ Убеждаемся, что ссылки/кнопки Каталога
        кликабельные и переход на страницу корректный. """

    page = CatalogBtn(web_browser)

    with allure.step("Проверка кнопки 'Новинки'"):
        if check.equal(page.button_novinki.get_text(), 'Новинки'):
            check.equal(page.button_novinki.get_attribute('href'),
                        'https://www.dollar.by/catalog/Novinki')
            page.button_novinki.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/Novinki')
            check.is_true(page.button_novinki.wait_for_visibility())
            check.is_true(page.button_novinki.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Подарочные наборы'"):
        if check.equal(page.button_podarochnyye_nabory.get_text(), 'Подарочные наборы'):
            check.equal(page.button_podarochnyye_nabory.get_attribute('href'),
                        'https://www.dollar.by/catalog/podarochnyie-naboryi')
            page.button_podarochnyye_nabory.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/podarochnyie-naboryi')
            check.is_true(page.button_podarochnyye_nabory.wait_for_visibility())
            check.is_true(page.button_podarochnyye_nabory.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'РАСПРОДАЖА!'"):
        if check.equal(page.button_rasprodazha.get_text(), 'РАСПРОДАЖА!'):
            check.equal(page.button_rasprodazha.get_attribute('href'),
                        'https://www.dollar.by/catalog/rasprodazha')
            page.button_rasprodazha.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/rasprodazha')
            check.is_true(page.button_rasprodazha.wait_for_visibility())
            check.is_true(page.button_rasprodazha.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Осенняя распродажа'"):
        page.button_rasprodazha.move_to()
        if check.equal(page.rasprodazha_osen.get_text(), 'Осенняя распродажа'):
            check.equal(page.rasprodazha_osen.get_attribute('href'),
                        'https://www.dollar.by/catalog/rasprodazha/vesennyaya-rasprodazha')
            check.is_true(page.rasprodazha_osen.wait_for_visibility())
            check.is_true(page.rasprodazha_osen.wait_to_be_clickable())
            page.rasprodazha_osen.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/rasprodazha/vesennyaya-rasprodazha')

    with allure.step("Проверка кнопки 'Подарки для женщин'"):
        if check.equal(page.button_podarki_dlya_zhenshchin.get_text(), 'Подарки для женщин'):
            check.equal(page.button_podarki_dlya_zhenshchin.get_attribute('href'),
                        'https://www.dollar.by/catalog/Podarki-na-8-marta')
            page.button_podarki_dlya_zhenshchin.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/Podarki-na-8-marta')
            check.is_true(page.button_podarki_dlya_zhenshchin.wait_for_visibility())
            check.is_true(page.button_podarki_dlya_zhenshchin.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Выгодное предложение'"):
        if check.equal(page.button_profitable_proposition.get_text(), 'Выгодное предложение'):
            check.equal(page.button_profitable_proposition.get_attribute('href'),
                        'https://www.dollar.by/catalog/Vygodnoe-predlozhenie')
            page.button_profitable_proposition.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/Vygodnoe-predlozhenie')
            check.is_true(page.button_profitable_proposition.wait_for_visibility())
            check.is_true(page.button_profitable_proposition.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Подарки для мужчин'"):
        if check.equal(page.button_podarki_dlya_muzhchin.get_text(), 'Подарки для мужчин'):
            check.equal(page.button_podarki_dlya_muzhchin.get_attribute('href'),
                        'https://www.dollar.by/catalog/18274')
            page.button_podarki_dlya_muzhchin.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/18274')
            check.is_true(page.button_podarki_dlya_muzhchin.wait_for_visibility())
            check.is_true(page.button_podarki_dlya_muzhchin.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Весенние скидки!'"):
        if check.equal(page.button_vesenniye_skidki.get_text(), 'Весенние скидки!'):
            check.equal(page.button_vesenniye_skidki.get_attribute('href'),
                        'https://www.dollar.by/catalog/18275')
            page.button_vesenniye_skidki.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/18275')
            check.is_true(page.button_vesenniye_skidki.wait_for_visibility())
            check.is_true(page.button_vesenniye_skidki.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Новогодние товары'"):
        if check.equal(page.button_novogodniye_tovary.get_text(), 'Новогодние товары'):
            check.equal(page.button_novogodniye_tovary.get_attribute('href'),
                        'https://www.dollar.by/catalog/Novogodnie-tovary')
            page.button_novogodniye_tovary.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/Novogodnie-tovary')
            check.is_true(page.button_novogodniye_tovary.wait_for_visibility())
            check.is_true(page.button_novogodniye_tovary.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Распродажа новогодних товаров'"):
        page.button_novogodniye_tovary.move_to()
        if check.equal(page.rasprodazha_novogodnikh_tovarov.get_text(),
                       'Распродажа новогодних товаров'):
            check.equal(page.rasprodazha_novogodnikh_tovarov.get_attribute('href'),
                        'https://www.dollar.by/catalog/Novogodnie-tovary/'
                        'Rasprodazha-novogodnikh-tovarov')
            check.is_true(page.rasprodazha_novogodnikh_tovarov.wait_for_visibility())
            check.is_true(page.rasprodazha_novogodnikh_tovarov.wait_to_be_clickable())
            page.rasprodazha_novogodnikh_tovarov.click()
            page1 = page.get_current_url()
            check.equal(page1,'https://www.dollar.by/catalog/Novogodnie-tovary/'
                        'Rasprodazha-novogodnikh-tovarov')

    with allure.step("Проверка кнопки 'Новогодние деревья (ели и сосны) и гирлянды'"):
        page.button_novogodniye_tovary.move_to()
        if check.equal(page.novogodniye_derevya.get_text(),
                       'Новогодние деревья (ели и сосны) и гирлянды'):
            check.equal(page.novogodniye_derevya.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-cleaning/Novogodnie-tovary/'
                        'Novogodnie-derevya-eli-i-sosny-i-girlyandy')
            check.is_true(page.novogodniye_derevya.wait_for_visibility())
            check.is_true(page.novogodniye_derevya.wait_to_be_clickable())
            page.novogodniye_derevya.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-cleaning/'
                               'Novogodnie-tovary/Novogodnie-derevya-eli-i-sosny-i-girlyandy')

    with allure.step("Проверка кнопки 'Новогодние гирлянды и венки'"):
        page.button_novogodniye_tovary.move_to()
        if check.equal(page.girlyandy_i_venki.get_text(), 'Новогодние гирлянды и венки'):
            check.equal(page.girlyandy_i_venki.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-cleaning/Novogodnie-tovary/'
                        'Novogodnie-derevya-eli-i-sosny-i-girlyandy/Novogodnie-girlyandy-i-venki')
            check.is_true(page.girlyandy_i_venki.wait_for_visibility())
            check.is_true(page.girlyandy_i_venki.wait_to_be_clickable())
            page.girlyandy_i_venki.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-cleaning/'
                               'Novogodnie-tovary/Novogodnie-derevya-eli-i-sosny-i-girlyandy/'
                               'Novogodnie-girlyandy-i-venki')

    with allure.step("Проверка кнопки 'Новогодние ели и сосны'"):
        page.button_novogodniye_tovary.move_to()
        if check.equal(page.yeli_i_sosny.get_text(), 'Новогодние ели и сосны'):
            check.equal(page.yeli_i_sosny.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-cleaning/Novogodnie-tovary/'
                        'Novogodnie-derevya-eli-i-sosny-i-girlyandy/Novogodnie-eli-i-sosny')
            check.is_true(page.yeli_i_sosny.wait_for_visibility())
            check.is_true(page.yeli_i_sosny.wait_to_be_clickable())
            page.yeli_i_sosny.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-cleaning/'
                               'Novogodnie-tovary/Novogodnie-derevya-eli-i-sosny-i-girlyandy/'
                               'Novogodnie-eli-i-sosny')

    with allure.step("Проверка кнопки 'Новогодние игрушки, статуэтки и фигурки'"):
        page.button_novogodniye_tovary.move_to()
        if check.equal(page.igrushki_statuetki.get_text(), 'Новогодние игрушки, статуэтки и фигурки'):
            check.equal(page.igrushki_statuetki.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-cleaning/'
                        'Novogodnie-tovary/7496')
            check.is_true(page.igrushki_statuetki.wait_for_visibility())
            check.is_true(page.igrushki_statuetki.wait_to_be_clickable())
            page.igrushki_statuetki.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-cleaning/'
                               'Novogodnie-tovary/7496')

    with allure.step("Проверка кнопки 'Товары для школы'"):
        if check.equal(page.button_tovary_dlya_shkoly.get_text(), 'Товары для школы'):
            check.equal(page.button_tovary_dlya_shkoly.get_attribute('href'),
                        'https://www.dollar.by/catalog/Tovary_dlya_shkoly')
            page.button_tovary_dlya_shkoly.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/Tovary_dlya_shkoly')
            check.is_true(page.button_tovary_dlya_shkoly.wait_for_visibility())
            check.is_true(page.button_tovary_dlya_shkoly.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Товары для кухни'"):
        page.execute_script("window.scrollTo(0, 200)")
        if check.equal(page.button_tovary_dlya_kukhni.get_text(), 'Товары для кухни'):
            check.equal(page.button_tovary_dlya_kukhni.get_attribute('href'),
                        'https://www.dollar.by/catalog/Tovary_dlya_kukhni')
            page.button_tovary_dlya_kukhni.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/Tovary_dlya_kukhni')
            check.is_true(page.button_tovary_dlya_kukhni.wait_for_visibility())
            check.is_true(page.button_tovary_dlya_kukhni.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Распродажа товаров для кухни'"):
        page.execute_script("window.scrollTo(0, 200)")
        page.button_tovary_dlya_kukhni.move_to()
        if check.equal(page.rasprodazha_kukhni.get_text(), 'Распродажа товаров для кухни'):
            check.equal(page.rasprodazha_kukhni.get_attribute('href'),
                        'https://www.dollar.by/catalog/Tovary_dlya_kukhni/'
                        'Rasprodazha-tovarov-dlya-kukhni')
            check.is_true(page.rasprodazha_kukhni.wait_for_visibility())
            check.is_true(page.rasprodazha_kukhni.wait_to_be_clickable())
            page.rasprodazha_kukhni.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/Tovary_dlya_kukhni/'
                               'Rasprodazha-tovarov-dlya-kukhni')

    with allure.step("Проверка кнопки 'Наборы посуды'"):
        page.execute_script("window.scrollTo(0, 200)")
        page.button_tovary_dlya_kukhni.move_to()
        if check.equal(page.nabory_posudy.get_text(), 'Наборы посуды'):
            check.equal(page.nabory_posudy.get_attribute('href'),
                        'https://www.dollar.by/catalog/Tovary_dlya_kukhni/nabory-posudi')
            check.is_true(page.nabory_posudy.wait_for_visibility())
            check.is_true(page.nabory_posudy.wait_to_be_clickable())
            page.nabory_posudy.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/Tovary_dlya_kukhni/nabory-posudi')

    with allure.step("Проверка кнопки 'Кастрюли'"):
        page.execute_script("window.scrollTo(0, 200)")
        page.button_tovary_dlya_kukhni.move_to()
        if check.equal(page.kastryuli.get_text(), 'Кастрюли'):
            check.equal(page.kastryuli.get_attribute('href'),
                        'https://www.dollar.by/catalog/Tovary_dlya_kukhni/931')
            check.is_true(page.kastryuli.wait_for_visibility())
            check.is_true(page.kastryuli.wait_to_be_clickable())
            page.kastryuli.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/Tovary_dlya_kukhni/931')

    with allure.step("Проверка кнопки 'Кухонные, столовые принадлежности'"):
        page.execute_script("window.scrollTo(0, 200)")
        page.button_tovary_dlya_kukhni.move_to()
        if check.equal(page.kukhonnyye_stolovyye.get_text(), 'Кухонные, столовые принадлежности'):
            check.equal(page.kukhonnyye_stolovyye.get_attribute('href'),
                        'https://www.dollar.by/catalog/Tovary_dlya_kukhni/936')
            check.is_true(page.kukhonnyye_stolovyye.wait_for_visibility())
            check.is_true(page.kukhonnyye_stolovyye.wait_to_be_clickable())
            page.kukhonnyye_stolovyye.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/Tovary_dlya_kukhni/936')

    with allure.step("Проверка кнопки 'Терки Овощерезки Кухонные'"):
        page.execute_script("window.scrollTo(0, 200)")
        page.button_tovary_dlya_kukhni.move_to()
        if check.equal(page.terki_ovoshcherezki.get_text(), 'Терки Овощерезки Кухонные'):
            check.equal(page.terki_ovoshcherezki.get_attribute('href'),
                        'https://www.dollar.by/catalog/Tovary_dlya_kukhni/937')
            check.is_true(page.terki_ovoshcherezki.wait_for_visibility())
            check.is_true(page.terki_ovoshcherezki.wait_to_be_clickable())
            page.terki_ovoshcherezki.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/Tovary_dlya_kukhni/937')

    with allure.step("Проверка кнопки 'Наборы ножей'"):
        page.execute_script("window.scrollTo(0, 200)")
        page.button_tovary_dlya_kukhni.move_to()
        if check.equal(page.nabory_nozhey.get_text(), 'Наборы ножей'):
            check.equal(page.nabory_nozhey.get_attribute('href'),
                        'https://www.dollar.by/catalog/Tovary_dlya_kukhni/938')
            check.is_true(page.nabory_nozhey.wait_for_visibility())
            check.is_true(page.nabory_nozhey.wait_to_be_clickable())
            page.nabory_nozhey.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/Tovary_dlya_kukhni/938')

    with allure.step("Проверка кнопки 'Для заточки ножей и ножниц'"):
        page.execute_script("window.scrollTo(0, 200)")
        page.button_tovary_dlya_kukhni.move_to()
        if check.equal(page.dlya_zatochki_nozhey.get_text(), 'Для заточки ножей и ножниц'):
            check.equal(page.dlya_zatochki_nozhey.get_attribute('href'),
                        'https://www.dollar.by/catalog/Tovary_dlya_kukhni/938/'
                        'dlya-zatochki-nozhej-i-nozhnits')
            check.is_true(page.dlya_zatochki_nozhey.wait_for_visibility())
            check.is_true(page.dlya_zatochki_nozhey.wait_to_be_clickable())
            page.dlya_zatochki_nozhey.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/Tovary_dlya_kukhni/938/'
                               'dlya-zatochki-nozhej-i-nozhnits')

    with allure.step("Проверка кнопки 'Сковороды'"):
        page.execute_script("window.scrollTo(0, 200)")
        page.button_tovary_dlya_kukhni.move_to()
        if check.equal(page.skovorody.get_text(), 'Сковороды'):
            check.equal(page.skovorody.get_attribute('href'),
                        'https://www.dollar.by/catalog/Tovary_dlya_kukhni/939')
            check.is_true(page.skovorody.wait_for_visibility())
            check.is_true(page.skovorody.wait_to_be_clickable())
            page.skovorody.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/Tovary_dlya_kukhni/939')

    with allure.step("Проверка кнопки 'Мантоварки'"):
        page.execute_script("window.scrollTo(0, 200)")
        page.button_tovary_dlya_kukhni.move_to()
        if check.equal(page.mantovarki.get_text(), 'Мантоварки'):
            check.equal(page.mantovarki.get_attribute('href'),
                        'https://www.dollar.by/catalog/Tovary_dlya_kukhni/942')
            check.is_true(page.mantovarki.wait_for_visibility())
            check.is_true(page.mantovarki.wait_to_be_clickable())
            page.mantovarki.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/Tovary_dlya_kukhni/942')

    with allure.step("Проверка кнопки 'Соковыжималки'"):
        page.execute_script("window.scrollTo(0, 200)")
        page.button_tovary_dlya_kukhni.move_to()
        if check.equal(page.sokovyzhimalki.get_text(), 'Соковыжималки'):
            check.equal(page.sokovyzhimalki.get_attribute('href'),
                        'https://www.dollar.by/catalog/Tovary_dlya_kukhni/1139')
            check.is_true(page.sokovyzhimalki.wait_for_visibility())
            check.is_true(page.sokovyzhimalki.wait_to_be_clickable())
            page.sokovyzhimalki.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/Tovary_dlya_kukhni/1139')

    with allure.step("Проверка кнопки 'Термосы'"):
        page.execute_script("window.scrollTo(0, 200)")
        page.button_tovary_dlya_kukhni.move_to()
        if check.equal(page.termosy.get_text(), 'Термосы'):
            check.equal(page.termosy.get_attribute('href'),
                        'https://www.dollar.by/catalog/Tovary_dlya_kukhni/2237')
            check.is_true(page.termosy.wait_for_visibility())
            check.is_true(page.termosy.wait_to_be_clickable())
            page.termosy.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/Tovary_dlya_kukhni/2237')

    with allure.step("Проверка кнопки 'Ножи керамические'"):
        page.execute_script("window.scrollTo(0, 200)")
        page.button_tovary_dlya_kukhni.move_to()
        if check.equal(page.nozhi_keramicheskiye.get_text(), 'Ножи керамические'):
            check.equal(page.nozhi_keramicheskiye.get_attribute('href'),
                        'https://www.dollar.by/catalog/kitchen/2243')
            check.is_true(page.nozhi_keramicheskiye.wait_for_visibility())
            check.is_true(page.nozhi_keramicheskiye.wait_to_be_clickable())
            page.nozhi_keramicheskiye.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/kitchen/2243')

    with allure.step("Проверка кнопки 'Посуда PENSOFAL'"):
        page.execute_script("window.scrollTo(0, 200)")
        page.button_tovary_dlya_kukhni.move_to()
        if check.equal(page.posuda_pensofal.get_text(), 'Посуда PENSOFAL'):
            check.equal(page.posuda_pensofal.get_attribute('href'),
                        'https://www.dollar.by/catalog/kitchen/2546')
            check.is_true(page.posuda_pensofal.wait_for_visibility())
            check.is_true(page.posuda_pensofal.wait_to_be_clickable())
            page.posuda_pensofal.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/kitchen/2546')

    with allure.step("Проверка кнопки 'Соковарки'"):
        page.execute_script("window.scrollTo(0, 200)")
        page.button_tovary_dlya_kukhni.move_to()
        if check.equal(page.cokovarki.get_text(), 'Соковарки'):
            check.equal(page.cokovarki.get_attribute('href'),
                        'https://www.dollar.by/catalog/kitchen/4775')
            check.is_true(page.cokovarki.wait_for_visibility())
            check.is_true(page.cokovarki.wait_to_be_clickable())
            page.cokovarki.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/kitchen/4775')

    with allure.step("Проверка кнопки 'Формы для выпечки'"):
        page.execute_script("window.scrollTo(0, 200)")
        page.button_tovary_dlya_kukhni.move_to()
        if check.equal(page.formy_dlya_vypechki.get_text(), 'Формы для выпечки'):
            check.equal(page.formy_dlya_vypechki.get_attribute('href'),
                        'https://www.dollar.by/catalog/kitchen/4858')
            check.is_true(page.formy_dlya_vypechki.wait_for_visibility())
            check.is_true(page.formy_dlya_vypechki.wait_to_be_clickable())
            page.formy_dlya_vypechki.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/kitchen/4858')

    with allure.step("Проверка кнопки 'Сушилки для овощей, фруктов и грибов'"):
        page.execute_script("window.scrollTo(0, 200)")
        page.button_tovary_dlya_kukhni.move_to()
        if check.equal(page.sushilki_dlya_ovoshchey.get_text(),
                       'Сушилки для овощей, фруктов и грибов'):
            check.equal(page.sushilki_dlya_ovoshchey.get_attribute('href'),
                        'https://www.dollar.by/catalog/Tovary_dlya_kukhni/'
                        'sushilki-dlya-ovoschej-fruktov-i-gribov')
            check.is_true(page.sushilki_dlya_ovoshchey.wait_for_visibility())
            check.is_true(page.sushilki_dlya_ovoshchey.wait_to_be_clickable())
            page.sushilki_dlya_ovoshchey.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/Tovary_dlya_kukhni/'
                               'sushilki-dlya-ovoschej-fruktov-i-gribov')

    with allure.step("Проверка кнопки 'Вакуумные контейнеры'"):
        page.execute_script("window.scrollTo(0, 200)")
        page.button_tovary_dlya_kukhni.move_to()
        if check.equal(page.vakuumnyye_konteynery.get_text(), 'Вакуумные контейнеры'):
            check.equal(page.vakuumnyye_konteynery.get_attribute('href'),
                        'https://www.dollar.by/catalog/kitchen/5162')
            check.is_true(page.vakuumnyye_konteynery.wait_for_visibility())
            check.is_true(page.vakuumnyye_konteynery.wait_to_be_clickable())
            page.vakuumnyye_konteynery.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/kitchen/5162')

    with allure.step("Проверка кнопки 'Аппараты для приготовления попкорна'"):
        page.execute_script("window.scrollTo(0, 200)")
        page.button_tovary_dlya_kukhni.move_to()
        if check.equal(page.apparaty_popkorna.get_text(), 'Аппараты для приготовления попкорна'):
            check.equal(page.apparaty_popkorna.get_attribute('href'),
                        'https://www.dollar.by/catalog/Tovary_dlya_kukhni/5237')
            check.is_true(page.apparaty_popkorna.wait_for_visibility())
            check.is_true(page.apparaty_popkorna.wait_to_be_clickable())
            page.apparaty_popkorna.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/Tovary_dlya_kukhni/5237')

    with allure.step("Проверка кнопки 'Аппараты для приготовления сахарной ваты'"):
        page.execute_script("window.scrollTo(0, 200)")
        page.button_tovary_dlya_kukhni.move_to()
        if check.equal(page.apparaty_sakharnoy_vaty.get_text(),
                       'Аппараты для приготовления сахарной ваты'):
            check.equal(page.apparaty_sakharnoy_vaty.get_attribute('href'),
                        'https://www.dollar.by/catalog/kitchen/5239')
            check.is_true(page.apparaty_sakharnoy_vaty.wait_for_visibility())
            check.is_true(page.apparaty_sakharnoy_vaty.wait_to_be_clickable())
            page.apparaty_sakharnoy_vaty.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/kitchen/5239')

    with allure.step("Проверка кнопки 'Товары для дома'"):
        page.execute_script("window.scrollTo(0, 300)")
        if check.equal(page.button_tovary_dlya_doma.get_text(), 'Товары для дома'):
            check.equal(page.button_tovary_dlya_doma.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house')
            page.button_tovary_dlya_doma.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house')
            check.is_true(page.button_tovary_dlya_doma.wait_for_visibility())
            check.is_true(page.button_tovary_dlya_doma.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Необычные светильники, проекторы'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.neobychnyye_svetilniki.get_text(), 'Необычные светильники, проекторы'):
            check.equal(page.neobychnyye_svetilniki.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/1284')
            check.is_true(page.neobychnyye_svetilniki.wait_for_visibility())
            check.is_true(page.neobychnyye_svetilniki.wait_to_be_clickable())
            page.neobychnyye_svetilniki.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/1284')

    with allure.step("Проверка кнопки 'Бытовая техника'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.bytovaya_tekhnika.get_text(), 'Бытовая техника'):
            check.equal(page.bytovaya_tekhnika.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/home-appliances')
            check.is_true(page.bytovaya_tekhnika.wait_for_visibility())
            check.is_true(page.bytovaya_tekhnika.wait_to_be_clickable())
            page.bytovaya_tekhnika.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/'
                               'home-appliances')

    with allure.step("Проверка кнопки 'Вентиляторы'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.ventilyatory.get_text(), 'Вентиляторы'):
            check.equal(page.ventilyatory.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/'
                        'home-appliances/fans')
            check.is_true(page.ventilyatory.wait_for_visibility())
            check.is_true(page.ventilyatory.wait_to_be_clickable())
            page.ventilyatory.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/'
                               'home-appliances/fans')

    with allure.step("Проверка кнопки 'Обогреватели'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.obogrevateli.get_text(), 'Обогреватели'):
            check.equal(page.obogrevateli.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/'
                        'home-appliances/heaters')
            check.is_true(page.obogrevateli.wait_for_visibility())
            check.is_true(page.obogrevateli.wait_to_be_clickable())
            page.obogrevateli.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/'
                               'home-appliances/heaters')

    with allure.step("Проверка кнопки 'Аэрогрили'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.aerogrili.get_text(), 'Аэрогрили'):
            check.equal(page.aerogrili.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/'
                        'home-appliances/aerogrills')
            check.is_true(page.aerogrili.wait_for_visibility())
            check.is_true(page.aerogrili.wait_to_be_clickable())
            page.aerogrili.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/'
                               'home-appliances/aerogrills')

    with allure.step("Проверка кнопки 'Блендеры, миксеры'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.blendery_miksery.get_text(), 'Блендеры, миксеры'):
            check.equal(page.blendery_miksery.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/'
                        'home-appliances/blenders-mixers')
            check.is_true(page.blendery_miksery.wait_for_visibility())
            check.is_true(page.blendery_miksery.wait_to_be_clickable())
            page.blendery_miksery.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/'
                               'home-appliances/blenders-mixers')

    with allure.step("Проверка кнопки 'Машинки по уходу за одеждой'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.mashinki_odezhdoy.get_text(), 'Машинки по уходу за одеждой'):
            check.equal(page.mashinki_odezhdoy.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/'
                        'home-appliances/machines-on-care-of-clothes')
            check.is_true(page.mashinki_odezhdoy.wait_for_visibility())
            check.is_true(page.mashinki_odezhdoy.wait_to_be_clickable())
            page.mashinki_odezhdoy.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/'
                               'home-appliances/machines-on-care-of-clothes')

    with allure.step("Проверка кнопки 'Пароочистители'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.paroochistiteli.get_text(), 'Пароочистители'):
            check.equal(page.paroochistiteli.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/'
                        'home-appliances/1159')
            check.is_true(page.paroochistiteli.wait_for_visibility())
            check.is_true(page.paroochistiteli.wait_to_be_clickable())
            page.paroochistiteli.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/'
                               'home-appliances/1159')

    with allure.step("Проверка кнопки 'Пылесосы'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.pylesosy.get_text(), 'Пылесосы'):
            check.equal(page.pylesosy.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/'
                        'home-appliances/2251')
            check.is_true(page.pylesosy.wait_for_visibility())
            check.is_true(page.pylesosy.wait_to_be_clickable())
            page.pylesosy.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/'
                               'home-appliances/2251')

    with allure.step("Проверка кнопки 'Утюги'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.utyugi.get_text(), 'Утюги'):
            check.equal(page.utyugi.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/'
                        'home-appliances/2255')
            check.is_true(page.utyugi.wait_for_visibility())
            check.is_true(page.utyugi.wait_to_be_clickable())
            page.utyugi.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/'
                               'home-appliances/2255')

    with allure.step("Проверка кнопки 'Электрочайники'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.elektrochayniki.get_text(), 'Электрочайники'):
            check.equal(page.elektrochayniki.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/'
                        'home-appliances/2285')
            check.is_true(page.elektrochayniki.wait_for_visibility())
            check.is_true(page.elektrochayniki.wait_to_be_clickable())
            page.elektrochayniki.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/'
                               'home-appliances/2285')

    with allure.step("Проверка кнопки 'Увлажнители воздуха'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.uvlazhniteli_vozdukha.get_text(), 'Увлажнители воздуха'):
            check.equal(page.uvlazhniteli_vozdukha.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/'
                        'home-appliances/5928')
            check.is_true(page.uvlazhniteli_vozdukha.wait_for_visibility())
            check.is_true(page.uvlazhniteli_vozdukha.wait_to_be_clickable())
            page.uvlazhniteli_vozdukha.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/'
                               'home-appliances/5928')

    with allure.step("Проверка кнопки 'Инкубаторы'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.incubators.get_text(), 'Инкубаторы'):
            check.equal(page.incubators.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/'
                        'home-appliances/4610')
            check.is_true(page.incubators.wait_for_visibility())
            check.is_true(page.incubators.wait_to_be_clickable())
            page.incubators.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/'
                               'home-appliances/4610')

    with allure.step("Проверка кнопки 'Электрические котлы'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.elektricheskiye_kotly.get_text(), 'Электрические котлы'):
            check.equal(page.elektricheskiye_kotly.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/'
                        'home-appliances/electrokotli')
            check.is_true(page.elektricheskiye_kotly.wait_for_visibility())
            check.is_true(page.elektricheskiye_kotly.wait_to_be_clickable())
            page.elektricheskiye_kotly.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/'
                               'home-appliances/electrokotli')

    with allure.step("Проверка кнопки 'Отпугиватели'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.otpugivateli.get_text(), 'Отпугиватели'):
            check.equal(page.otpugivateli.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/against-wreckers')
            check.is_true(page.otpugivateli.wait_for_visibility())
            check.is_true(page.otpugivateli.wait_to_be_clickable())
            page.otpugivateli.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/'
                               'against-wreckers')

    with allure.step("Проверка кнопки 'Отпугиватели животных'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.otpugivateli_zhivotnykh.get_text(), 'Отпугиватели животных'):
            check.equal(page.otpugivateli_zhivotnykh.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/against-wreckers/'
                        'Otpugivateli-zhivotnykh')
            check.is_true(page.otpugivateli_zhivotnykh.wait_for_visibility())
            check.is_true(page.otpugivateli_zhivotnykh.wait_to_be_clickable())
            page.otpugivateli_zhivotnykh.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/'
                               'against-wreckers/Otpugivateli-zhivotnykh')

    with allure.step("Проверка кнопки 'Отпугиватели птиц'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.otpugivateli_ptits.get_text(), 'Отпугиватели птиц'):
            check.equal(page.otpugivateli_ptits.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/'
                        'against-wreckers/otpugivateli-ptits')
            check.is_true(page.otpugivateli_ptits.wait_for_visibility())
            check.is_true(page.otpugivateli_ptits.wait_to_be_clickable())
            page.otpugivateli_ptits.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/'
                               'against-wreckers/otpugivateli-ptits')

    with allure.step("Проверка кнопки 'Отпугиватели кротов и змей'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.otpugivateli_krotov.get_text(), 'Отпугиватели кротов и змей'):
            check.equal(page.otpugivateli_krotov.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/'
                        'against-wreckers/Otpugivateli-krotov-i-zmey')
            check.is_true(page.otpugivateli_krotov.wait_for_visibility())
            check.is_true(page.otpugivateli_krotov.wait_to_be_clickable())
            page.otpugivateli_krotov.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/'
                               'against-wreckers/Otpugivateli-krotov-i-zmey')

    with allure.step("Проверка кнопки 'Отпугиватели комаров и других насекомых'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.otpugivateli_komarov.get_text(),
                       'Отпугиватели комаров и других насекомых'):
            check.equal(page.otpugivateli_komarov.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/'
                        'against-wreckers/Otpugivateli-komarov')
            check.is_true(page.otpugivateli_komarov.wait_for_visibility())
            check.is_true(page.otpugivateli_komarov.wait_to_be_clickable())
            page.otpugivateli_komarov.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/'
                               'against-wreckers/Otpugivateli-komarov')

    with allure.step("Проверка кнопки 'Товары для уборки'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.tovary_dly_auborki.get_text(), 'Товары для уборки'):
            check.equal(page.tovary_dly_auborki.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/'
                        'the-goods-for-cleaning')
            check.is_true(page.tovary_dly_auborki.wait_for_visibility())
            check.is_true(page.tovary_dly_auborki.wait_to_be_clickable())
            page.tovary_dly_auborki.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house'
                               '/the-goods-for-cleaning')

    with allure.step("Проверка кнопки 'Сушилки для обуви'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.sushilki_dlya_obuvi.get_text(), 'Сушилки для обуви'):
            check.equal(page.sushilki_dlya_obuvi.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/dryers-for-footwear')
            check.is_true(page.sushilki_dlya_obuvi.wait_for_visibility())
            check.is_true(page.sushilki_dlya_obuvi.wait_to_be_clickable())
            page.sushilki_dlya_obuvi.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/'
                               'dryers-for-footwear')

    with allure.step("Проверка кнопки 'Беспроводные дверные звонки'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.besprovodnyye_zvonki.get_text(), 'Беспроводные дверные звонки'):
            check.equal(page.besprovodnyye_zvonki.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/7629')
            check.is_true(page.besprovodnyye_zvonki.wait_for_visibility())
            check.is_true(page.besprovodnyye_zvonki.wait_to_be_clickable())
            page.besprovodnyye_zvonki.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/7629')

    with allure.step("Проверка кнопки 'Весы'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.vesy.get_text(), 'Весы'):
            check.equal(page.vesy.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/2245')
            check.is_true(page.vesy.wait_for_visibility())
            check.is_true(page.vesy.wait_to_be_clickable())
            page.vesy.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/2245')

    with allure.step("Проверка кнопки 'Для ухода за обувью '"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.dlya_ukhoda_za_obuvyu.get_text(), 'Для ухода за обувью'):
            check.equal(page.dlya_ukhoda_za_obuvyu.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/'
                        'the-goods-for-cleaning/Dlya-ukhoda-za-obuvyu')
            check.is_true(page.dlya_ukhoda_za_obuvyu.wait_for_visibility())
            check.is_true(page.dlya_ukhoda_za_obuvyu.wait_to_be_clickable())
            page.dlya_ukhoda_za_obuvyu.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/'
                               'the-goods-for-cleaning/Dlya-ukhoda-za-obuvyu')

    with allure.step("Проверка кнопки 'Машинки для катышек'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.mashinki_dlya_katyshek.get_text(), 'Машинки для катышек'):
            check.equal(page.mashinki_dlya_katyshek.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/1117')
            check.is_true(page.mashinki_dlya_katyshek.wait_for_visibility())
            check.is_true(page.mashinki_dlya_katyshek.wait_to_be_clickable())
            page.mashinki_dlya_katyshek.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/1117')

    with allure.step("Проверка кнопки 'Планетарии'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.planetarii.get_text(), 'Планетарии'):
            check.equal(page.planetarii.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/7850')
            check.is_true(page.planetarii.wait_for_visibility())
            check.is_true(page.planetarii.wait_to_be_clickable())
            page.planetarii.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/7850')

    with allure.step("Проверка кнопки 'Сигнализация (дверная, оконная, велосипедная)'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.signalizacia.get_text(),
                       'Сигнализация (дверная, оконная, велосипедная)'):
            check.equal(page.signalizacia.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/7712')
            check.is_true(page.signalizacia.wait_for_visibility())
            check.is_true(page.signalizacia.wait_to_be_clickable())
            page.signalizacia.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/7712')

    with allure.step("Проверка кнопки 'Сумки, тележки, рюкзаки'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.sumki_telechki_rykzaki.get_text(), 'Сумки, тележки, рюкзаки'):
            check.equal(page.sumki_telechki_rykzaki.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/7981')
            check.is_true(page.sumki_telechki_rykzaki.wait_for_visibility())
            check.is_true(page.sumki_telechki_rykzaki.wait_to_be_clickable())
            page.sumki_telechki_rykzaki.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/7981')

    with allure.step("Проверка кнопки 'Рюкзаки'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.rykzaki.get_text(), 'Рюкзаки'):
            check.equal(page.rykzaki.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/7981/7982')
            check.is_true(page.rykzaki.wait_for_visibility())
            check.is_true(page.rykzaki.wait_to_be_clickable())
            page.rykzaki.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/7981/7982')

    with allure.step("Проверка кнопки 'Сумки'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.sumki.get_text(), 'Сумки'):
            check.equal(page.sumki.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/7981/7985')
            check.is_true(page.sumki.wait_for_visibility())
            check.is_true(page.sumki.wait_to_be_clickable())
            page.sumki.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/7981/7985')

    with allure.step("Проверка кнопки 'Товары для ремонта'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.tovary_dlya_remonta.get_text(), 'Товары для ремонта'):
            check.equal(page.tovary_dlya_remonta.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/7558')
            check.is_true(page.tovary_dlya_remonta.wait_for_visibility())
            check.is_true(page.tovary_dlya_remonta.wait_to_be_clickable())
            page.tovary_dlya_remonta.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/7558')

    with allure.step("Проверка кнопки 'Товары для ухода за кожей (натуральной и искусственной)'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.tovary_dlya_kozhey.get_text(),
                       'Товары для ухода за кожей (натуральной и искусственной)'):
            check.equal(page.tovary_dlya_kozhey.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/5943')
            check.is_true(page.tovary_dlya_kozhey.wait_for_visibility())
            check.is_true(page.tovary_dlya_kozhey.wait_to_be_clickable())
            page.tovary_dlya_kozhey.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/5943')

    with allure.step("Проверка кнопки 'Умные лампочки (светодиодные лампочки)'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.umnyye_lampochki.get_text(), 'Умные лампочки (светодиодные лампочки)'):
            check.equal(page.umnyye_lampochki.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/11920')
            check.is_true(page.umnyye_lampochki.wait_for_visibility())
            check.is_true(page.umnyye_lampochki.wait_to_be_clickable())
            page.umnyye_lampochki.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/11920')

    with allure.step("Проверка кнопки 'Швейные машины и машинки'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.shveynyye_mashiny.get_text(), 'Швейные машины и машинки'):
            check.equal(page.shveynyye_mashiny.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/sewing-machines')
            check.is_true(page.shveynyye_mashiny.wait_for_visibility())
            check.is_true(page.shveynyye_mashiny.wait_to_be_clickable())
            page.shveynyye_mashiny.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/'
                               'sewing-machines')

    with allure.step("Проверка кнопки 'Распродажа товаров для дома'"):
        page.execute_script("window.scrollTo(0, 300)")
        page.button_tovary_dlya_doma.move_to()
        if check.equal(page.rasprodazha_dlya_doma.get_text(), 'Распродажа товаров для дома'):
            check.equal(page.rasprodazha_dlya_doma.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-goods-for-the-house/'
                        'Rasprodazha-tovarov-dlya-doma')
            check.is_true(page.rasprodazha_dlya_doma.wait_for_visibility())
            check.is_true(page.rasprodazha_dlya_doma.wait_to_be_clickable())
            page.rasprodazha_dlya_doma.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-goods-for-the-house/'
                               'Rasprodazha-tovarov-dlya-doma')

    with allure.step("Проверка кнопки 'Спортивные товары'"):
        if check.equal(page.button_sportivnyye_tovary.get_text(), 'Спортивные товары'):
            check.equal(page.button_sportivnyye_tovary.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-sports-goods')
            page.button_sportivnyye_tovary.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-sports-goods')
            check.is_true(page.button_sportivnyye_tovary.wait_for_visibility())
            check.is_true(page.button_sportivnyye_tovary.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Красота и здоровье'"):
        if check.equal(page.button_krasota_i_zdorovye.get_text(), 'Красота и здоровье'):
            check.equal(page.button_krasota_i_zdorovye.get_attribute('href'),
                        'https://www.dollar.by/catalog/beauty-and-health')
            page.button_krasota_i_zdorovye.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/beauty-and-health')
            check.is_true(page.button_krasota_i_zdorovye.wait_for_visibility())
            check.is_true(page.button_krasota_i_zdorovye.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Сумки, клатчи, рюкзаки'"):
        if check.equal(page.button_sumki_klatchi_ryukzaki.get_text(), 'Сумки, клатчи, рюкзаки'):
            check.equal(page.button_sumki_klatchi_ryukzaki.get_attribute('href'),
                        'https://www.dollar.by/catalog/sumki-klatchi-ryukzaki')
            page.button_sumki_klatchi_ryukzaki.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/sumki-klatchi-ryukzaki')
            check.is_true(page.button_sumki_klatchi_ryukzaki.wait_for_visibility())
            check.is_true(page.button_sumki_klatchi_ryukzaki.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Гаджеты'"):
        if check.equal(page.button_gadzhety.get_text(), 'Гаджеты'):
            check.equal(page.button_gadzhety.get_attribute('href'),
                        'https://www.dollar.by/catalog/electronic-gadget')
            page.button_gadzhety.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/electronic-gadget')
            check.is_true(page.button_gadzhety.wait_for_visibility())
            check.is_true(page.button_gadzhety.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Детский мир'"):
        if check.equal(page.button_detskiy_mir.get_text(), 'Детский мир'):
            check.equal(page.button_detskiy_mir.get_attribute('href'),
                        'https://www.dollar.by/catalog/the-childrens-world')
            page.button_detskiy_mir.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/the-childrens-world')
            check.is_true(page.button_detskiy_mir.wait_for_visibility())
            check.is_true(page.button_detskiy_mir.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Подарки'"):
        if check.equal(page.button_podarki.get_text(), 'Подарки'):
            check.equal(page.button_podarki.get_attribute('href'),
                        'https://www.dollar.by/catalog/gifts')
            page.button_podarki.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/gifts')
            check.is_true(page.button_podarki.wait_for_visibility())
            check.is_true(page.button_podarki.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Авто'"):
        if check.equal(page.button_avto.get_text(), 'Авто'):
            check.equal(page.button_avto.get_attribute('href'),
                        'https://www.dollar.by/catalog/car')
            page.button_avto.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/car')
            check.is_true(page.button_avto.wait_for_visibility())
            check.is_true(page.button_avto.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Электроинструмент'"):
        if check.equal(page.button_elektroinstrument.get_text(), 'Электроинструмент'):
            check.equal(page.button_elektroinstrument.get_attribute('href'),
                        'https://www.dollar.by/catalog/electric-instrument')
            page.button_elektroinstrument.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/electric-instrument')
            check.is_true(page.button_elektroinstrument.wait_for_visibility())
            check.is_true(page.button_elektroinstrument.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Туризм и Отдых'"):
        if check.equal(page.button_turizm_i_otdykh.get_text(), 'Туризм и Отдых'):
            check.equal(page.button_turizm_i_otdykh.get_attribute('href'),
                        'https://www.dollar.by/catalog/turizm')
            page.button_turizm_i_otdykh.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/turizm')
            check.is_true(page.button_turizm_i_otdykh.wait_for_visibility())
            check.is_true(page.button_turizm_i_otdykh.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Все для дома и дачи'"):
        if check.equal(page.button_vse_dlya_doma_i_dachi.get_text(), 'Все для дома и дачи'):
            check.equal(page.button_vse_dlya_doma_i_dachi.get_attribute('href'),
                        'https://www.dollar.by/catalog/vse-dlja-doma-i-dachi')
            page.button_vse_dlya_doma_i_dachi.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/vse-dlja-doma-i-dachi')
            check.is_true(page.button_vse_dlya_doma_i_dachi.wait_for_visibility())
            check.is_true(page.button_vse_dlya_doma_i_dachi.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Все товары для сельского хозяйства: "
                     "теплицы, инкубаторы, кормоцеха'"):
        if check.equal(page.button_vse_dlya_selskogo_khozyaystva.get_text(),
                       'Все для сельского хозяйства'):
            check.equal(page.button_vse_dlya_selskogo_khozyaystva.get_attribute('href'),
                        'https://www.dollar.by/catalog/7936')
            page.button_vse_dlya_selskogo_khozyaystva.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/7936')
            check.is_true(page.button_vse_dlya_selskogo_khozyaystva.wait_for_visibility())
            check.is_true(page.button_vse_dlya_selskogo_khozyaystva.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Микроклиматическая техника'"):
        if check.equal(page.button_mikroklimaticheskaya_tekhnika.get_text(),
                       'Микроклиматическая техника'):
            check.equal(page.button_mikroklimaticheskaya_tekhnika.get_attribute('href'),
                        'https://www.dollar.by/catalog/1565')
            page.button_mikroklimaticheskaya_tekhnika.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/1565')
            check.is_true(page.button_mikroklimaticheskaya_tekhnika.wait_for_visibility())
            check.is_true(page.button_mikroklimaticheskaya_tekhnika.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Сувенирная продукция'"):
        if check.equal(page.button_suvenirnaya_produktsiya.get_text(), 'Сувенирная продукция'):
            check.equal(page.button_suvenirnaya_produktsiya.get_attribute('href'),
                        'https://www.dollar.by/catalog/Suvenirnaya-produktsiya')
            page.button_suvenirnaya_produktsiya.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/Suvenirnaya-produktsiya')
            check.is_true(page.button_suvenirnaya_produktsiya.wait_for_visibility())
            check.is_true(page.button_suvenirnaya_produktsiya.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Все для питомцев'"):
        if check.equal(page.button_vse_dlya_pitomtsev.get_text(), 'Все для питомцев'):
            check.equal(page.button_vse_dlya_pitomtsev.get_attribute('href'),
                        'https://www.dollar.by/catalog/5246')
            page.button_vse_dlya_pitomtsev.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/5246')
            check.is_true(page.button_vse_dlya_pitomtsev.wait_for_visibility())
            check.is_true(page.button_vse_dlya_pitomtsev.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Одежда и обувь'"):
        if check.equal(page.button_odezhda_i_obuv.get_text(), 'Одежда и обувь'):
            check.equal(page.button_odezhda_i_obuv.get_attribute('href'),
                        'https://www.dollar.by/catalog/5675')
            page.button_odezhda_i_obuv.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/5675')
            check.is_true(page.button_odezhda_i_obuv.wait_for_visibility())
            check.is_true(page.button_odezhda_i_obuv.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Стройматериалы'"):
        if check.equal(page.button_stroymaterialy.get_text(), 'Стройматериалы'):
            check.equal(page.button_stroymaterialy.get_attribute('href'),
                        'https://www.dollar.by/catalog/18957')
            page.button_stroymaterialy.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/18957')
            check.is_true(page.button_stroymaterialy.wait_for_visibility())
            check.is_true(page.button_stroymaterialy.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Уценённые товары'"):
        if check.equal(page.button_utsenonnyye_tovary.get_text(), 'Уценённые товары'):
            check.equal(page.button_utsenonnyye_tovary.get_attribute('href'),
                        'https://www.dollar.by/catalog/5386')
            page.button_utsenonnyye_tovary.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/catalog/5386')
            check.is_true(page.button_utsenonnyye_tovary.wait_for_visibility())
            check.is_true(page.button_utsenonnyye_tovary.wait_to_be_clickable())


# <-----------------------------------------Left menu--------------------------------------------->
@allure.feature('Смоук тест')
@allure.story('Имитация скролла в низ экрана и нажатия кнопок Left menu')
def test_left_menu_btn(web_browser):
    """ Убеждаемся, что ссылки/кнопки Left menu
        кликабельные и переход на страницу корректный. """

    page = CatalogBtn(web_browser)

    with allure.step("Проверка кнопки 'Все статьи'"):
        if check.equal(page.button_vse_stati.get_text(), 'Все статьи'):
            check.equal(page.button_vse_stati.get_attribute('href'),
                        'https://www.dollar.by/articles')
            page.button_vse_stati.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/articles')
            check.is_true(page.button_vse_stati.wait_for_visibility())
            check.is_true(page.button_vse_stati.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Все новости'"):
        if check.equal(page.button_vse_novosti.get_text(), 'Все новости'):
            check.equal(page.button_vse_novosti.get_attribute('href'),
                        'https://www.dollar.by/news')
            page.button_vse_novosti.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/news')
            check.is_true(page.button_vse_novosti.wait_for_visibility())
            check.is_true(page.button_vse_novosti.wait_to_be_clickable())


# <--------------------------------------------ПОИСК---------------------------------------------->
@allure.feature('Смоук тест')
@allure.story('Имитация скролла в низ экрана и нажатия кнопок Хедера')
def test_poisk(web_browser):
    """ Убеждаемся, что поиск работает корректно. """

    page = HeaderBtn(web_browser)

    with allure.step("Проверка поля поиска, ввод более трех символов"):
        if check.equal(page.input_poisk.get_attribute('type'),'text'):
            page.input_poisk.click()
            page.input_poisk.send_keys('Кастрюля')
            page.button_poisk.click()
            check.not_equal(page.assert_poisk.count(), 0)

    with allure.step("Проверка поиска по заданному тексту"):
        page.input_poisk.click()
        page.input_poisk.send_keys('Кастрюля')
        page.button_poisk.click()
        if check.not_equal(page.assert_poisk.count(), 0):
            element_text = page.one_tovar.get_text().split()
            text = element_text[0]
            check.equal(text, 'Кастрюля')

    with allure.step("Проверка поля поиска, ввод менее трех символов"):
        if check.equal(page.input_poisk.get_attribute('type'),'text'):
            page.input_poisk.click()
            page.input_poisk.send_keys('А')
            page.button_poisk.click()
            check.equal(page.assert_poisk.count(), 0)

    with allure.step("Проверка поля поиска, ввод трех символов"):
        if check.equal(page.input_poisk.get_attribute('type'),'text'):
            page.input_poisk.click()
            page.input_poisk.send_keys('Кот')
            page.button_poisk.click()
            check.not_equal(page.assert_poisk.count(), 0)


# <-------------------------------------Домашняя страница----------------------------------------->
@allure.feature('Смоук тест')
@allure.story('Имитация скролла в низ экрана и нажатия кнопок слайдера')
def test_home_slider(web_browser):
    """ Убеждаемся, что кнопки слайдера
        кликабельные и переход слайдов корректный. """

    page = HomeBtn(web_browser)

    with allure.step("Проверка кнопок слайдера"):
        check.is_true(page.slider_1.wait_for_visibility())
        check.is_true(page.slider_1.wait_to_be_clickable())
        check.is_true(page.slider_1.is_enabled())
        page.slider_2.click()
        check.is_true(page.slider_2.wait_for_visibility())
        check.is_true(page.slider_2.wait_to_be_clickable())
        check.is_true(page.slider_2.is_enabled())
        page.slider_3.click()
        check.is_true(page.slider_3.wait_for_visibility())
        check.is_true(page.slider_3.wait_to_be_clickable())
        check.is_true(page.slider_3.is_enabled())
        page.slider_4.click()
        check.is_true(page.slider_4.wait_for_visibility())
        check.is_true(page.slider_4.wait_to_be_clickable())
        check.is_true(page.slider_4.is_enabled())
        page.slider_5.click()
        check.is_true(page.slider_5.wait_for_visibility())
        check.is_true(page.slider_5.wait_to_be_clickable())
        check.is_true(page.slider_5.is_enabled())


@allure.feature('Смоук тест')
@allure.story('Имитация скролла в низ экрана и нажатия кнопок слайдера')
def test_home_korzina(web_browser):
    """ Убеждаемся, что добавленный товар отображается
        количество и сумма """

    page = HomeBtn(web_browser)

    with allure.step("Проверка кнопки 'Добавить в корзину' и отображения товара в корзине."):
        if check.equal(page.button_dobavit_v_korzinu.get_text(), 'В корзину'):
            check.equal(page.button_dobavit_v_korzinu.get_attribute('title'),
                            'Добавить в корзину')
            check.is_true(page.button_dobavit_v_korzinu.wait_for_visibility())
            check.is_true(page.button_dobavit_v_korzinu.wait_to_be_clickable())
            page.button_dobavit_v_korzinu.click()
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/shopcart')
            check.not_equal(page.koll_tovara.get_text(), '0')
            check.not_equal(page.sum_tovara.get_text(), '0')
            page.go_back()
            page.scroll_up()
            check.greater(page.home_koll_tovarov.get_text(), '0')
            check.greater(page.home_sum_tovarov.get_text(), '0')


@allure.feature('Смоук тест')
@allure.story('Имитация скролла в низ экрана и нажатия кнопоки заказать')
def test_home_zakazat(web_browser):
    """ Убеждаемся, что ссылка/кнопка заказать
        кликабельные и переход на страницу корректный. """

    page = HomeBtn(web_browser)

    with allure.step("Проверка кнопки 'Заказать'"):
        if check.equal(page.button_zakazat.get_text(), 'Заказать'):
            check.is_true(page.button_zakazat.wait_for_visibility())
            check.is_true(page.button_zakazat.wait_to_be_clickable())
            page.button_zakazat.click()
            check.equal(page.assert_zakazati_okno.get_text(), 'Заполните форму заказа')


@allure.feature('Смоук тест')
@allure.story('Имитация скролла в низ экрана и нажатия кнопоки заказать')
def test_home_zakazat_form(web_browser):
    """ Убеждаемся, что форма заказать работает корректно. """

    page = HomeBtn(web_browser)

    with allure.step("Заполнение формы заказать'"):
        if check.equal(page.button_zakazat.get_text(), 'Заказать'):
            page.button_zakazat.click()
            check.equal(page.assert_zakazati_okno.get_text(), 'Заполните форму заказа')
            page.name_form.send_keys('Andrew')
            page.numbers.send_keys('999999999')
            check.is_true(page.btn_zakazat.wait_for_visibility())
            check.is_true(page.btn_zakazat.wait_to_be_clickable())
            page.btn_zakazat.click()
            check.equal(page.assert_zakazati.get_text(), 'Спасибо! Ваш заказ принят!')


# <----------------------------------------КОРЗИНА------------------------------------------------>
@allure.feature('Смоук тест')
@allure.story('Проверка формы заказа в корзине')
def test_korzina_form(web_browser):
    """ Убеждаемся, что форма заказа заполняется и отсылается """

    page = HomeBtn(web_browser)

    with allure.step("Проверка формы заказа товара через корзину"):
        if check.equal(page.button_dobavit_v_korzinu.get_text(), 'В корзину'):
            check.equal(page.button_dobavit_v_korzinu.get_attribute('title'),
                        'Добавить в корзину')
            check.is_true(page.button_dobavit_v_korzinu.wait_for_visibility())
            check.is_true(page.button_dobavit_v_korzinu.wait_to_be_clickable())
            tovar = page.assert_tovar.get_text()
            page.button_dobavit_v_korzinu.click()
            check.is_true(page.button_info.wait_for_visibility())
            check.is_true(page.button_info.wait_to_be_clickable())
            page.button_info.click()
            check.equal(page.assert_info.get_text(), 'Для оформления заказа заполните пожалуйста форму с контактными данными НИЖЕ.')
            check.equal(tovar, page.assert_tovar_korzina.get_text())
            page.button_samovyvoz.click()
            check.is_true(page.button_samovyvoz.is_selected())
            page.button_dostavka.click()
            check.is_true(page.button_dostavka.is_selected())
            page.button_belpochta.click()
            check.is_true(page.button_belpochta.is_selected())
            page.button_cards.click()
            check.is_true(page.button_cards.is_selected())
            page.button_nalichnymi.click()
            check.is_true(page.button_nalichnymi.is_selected())
            page.input_name.send_keys('Alexey')
            page.input_number.send_keys('999999999')
            page.input_adress.send_keys('Minsk')
            page.input_comment.send_keys('Thanks')
            time.sleep(4)
            page.button_person_inf.click()
            check.is_true(page.button_person_inf.is_selected())
            check.is_true(page.button_podtverdit_zakaz.wait_for_visibility())
            check.is_true(page.button_podtverdit_zakaz.wait_to_be_clickable())
            check.equal(page.button_podtverdit_zakaz.get_attribute('value'), 'Подтвердить заказ')
            page.button_podtverdit_zakaz.click()
            check.equal(page.assert_vash_zakaz.get_text(), 'Благодарим Вас за заказ!')


@allure.feature('Смоук тест')
@allure.story('Проверка формы заказа в корзине')
def test_korzina_form_2(web_browser):
    """ Убеждаемся, что сумма изменяется в зависимости от смены параметров """

    page = HomeBtn(web_browser)

    with allure.step("Проверка параметров при заказе товара"):
        if check.equal(page.button_dobavit_v_korzinu.get_text(), 'В корзину'):
            check.equal(page.button_dobavit_v_korzinu.get_attribute('title'),
                        'Добавить в корзину')
            page.button_dobavit_v_korzinu.click()
            page.button_samovyvoz.click()
            check.equal(page.assert_price.get_text_index()[0],
                        page.assert_itogo.get_text_index()[0])
            check.equal(page.assert_itogo.get_text_index()[0],
                        page.assert_koll_header.get_text_index()[0])
            page.button_dostavka.click()
            check.equal(page.assert_itogo.get_text_index()[0],
                        page.assert_koll_header.get_text_index()[0])
            page.button_belpochta.click()
            check.equal(page.assert_itogo.get_text_index()[0],
                        page.assert_koll_header.get_text_index()[0])
            page.button_samovyvoz.click()
            page.assert_koll.send_keys("2")
            check.equal(page.assert_itogo.get_text_index()[0],
                        page.assert_koll_header.get_text_index()[0])


@allure.feature('Смоук тест')
@allure.story('Удаление из корзины товара')
def test_korzina_delet(web_browser):
    """ Убеждаемся, что товар удаляется с корзины """

    page = HomeBtn(web_browser)

    with allure.step("Удалить товар с корзины"):
        if check.equal(page.button_dobavit_v_korzinu.get_text(), 'В корзину'):
            page.button_dobavit_v_korzinu.click()
            check.is_true(page.button_delet.wait_for_visibility())
            check.is_true(page.button_delet.wait_to_be_clickable())
            page.button_delet.click()
            check.equal(page.assert_delet.get_text(), 'В Вашей корзине еще нет товаров.')



