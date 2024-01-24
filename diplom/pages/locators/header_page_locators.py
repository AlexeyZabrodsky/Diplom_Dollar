import os
from diplom.pages.base_page import WebPage
from diplom.pages.elements import WebElement
from diplom.pages.elements import ManyWebElements


class HeaderBtn(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("HEADER") or 'https://www.dollar.by/'

        super().__init__(web_driver, url)

# <--Header-->
    button_o_magazine = WebElement(css_selector='div.header__menu__item:nth-of-type(1) a')
    button_dostavka_i_oplata = WebElement(css_selector='div.header__menu__item:nth-of-type(2) a')
    button_garantiya = WebElement(css_selector='div.header__menu__item:nth-of-type(3) a')
    button_instagram = WebElement(css_selector='div.header div.header__social_links a:nth-of-type(1)')
    button_facebook = WebElement(css_selector='div.header div.header__social_links a:nth-of-type(2)')
    button_vk = WebElement(css_selector='div.header div.header__social_links a:nth-of-type(3)')
    button_logo = WebElement(xpath='//div[@class="header__logo__image"]/a')
    button_korzina = WebElement(css_selector='div.header__wrapper a#id__header__shopcart__title__link')
    input_poisk = WebElement(css_selector='div.header__search input.top-search-input')
    button_poisk = WebElement(css_selector='div.header__search button#id__top__search__button')
    button_viber = WebElement(css_selector='div.header div.block__phone__social__item.viber a')
    button_watsapp = WebElement(css_selector='div.header div.block__phone__social__item.watsapp a')
    button_telegram = WebElement(css_selector='div.header div.block__phone__social__item.telegram a')
    number_A1 = WebElement(css_selector='div.header a#id__header_phone_velcom')
    number_mts = WebElement(css_selector='div.header a#id__header_phone_mts')
    number_city = WebElement(css_selector='div.header a#id__header_phone_city')

# <--mini-header-->
    button_korzina_mini = WebElement(css_selector='div.mobile__navbar.active '
                                                  'a#id__header__shopcart__title__link')
    input_poisk_mini = WebElement(css_selector='div.mobile__navbar__search input.top-search-input')
    button_poisk_mini = WebElement(css_selector='div.mobile__navbar.active '
                                                'button#id__top__search__button')
    button_logo_mini = WebElement(css_selector='div.mobile__navbar__logo a')
    button_info_mini = WebElement(css_selector='div.header__phones')
    number_A1_mini = WebElement(css_selector='div.mobile__navbar.active div.header__phones>div:nth-of-type(1) a')
    number_mts_mini = WebElement(css_selector='div.mobile__navbar.active div.header__phones>div:nth-of-type(2) a')
    number_city_mini = WebElement(css_selector='div.mobile__navbar.active div.header__phones>div:nth-of-type(3) a')

# assert poisk
    assert_poisk = ManyWebElements(css_selector='div.page__search__items>div')
    one_tovar = WebElement(css_selector='div.page__search__items>div:nth-of-type(1) '
                                        'div.page__search__item__title a')
