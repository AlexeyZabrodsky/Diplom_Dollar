import time
from termcolor import colored
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class WebElement(object):
    _locator = ('', '')
    _web_driver = None
    _page = None
    _timeout = 10
    _wait_after_click = False

    def __init__(self, timeout=10, wait_after_click=False, **kwargs):
        self._timeout = timeout
        self._wait_after_click = wait_after_click

        for attr in kwargs:
            self._locator = (str(attr).replace('_', ' '), str(kwargs.get(attr)))

    def find(self, timeout=10):
        """ Найти элемент на странице. """

        element = None

        try:
            element = WebDriverWait(self._web_driver, timeout).until(
                EC.presence_of_element_located(self._locator)
            )
        except:
            print(colored('Element not found on the page!', 'red'))

        return element

    def wait_to_be_clickable(self, timeout=10, check_visibility=True):
        """ Подождите, пока элемент будет готов к клику. """

        element = None

        try:
            element = WebDriverWait(self._web_driver, timeout).until(
                EC.element_to_be_clickable(self._locator)
            )
        except:
            print(colored('Element not clickable!', 'red'))

        if check_visibility:
            self.wait_until_not_visible()

        return element

    def wait_for_visibility(self, timeout=10):
        """ Подождите, пока элемент не станет видимым на странице. """

        element = None

        try:
            element = WebDriverWait(self._web_driver, timeout).until(
                EC.visibility_of_element_located(self._locator)
            )
        except:
            print(colored('Element not visible!', 'red'))

        return element

    def wait_for_clickability_and_visibility(self, timeout=10):
        """ Подождите, пока элемент не станет видимым на странице и не будет готов к клику. """

        element = None

        try:
            element = WebDriverWait(self._web_driver, timeout).until(
                EC.element_to_be_clickable(self._locator) and EC.visibility_of_element_located(self._locator)
            )
        except:
            print(colored('Element not clickable and visible!', 'red'))

        return element

    def is_clickable(self):
        """ Проверить, готов ли элемент к клику или нет. """

        element = self.wait_to_be_clickable(timeout=1)
        return element is not None

    def is_presented(self):
        """ Убедитесь, что элемент представлен на странице. """

        element = self.find(timeout=1)
        return element is not None

    def is_visible(self):
        """ Проверить, виден элемент или нет. """

        element = self.find(timeout=1)

        if element:
            return element.is_displayed()

        return False

    def is_selected(self) -> bool:
        """Возвращает результат, выбран ли элемент.
        Может использоваться для проверки установлен ли флажок или переключатель.
        """

        element = self.find(timeout=1)

        if element:
            return element.is_selected()

        return False

    def is_enabled(self) -> bool:
        """Проверка, активна ли кнопка слайдера"""

        element = self.find(timeout=1)

        if element:
            return element.is_enabled()

        return False

    def wait_until_not_visible(self, timeout=10):

        element = None

        try:
            element = WebDriverWait(self._web_driver, timeout).until(
                EC.visibility_of_element_located(self._locator)
            )
        except:
            print(colored('Element not visible!', 'red'))

        if element:
            js = ('return (!(arguments[0].offsetParent === null) && '
                  '!(window.getComputedStyle(arguments[0]) === "none") &&'
                  'arguments[0].offsetWidth > 0 && arguments[0].offsetHeight > 0'
                  ');')
            visibility = self._web_driver.execute_script(js, element)
            iteration = 0

            while not visibility and iteration < 10:
                time.sleep(0.5)

                iteration += 1

                visibility = self._web_driver.execute_script(js, element)
                print('Element {0} visibility: {1}'.format(self._locator, visibility))

        return element

    def wait_for_invisibility(self, timeout=15):
        """ Подождите, пока элемент не перестанет быть видимым на странице. """

        try:
            element = WebDriverWait(self._web_driver, timeout).until(
                EC.invisibility_of_element_located(self._locator)
            )
        except:
            print(colored('Element still visible!', 'red'))
            return None

        return element

    def send_keys(self, keys, wait=2):
        """ Отправить ключи к элементу. """

        keys = keys.replace('\n', '\ue007')

        element = self.find()

        if element:
            element.click()
            element.clear()
            element.send_keys(keys)
            time.sleep(wait)
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))

    def send_keys_all_select(self, keys, wait=2):
        """ Отправить ключи к элементу второй вариант. """

        keys = keys.replace('\n', '\ue007')

        element = self.find()

        if element:
            element.click()
            element.send_keys(Keys.CONTROL + 'a')
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(keys)
            time.sleep(wait)
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))

    def get_text(self):
        """ Получить текст элемента. """

        element = self.find()
        text = ''

        try:
            text = str(element.text)
        except Exception as e:
            print('Error: {0}'.format(e))

        return text

    def get_text_index(self):
        """ Получить текст по индексу. """

        element = self.find()
        text = ''

        try:
            text = tuple(element.text.split())
        except Exception as e:
            print('Error: {0}'.format(e))

        return text

    def get_text_str(self):
        """ Получить текст по индексу. """

        element = self.find()
        text = []

        try:
            text = str(element.text.split())
        except Exception as e:
            print('Error: {0}'.format(e))

        return text

    def get_attribute(self, attr_name):
        """ Получить атрибут элемента. """

        element = self.find()

        if element:
            return element.get_attribute(attr_name)

    def _set_value(self, web_driver, value, clear=True):
        """ Установить значение для элемента ввода. """

        element = self.find()

        if clear:
            element.clear()

        element.send_keys(value)

    def click(self, hold_seconds=0, x_offset=1, y_offset=1):
        """ Подождать и кликнуть по элементу. """

        element = self.wait_to_be_clickable()

        if element:
            action = ActionChains(self._web_driver)
            action.move_to_element_with_offset(element, x_offset, y_offset). \
                pause(hold_seconds).click(on_element=element).perform()
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))

        if self._wait_after_click:
            self._page.wait_page_loaded()

    def doubleclick(self, hold_seconds=0, x_offset=1, y_offset=1):
        """ Подождать и кликнуть дважды по элементу. """

        element = self.wait_to_be_clickable()

        if element:
            action = ActionChains(self._web_driver)
            action.move_to_element_with_offset(element, x_offset, y_offset). \
                pause(hold_seconds).double_click(on_element=element).perform()
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))

        if self._wait_after_click:
            self._page.wait_page_loaded()

    def right_mouse_click(self, x_offset=0, y_offset=0, hold_seconds=0):
        """ Кликнуть правой кнопкой мыши по элементу. """

        element = self.wait_to_be_clickable()

        if element:
            action = ActionChains(self._web_driver)
            action.move_to_element_with_offset(element, x_offset, y_offset). \
                pause(hold_seconds).context_click(on_element=element).perform()
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))

    def click_new_tab(self, x_offset=0, y_offset=0, hold_seconds=0):
        """ Кликнуть правой кнопкой мыши по элементу. """

        element = self.wait_to_be_clickable()

        if element:
            action = ActionChains(self._web_driver)
            action.key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))

    def move_to(self, x_offset=0, y_offset=0, hold_seconds=0):
        """ Наведение мышки на элемент без клика """

        element = self.find()

        if element:
            action = ActionChains(self._web_driver)
            action.move_to_element_with_offset(element, x_offset, y_offset). \
                pause(hold_seconds).pause(1).perform()
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))

    def highlight_and_make_screenshot(self, file_name='element.png'):
        """ Выделить элемент и сделайте скриншот всей страницы. """

        element = self.find()

        # Прокрутить страницу до элемента:
        try:
            element.send_keys(Keys.DOWN)
        except Exception as e:
            pass  # Просто игнорирует ошибку, если мы не можем отправить ключи к элементу

        # Добавьте красную рамку к стилю:
        self._web_driver.execute_script("arguments[0].style.border='3px solid red'", element)

        # Сделать скриншот страницы:
        self._web_driver.save_screenshot(file_name)

    def scroll_to_element(self):
        """ Прокрутить страницу до элемента. """

        element = self.find()

        # Option #2 для прокрутки до элемента:
        try:
            element.send_keys(Keys.DOWN)
        except Exception as e:
            pass  # Просто игнорирует ошибку, если мы не можем отправить ключи к элементу


    def scroll_to_element_2(self):
        """ Прокрутить страницу до элемента. """

        element = self.find()

        # # Прокрутить страницу до элемента:
        # Option #1 для прокрутки до элемента:
        self._web_driver.execute_script("arguments[0].scrollIntoView();", element)


    def scroll_to_element_3(self):
        """ Прокрутить страницу до элемента. """

        element = self.find()

        # Option #3 для прокрутки до элемента:
        # Получаем высоту экрана
        screen_height = self._web_driver.execute_script("return window.innerHeight")

        # Получаем координаты элемента
        location = element.location_once_scrolled_into_view

        # Вычисляем, насколько нужно прокрутить страницу, чтобы элемент оказался по центру экрана
        scroll_offset = location['y'] - screen_height / 3

        # Прокручиваем страницу
        self._web_driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_offset)


    def delete(self):
        """ Удаляет элемент со страницы. """

        element = self.find()

        # Удаляет элемент:
        self._web_driver.execute_script("arguments[0].remove();", element)


