import os
from diplom.pages.base_page import WebPage
from diplom.pages.elements import WebElement
from diplom.pages.elements import ManyWebElements


class CatalogBtn(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("CATALOG") or 'https://www.dollar.by/'

        super().__init__(web_driver, url)

    # <---Menu left--->
    button_novinki = WebElement(css_selector='div.menu_catalog [data-id="19860"] a')
    button_podarochnyye_nabory = WebElement(css_selector='div.menu_catalog [data-id="21347"] a')
    button_rasprodazha = WebElement(css_selector='div.menu_catalog [data-id="7189"] a')
    button_podarki_dlya_zhenshchin = WebElement(css_selector='div.menu_catalog [data-id="20080"] a')
    button_profitable_proposition = WebElement(css_selector='div.menu_catalog [data-id="19556"] a')
    button_podarki_dlya_muzhchin = WebElement(css_selector='div.menu_catalog [data-id="18274"] a')
    button_vesenniye_skidki = WebElement(css_selector='div.menu_catalog [data-id="18275"] a')
    button_novogodniye_tovary = WebElement(css_selector='div.menu_catalog [data-id="5436"] a')
    button_tovary_dlya_shkoly = WebElement(css_selector='div.menu_catalog [data-id="17740"] a')
    button_tovary_dlya_kukhni = WebElement(css_selector='div.menu_catalog [data-id="766"] a')
    button_tovary_dlya_doma = WebElement(css_selector='div.menu_catalog [data-id="943"] a')
    button_sportivnyye_tovary = WebElement(css_selector='div.menu_catalog [data-id="954"] a')
    button_krasota_i_zdorovye = WebElement(css_selector='div.menu_catalog [data-id="959"] a')
    button_sumki_klatchi_ryukzaki = WebElement(css_selector='div.menu_catalog [data-id="18931"] a')
    button_gadzhety = WebElement(css_selector='div.menu_catalog [data-id="965"] a')
    button_detskiy_mir = WebElement(css_selector='div.menu_catalog [data-id="969"] a')
    button_podarki = WebElement(css_selector='div.menu_catalog [data-id="976"] a')
    button_avto = WebElement(css_selector='div.menu_catalog [data-id="981"] a')
    button_elektroinstrument = WebElement(css_selector='div.menu_catalog [data-id="984"] a')
    button_turizm_i_otdykh = WebElement(css_selector='div.menu_catalog [data-id="735"] a')
    button_vse_dlya_doma_i_dachi = WebElement(css_selector='div.menu_catalog [data-id="734"] a')
    button_vse_dlya_selskogo_khozyaystva = WebElement(css_selector='div.menu_catalog '
                                                                   '[data-id="7936"] a')
    button_mikroklimaticheskaya_tekhnika = WebElement(css_selector='div.menu_catalog '
                                                                   '[data-id="1565"] a')
    button_suvenirnaya_produktsiya = WebElement(css_selector='div.menu_catalog [data-id="2277"] a')
    button_vse_dlya_pitomtsev = WebElement(css_selector='div.menu_catalog [data-id="5246"] a')
    button_odezhda_i_obuv = WebElement(css_selector='div.menu_catalog [data-id="5675"] a')
    button_stroymaterialy = WebElement(css_selector='div.menu_catalog [data-id="18957"] a')
    button_utsenonnyye_tovary = WebElement(css_selector='div.menu_catalog [data-id="5386"] a')
    button_vse_stati = WebElement(css_selector='div.main__left_side '
                                               'div.block__articles__read_more a')
    button_vse_novosti = WebElement(css_selector='div.main__left_side div.block__news__read_more a')

    # <---MENU in MENU--->
    # <---РАСПРОДАЖА--->
    rasprodazha_osen = WebElement(css_selector='[data-id="21136"] a')
    # <---НОВОГОДНИЕ ТОВАРЫ--->
    rasprodazha_novogodnikh_tovarov = WebElement(css_selector='[data-id="20140"] a')
    novogodniye_derevya = WebElement(css_selector='[data-id="5437"] a')
    girlyandy_i_venki = WebElement(css_selector='[data-id="7451"] a')
    yeli_i_sosny = WebElement(css_selector='[data-id="7452"] a')
    igrushki_statuetki = WebElement(css_selector='[data-id="7496"] a')
    # <---ТОВАРЫ ДЛЯ КУХНИ--->
    rasprodazha_kukhni = WebElement(css_selector='[data-id="20141"] a')
    nabory_posudy = WebElement(css_selector='[data-id="767"] a')
    kastryuli = WebElement(css_selector='[data-id="931"] a')
    kukhonnyye_stolovyye = WebElement(css_selector='[data-id="936"] a')
    terki_ovoshcherezki = WebElement(css_selector='[data-id="937"] a')
    nabory_nozhey = WebElement(css_selector='[data-id="938"] a')
    dlya_zatochki_nozhey = WebElement(css_selector='[data-id="5181"] a')
    skovorody = WebElement(css_selector='[data-id="939"] a')
    mantovarki = WebElement(css_selector='[data-id="942"] a')
    sokovyzhimalki = WebElement(css_selector='[data-id="1139"] a')
    termosy = WebElement(css_selector='[data-id="2237"] a')
    nozhi_keramicheskiye = WebElement(css_selector='[data-id="2243"] a')
    posuda_pensofal = WebElement(css_selector='[data-id="2546"] a')
    cokovarki = WebElement(css_selector='[data-id="4775"] a')
    formy_dlya_vypechki = WebElement(css_selector='[data-id="4858"] a')
    sushilki_dlya_ovoshchey = WebElement(css_selector='[data-id="5074"] a')
    vakuumnyye_konteynery = WebElement(css_selector='[data-id="5162"] a')
    apparaty_popkorna = WebElement(css_selector='[data-id="5237"] a')
    apparaty_sakharnoy_vaty = WebElement(css_selector='[data-id="5239"] a')
    # <---ТОВАРЫ ДЛЯ ДОМА--->
    neobychnyye_svetilniki = WebElement(css_selector='[data-id="1284"] a')
    bytovaya_tekhnika = WebElement(css_selector='[data-id="944"] a')
    ventilyatory = WebElement(css_selector='[data-id="945"] a')
    obogrevateli = WebElement(css_selector='[data-id="946"] a')
    aerogrili = WebElement(css_selector='[data-id="947"] a')
    blendery_miksery = WebElement(css_selector='[data-id="948"] a')
    mashinki_odezhdoy = WebElement(css_selector='[data-id="952"] a')
    paroochistiteli = WebElement(css_selector='[data-id="1159"] a')
    pylesosy = WebElement(css_selector='[data-id="2251"] a')
    utyugi = WebElement(css_selector='[data-id="2255"] a')
    elektrochayniki = WebElement(css_selector='[data-id="2285"] a')
    uvlazhniteli_vozdukha = WebElement(css_selector='[data-id="5928"] a')
    incubators = WebElement(css_selector='[data-id="8123"] a')
    elektricheskiye_kotly = WebElement(css_selector='[data-id="20370"] a')
    otpugivateli = WebElement(css_selector='[data-id="1005"] a')
    otpugivateli_zhivotnykh = WebElement(css_selector='[data-id="20627"] a')
    otpugivateli_ptits = WebElement(css_selector='[data-id="20628"] a')
    otpugivateli_krotov = WebElement(css_selector='[data-id="20633"] a')
    otpugivateli_komarov = WebElement(css_selector='[data-id="20634"] a')
    tovary_dly_auborki = WebElement(css_selector='[data-id="1006"] a')
    sushilki_dlya_obuvi = WebElement(css_selector='[data-id="1007"] a')
    besprovodnyye_zvonki = WebElement(css_selector='[data-id="7629"] a')
    vesy = WebElement(css_selector='[data-id="2245"] a')
    dlya_ukhoda_za_obuvyu = WebElement(css_selector='[data-id="19432"] a')
    mashinki_dlya_katyshek = WebElement(css_selector='[data-id="1117"] a')
    planetarii = WebElement(css_selector='[data-id="7850"] a')
    signalizacia = WebElement(css_selector='[data-id="7712"] a')
    sumki_telechki_rykzaki = WebElement(css_selector='[data-id="7981"] a')
    rykzaki = WebElement(css_selector='[data-id="7982"] a')
    sumki = WebElement(css_selector='[data-id="7985"] a')
    tovary_dlya_remonta = WebElement(css_selector='[data-id="7558"] a')
    tovary_dlya_kozhey = WebElement(css_selector='[data-id="5943"] a')
    umnyye_lampochki = WebElement(css_selector='[data-id="11920"] a')
    shveynyye_mashiny = WebElement(css_selector='[data-id="1146"] a')
    rasprodazha_dlya_doma = WebElement(css_selector='[data-id="20142"] a')
