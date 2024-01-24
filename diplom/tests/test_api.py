import requests
import allure
import pytest_check as check
import time
import json


@allure.suite("Test API")
@allure.story("Test API")
@allure.description("Пишем тесты для метода GET")
@allure.tag("API", "GET")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "maksim tsybulko")
@allure.link("https://dev.example.com/", name="Website_1")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
def test_api_1():
    url = "https://www.dollar.by/"

    payload = {}
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    time_start = time.time()

    response = requests.request("GET", url, headers=headers, data=payload)

    time_end = time.time()
    time_loud = time_end - time_start

    with allure.step('Проверка статус кода '):
        check.greater_equal(1, time_loud)

    with allure.step('Проверка статус кода '):
        check.equal(response.status_code, 200, 'Неверый статус код')

    with allure.step('Проверка времени ответа страницы'):
        check.greater_equal(time_loud, 0, 'Неверый статус код')

    with allure.step('Проверка наличия Content-Type в headers'):
        check.is_in(response.headers["Content-Type"], "text/html; charset=utf-8")

    with allure.step('Добавить attuch'):
        allure.attach('Remove error', response.text, attachment_type=allure.attachment_type.TEXT)

    with allure.step('Проверка,что метод GET'):
        print(response.request.method)
        check.not_equal(response.request.method, 'POST')


@allure.suite("Test API")
@allure.story("Test API")
@allure.description("Пишем тесты для метода POST")
@allure.tag("API", "POST")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "maksim tsybulko")
@allure.link("https://dev.example.com/", name="Website_1")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
def test_api_2():
    url = "https://catalog.onliner.by/api/seo"

    payload = json.dumps({
        "test": "test"
    })
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',

    }

    response = requests.request("POST", url, headers=headers, data=payload)

    with allure.step('Проверка статус кода'):
        check.equal(response.status_code, 422, 'Неверный статус код')

    with allure.step('Проверка параметра errors'):
        a = response.text
        b = a.find('Unprocessable Content')
        check.not_equal(b, -1)
