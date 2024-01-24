title: Файл по запуску API тестов
date: 2024-01-02
description: Тесты по регистрации, авторизации, корзине и нагрузки
tag: api
project: Описание тестов и запуск
platform: Запуск тестов
link: http://example.com

Откуда Flask знает, какую функцию выводить, когда он получает запрос от клиента?

Flask сопоставляет URL и функции отображения, которые будут выводиться. Определение соответствий (маршрутизация) создается с помощью декоратора route или метода add_url_rule() в экземпляре Flask. Получить доступ к этим соответствиям можно с помощью атрибута url_map у экземпляра Flask.

	>>>
	>>> from main2 import app
	>>> app.url_map
	Map([<Rule '/' (OPTIONS, GET, HEAD) -> index>,
	 <Rule '/static/<filename>' (OPTIONS, GET, HEAD) ->  static>,
	 <Rule '/books/<genre>' (OPTIONS, GET, HEAD) ->  books>,
	 <Rule '/user/<user_id>' (OPTIONS, GET, HEAD) ->  user_profile>])
	>>>

Как видно, есть 4 правила. Flask определяет соответствия URL в следующем формате:

	url pattern, (comma separated list of HTTP methods handled by the route) -> view function to execute

Путь /static/<filename> автоматически добавляется для статических файлов Flask. О работе со статическими файлами речь пойдет в отдельном уроке «Обслуживание статических файлов во Flask».