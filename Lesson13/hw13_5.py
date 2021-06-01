from selenium import webdriver
from time import sleep
import selenium.common.exceptions as ex
import string
import random


def random_name_coupon():
    return 'Shura' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


def random_discount_amount():
    return random.randrange(101)


def random_num_coupons():
    return random.randrange(1, 51)


class Coupons:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.naming = str(random_name_coupon())
        self.discount = str(random_discount_amount())
        self.num_coupons = str(random_num_coupons())

    def run_test_coupon(self):
        try:
            self.login_if_needed()
            self.create()
            self.search_coupon()
            self.del_found_coupon()
            self.logout()
        finally:
            self.fin()

    def login_if_needed(self):
        try:
            self.driver.find_element_by_css_selector('a.btn.dropdown-toggle.btn-success.navbar-btn')
        except ex.NoSuchElementException:
            self.driver.get('https://open-eshop.stqa.ru/oc-panel/auth/login')
            self.driver.find_element_by_css_selector('section#page input[name="email"]').send_keys(
                'demo@open-eshop.com')
            self.driver.find_element_by_css_selector('section#page input[name="password"]').send_keys('demo')
            self.driver.find_element_by_css_selector('section#page i.glyphicon.glyphicon-user.glyphicon').click()
        else:
            pass

    def go_coupon_page(self):
        self.driver.find_element_by_css_selector('span.glyphicon.glyphicon-th').click()
        self.driver.find_element_by_css_selector('i.glyphicon.glyphicon-tag').click()

    def create(self):
        self.login_if_needed()
        self.go_coupon_page()
        sleep(3)
        self.driver.find_element_by_css_selector('i.glyphicon.glyphicon-pencil').click()
        sleep(3)
        self.driver.find_element_by_css_selector('input#name').send_keys(self.naming)
        sleep(3)
        self.driver.find_element_by_css_selector('input[name="valid_date"]').click()
        sleep(2)
        dates = self.driver.find_elements_by_css_selector('div.datepicker-days tbody tr td')
        date_valid = random.choice(dates)
        sleep(2)
        date_valid.click()
        self.driver.find_element_by_css_selector('input#discount_amount').click()
        self.driver.find_element_by_css_selector('input#discount_amount').send_keys(self.discount)
        sleep(2)
        self.driver.find_element_by_css_selector('input[id="number_coupons"]').clear()
        self.driver.find_element_by_css_selector('input[id="number_coupons"]').send_keys(self.num_coupons)
        sleep(2)
        self.driver.find_element_by_css_selector('button[name = "submit"]').click()
        sleep(3)
        self.assert_success_created()
        self.assert_coupon_name_present()

    def assert_success_created(self):
        try:
            self.driver.find_element_by_css_selector('div.alert.alert-success')
        except ex.NoSuchElementException:
            print(
                'Проверка в сценарии создания купона завершилась неудачей. Сообщение о том, что купон успешно создан, '
                'отсутствует.')
        else:
            print('Проверка в сценарии создания купона завершилась успешно. Сообщение об успешном создании купона '
                  'присутствует')

    def assert_coupon_name_present(self):
        try:
            assert self.driver.find_elements_by_css_selector('div.table-responsive td')[0].text == self.naming
        except AssertionError:
            print('Проверка наличия купона в таблице закончилась неудачей. В ячейке неверное имя купона')
            print('Ожидалось имя %s, а на самом деле %s' % (
                self.naming, self.driver.find_elements_by_css_selector('div.table-responsive td')[0].text))
        except ex.NoSuchElementException:
            print(
                'Проверка наличия купона в таблице закончилась неудачей. Не найден элемент с локатором '
                'div.table-responsive td')
        else:
            print('Проверка наличия купона в таблице успешно завершена')

    def assert_coupon_name_not_present(self):
        self.driver.implicitly_wait(0)
        try:
            self.driver.find_element_by_css_selector('div.table-responsive td')
        except ex.NoSuchElementException:
            print('Проверка отсутствия купона в таблице успешно завершена')
        else:
            print(
                'Проверка отсутствия купона в таблице закончилась неудачей. Имя купона по прежнему находится в таблице')
        finally:
            self.driver.implicitly_wait(10)

    def search_coupon(self):
        self.driver.find_element_by_css_selector('input[name="name"]').clear()
        self.driver.find_element_by_css_selector('input[name = "name"]').send_keys(self.naming)
        sleep(3)
        self.driver.find_element_by_css_selector('form.form-inline.pull-right button.btn').click()
        sleep(3)
        self.assert_search_correct_value()

    def assert_search_correct_value(self):
        try:
            assert self.driver.find_element_by_css_selector('input[name="name"]').get_attribute("value") == self.naming
        except AssertionError:
            print(
                'Строка поля поиска не содержит то значение, по которому выполнялся поиск: строка поиска содержит %s, '
                'а мы ищем %s' % (self.driver.find_element_by_css_selector('input[name="name"]').get_attribute("value"),
                                  self.naming))
        except ex.NoSuchElementException:
            print(
                'Проверка сравнения строки поиска с искомым значением закончилась неудачей. Не найден элемент с '
                'локатором '
                'input[name="name"]')
        else:
            print('Сравнение строки поиска и искомым значением успешно')

    def assert_one_coupon_found(self):
        lst = self.driver.find_elements_by_css_selector('div.table-responsive tbody tr')
        if len(lst) == 1:
            print('Найден один купон, проверка успешна')
        else:
            print(
                'Проверка в сценарии поиска купона закончилась неудачей. Купонов больше или меньше одного, а именно: '
                '%d.' % len(
                    lst))

    def del_found_coupon(self):
        self.login_if_needed()
        try:
            self.driver.find_element_by_css_selector('div.table-responsive')
        except ex.NoSuchElementException:
            self.go_coupon_page()
        finally:
            self.search_coupon()
            self.assert_coupon_name_present()
            self.assert_one_coupon_found()
            self.driver.find_element_by_css_selector('i.glyphicon.glyphicon-trash').click()
            sleep(3)
            self.driver.find_element_by_css_selector('div.sweet-alert.showSweetAlert.visible')
            self.driver.find_element_by_css_selector('button.confirm').click()
            sleep(2)
            self.assert_empty_table()
            self.search_coupon()
            self.assert_coupon_name_not_present()

    def assert_empty_table(self):
        try:
            self.driver.find_element_by_css_selector('div.table-responsive tr[id][style="display: none;"]')
        except ex.NoSuchElementException:
            print('Таблица не пустая! Проверка удаления купона завершилась неуспешно')
        else:
            print('Таблица пустая, проверка удаления купона успешна')

    def logout(self):
        self.login_if_needed()
        sleep(2)
        self.driver.find_element_by_css_selector('a.btn.dropdown-toggle.btn-success.navbar-btn').click()
        sleep(2)
        self.driver.find_element_by_css_selector('i.glyphicon.glyphglyphicon.glyphicon-off').click()
        try:
            self.driver.find_element_by_css_selector('section#page input[name="password"]')
        except ex.NoSuchElementException:
            print(
                'Проверка в сценарии logout завершилась неудачей. Элемент с локатором section#page input['
                'name="password"] не найден.')
        else:
            print('Сценарий logout завершен успешно.')

    def fin(self):
        self.driver.close()


c = Coupons()
c.run_test_coupon()
