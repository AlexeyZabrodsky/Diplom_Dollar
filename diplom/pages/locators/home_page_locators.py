import os
from diplom.pages.base_page import WebPage
from diplom.pages.elements import WebElement
from diplom.pages.elements import ManyWebElements


class HomeBtn(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("HOME") or 'https://www.dollar.by/'

        super().__init__(web_driver, url)

    slider_1 = WebElement(css_selector='div.owl-dots button:nth-of-type(1)')
    slider_2 = WebElement(css_selector='div.owl-dots button:nth-of-type(2)')
    slider_3 = WebElement(css_selector='div.owl-dots button:nth-of-type(3)')
    slider_4 = WebElement(css_selector='div.owl-dots button:nth-of-type(4)')
    slider_5 = WebElement(css_selector='div.owl-dots button:nth-of-type(5)')
    button_zakazat = WebElement(css_selector='[class="teaser__catitem__list"] '
                                             'div.teaser__catitem:nth-of-type(1) div#id__buy__fast')
    button_dobavit_v_korzinu = WebElement(css_selector='[class="teaser__catitem__list"] '
                                                       'div.teaser__catitem:nth-of-type(1) '
                                                       'a#id__add__to__cart')
    koll_tovara = WebElement(css_selector='div.header div.header__shopcart__count')
    sum_tovara = WebElement(css_selector='div.header div.header__shopcart__price')
    home_koll_tovarov = WebElement(css_selector='div.header__wrapper div.header__shopcart__count')
    home_sum_tovarov = WebElement(css_selector='div.header__wrapper '
                                               'div.header__shopcart__price span')
    assert_zakazati_okno = WebElement(css_selector='div.modal__window__title')
# <------Форма заказать--------->
    name_form = WebElement(css_selector='input#id_page_20660-field_0')
    numbers = WebElement(css_selector='input#id_page_20660-field_1')
    btn_zakazat = WebElement(css_selector='button#id__add___field__offer__request__send')
    assert_zakazati = WebElement(css_selector='div.modal__window__title')

# <-------КОРЗИНА--------------->
    slider_home = WebElement(css_selector='div.block__slider_and_day_offer__slider')
    button_info = WebElement(css_selector='div.page__shopcart__delivery_info__title__wrapper')
    assert_info = WebElement(css_selector='div.page__shopcart__delivery_info__body__wrapper '
                                          'p:nth-of-type(1)')
    button_delet = WebElement(css_selector='td.page__shopcart__table__body__tools a')
    assert_delet = WebElement(css_selector='div.main__content__body>div>p')
    button_samovyvoz = WebElement(css_selector='div.page__shopcart__table__wrapper '
                                               'input#id_delivery_0')
    button_dostavka = WebElement(css_selector='div.page__shopcart__table__wrapper '
                                              'input#id_delivery_1')
    button_belpochta = WebElement(css_selector='div.page__shopcart__table__wrapper '
                                               'input#id_delivery_2')

    button_nalichnymi = WebElement(css_selector='div.form__item.radio div:nth-of-type(1) input')
    button_cards = WebElement(css_selector='div.form__item.radio div:nth-of-type(2) input')

    # <---Форма заполнения данных--->
    input_name = WebElement(css_selector='input#id_first_name')
    input_number = WebElement(css_selector='input#id_phone')
    input_adress = WebElement(css_selector='input#id_delivery_address')
    input_comment = WebElement(css_selector='textarea#id_comment')
    button_person_inf = WebElement(css_selector='input#id_i_agree')
    button_podtverdit_zakaz = WebElement(css_selector='input#id__submit__an__order')
    assert_vash_zakaz = WebElement(css_selector='div.thank')
    # <---Проверка товара с корзиной--->
    assert_tovar = WebElement(xpath="(//div[@class='block__offers_after_slider_on_main']"
                                    "//div[@page_id='20145']//a)[1]")
    assert_tovar_korzina = WebElement(css_selector='td.page__shopcart__table__body__title a')
    # <---Проверка cуммы товара--->
    assert_itogo = WebElement(css_selector='tfoot.page__shopcart__table__footer td:nth-of-type(3)')
    assert_price = WebElement(css_selector='tr.cart-order td.page__shopcart__table__body__price')
    assert_koll = WebElement(css_selector='div.form-item.form-item-quantity input')
    assert_koll_header = WebElement(css_selector='div.header div.header__shopcart__price')
    # <---Проверка формы оставить отзыв--->
    slider_tovar = WebElement(css_selector='div.teaser__catitem.teaser__catitem__day_product'
                                           '>div>div>div:nth-of-type(4) a')
    dobavit_otziv = WebElement(css_selector='span.expand-review-form')
    name_otziv = WebElement(css_selector='input#id_review-username')
    title_otziv = WebElement(css_selector='[name="review-text"]')
    ball_otziv = WebElement(css_selector='select#id_review-rating')
    text_otziv_span = WebElement(css_selector='span.captcha-question')
    otpravit_otziv = WebElement(css_selector='div.form__item.form__button > input')
