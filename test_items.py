# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 10:41:04 2020
"""
"""
Создайте GitHub-репозиторий, в котором будут лежать файлы conftest.py и test_items.py.
Добавьте в файл conftest.py обработчик, который считывает из командной строки параметр language.
Реализуйте в файле conftest.py логику запуска браузера с указанным языком пользователя. Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.
В файл test_items.py напишите тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину. Например, можно проверять товар, доступный по http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.
Тест должен запускаться с параметром language следующей командой:
pytest --language=es test_items.py
и проходить успешно. Достаточно, чтобы код работал только для браузера Сhrome.
Отправить ссылку на данный репозиторий в качестве ответа на данное задание.
Отправить решение на рецензирование другим учащимся. Не забудьте, что решение на рецензирование можно отправить только один раз.
Проверьте решения минимум трех других учащихся, чтобы получить баллы за задание.
"""

import pytest
import time


links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"]

@pytest.mark.parametrize('link', links)
def test_add_product(browser, link):
    browser.implicitly_wait(5)
    browser.get(link)
#    time.sleep(30)
    assert browser.find_element_by_css_selector(".add-to-basket"), 'Button "add to basket" not found'
    











