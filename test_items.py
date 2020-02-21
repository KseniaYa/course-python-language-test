# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 10:41:04 2020
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
    











