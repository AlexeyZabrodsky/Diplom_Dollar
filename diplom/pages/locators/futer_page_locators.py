import os
from diplom.pages.base_page import WebPage
from diplom.pages.elements import WebElement
from diplom.pages.elements import ManyWebElements


class FuterBtn(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("FUTER") or 'https://www.dollar.by/'

        super().__init__(web_driver, url)

    button_glavnaya_foot = WebElement(css_selector='div.footer__menu__item [title="Главная"]')
    button_novosti_foot = WebElement(css_selector='div.footer__menu__item [title="Новости"]')
    button_stati_foot = WebElement(css_selector='div.footer__menu__item [title="Статьи"]')
    button_o_magazine_foot = WebElement(css_selector='div.footer__menu__item [title="О магазине"]')
    button_dostavka_i_oplata_foot = WebElement(css_selector='div.footer__menu__item '
                                                        '[title="Доставка и оплата"]')
    button_kontakty_foot = WebElement(css_selector='div.footer__menu__item [title="Контакты"]')
    inst_foot = WebElement(css_selector='div.footer__social_links a:nth-of-type(1)')
    face_foot = WebElement(css_selector='div.footer__social_links a:nth-of-type(2)')
    vk_foot = WebElement(css_selector='div.footer__social_links a:nth-of-type(3)')