class ManyWebElements(WebElement):

    def __getitem__(self, item):
        """ Получить список элементов и попытаться вернуть требуемый элемент. """

        elements = self.find()
        return elements[item]

    def find(self, timeout=10):
        """ Поиск элементов на странице. """

        elements = []

        try:
            elements = WebDriverWait(self._web_driver, timeout).until(
                EC.presence_of_all_elements_located(self._locator)
            )
        except:
            print(colored('Elements not found on the page!', 'red'))

        return elements

    def set_value(self, web_driver, value):
        """ Примечание: это действие не применимо к списку элементов. """
        raise NotImplemented('This action is not applicable for the list of elements')

    def click(self, hold_seconds=0, x_offset=0, y_offset=0):
        """ Примечание: это действие не применимо к списку элементов. """
        raise NotImplemented('This action is not applicable for the list of elements')

    def count(self):
        """ Получить количество элементов. """

        elements = self.find()
        el = len(elements)
        return el

    def get_text(self):
        """ Получить текст элементов. """

        elements = self.find()
        result = []

        for element in elements:
            text = ''

            try:
                text = str(element.text)
            except Exception as e:
                print('Error: {0}'.format(e))

            result.append(text)

        return result

    def get_attribute(self, attr_name):
        """ Получить атрибут всех элементов. """

        results = []
        elements = self.find()

        for element in elements:
            results.append(element.get_attribute(attr_name))

        return results

    def highlight_and_make_screenshot(self, file_name='element.png'):
        """ Выделите элементы и сделайте скриншот всей страницы. """

        elements = self.find()

        for element in elements:
            # Прокрутить страницу до элемента:
            self._web_driver.execute_script("arguments[0].scrollIntoView();", element)

            # Добавьте красную рамку к стилю:
            self._web_driver.execute_script("arguments[0].style.border='3px solid red'", element)

        # Сделать скриншот страницы:
        self._web_driver.save_screenshot(file_name)
