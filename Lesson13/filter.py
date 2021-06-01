from selenium import webdriver
from time import sleep
import random
import selenium.common.exceptions as ex


class Test:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test(self):
        try:
            self.login()
            self.edit(str(random.randrange(1, 20)))
            self.logout()
        finally:
            self.fin()

    def logout(self):
        sleep(4)
        self.driver.find_element_by_css_selector('a.btn.dropdown-toggle.btn-success.navbar-btn').click()
        self.driver.find_element_by_css_selector('i.glyphicon.glyphglyphicon.glyphicon-off').click()
        try:
            self.driver.find_element_by_css_selector('section#page input[name="email"]')
        except ex.NoSuchElementException:
            print(
                'Проверка в сценарии логаута завершилась неудачей. Элемент с локатором section#page input[name="email"] не найден.')
        else:
            print('Сценарий логаута завершен успешно.')

    def edit(self, val):
        self.go_coupon_page()
        self.driver.find_element_by_css_selector('a[title="Edit"]').click()
        self.driver.find_element_by_css_selector('input#number_coupons').clear()
        sleep(4)
        self.driver.find_element_by_css_selector('input#number_coupons').send_keys(val)
        self.driver.find_element_by_css_selector('button.btn.btn-primary').click()
        try:
            self.driver.find_element_by_css_selector('div.alert.alert-success')
        except ex.NoSuchElementException:
            print(
                'Проверка номер1 в сценарии модификации завершилась неудачей. Элемент с локатором div.alert.alert-success не найден.')
        else:
            print('Проверка номер1 в сценарии модификации завершилась успешно.')
        self.check_that_number_changed(val)

    def check_that_number_changed(self, num):
        self.go_coupon_page()
        lst = self.driver.find_elements_by_css_selector('div.table-responsive td')
        if len(lst) > 3:
            if lst[3].text == num:
                print('Все ок')
            else:
                print('В соответствующей ячейке неправильное количество купонов.')
                print('Ожидалось %s купонов, на самом деле %s купонов' % (
                    num, self.driver.find_elements_by_css_selector('div.table-responsive td')[3].text))
        else:
            print('Недостаточно элементов с нужным локатором')

    def go_coupon_page(self):
        self.driver.find_element_by_css_selector('span.glyphicon.glyphicon-th').click()
        self.driver.find_element_by_css_selector('i.glyphicon.glyphicon-tag').click()

    def login(self):
        self.driver.get('https://open-eshop.stqa.ru/oc-panel/auth/login')
        self.driver.find_element_by_css_selector('section#page input[name="email"]').send_keys('demo@open-eshop.com')
        self.driver.find_element_by_css_selector('section#page input[name="password"]').send_keys('demo')
        self.driver.find_element_by_css_selector('section#page i.glyphicon.glyphicon-user.glyphicon').click()
        try:
            self.driver.find_element_by_css_selector('a.btn.dropdown-toggle.btn-success.navbar-btn')
        except ex.NoSuchElementException:
            print(
                'Проверка в сценарии логина завершилась неудачей. Элемент с локатором a.btn.dropdown-toggle.btn-success.navbar-btn не найден.')
        else:
            print('Сценарий логина завершен успешно.')

    def fin(self):
        self.driver.close()


t = Test()
t.test()
