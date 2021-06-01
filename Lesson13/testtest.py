import random as r

from selenium import webdriver
from time import sleep
import selenium.common.exceptions as ex
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://open-eshop.stqa.ru/oc-panel/auth/login')
driver.find_element_by_css_selector('section#page input[name="email"]').send_keys('demo@open-eshop.com')
driver.find_element_by_css_selector('section#page input[name="password"]').send_keys('demo')
driver.find_element_by_css_selector('section#page i.glyphicon.glyphicon-user.glyphicon').click()
sleep(3)
driver.find_element_by_css_selector('span.glyphicon.glyphicon-th').click()
sleep(3)
driver.find_element_by_css_selector('i.glyphicon.glyphicon-tag').click()
sleep(3)
driver.find_element_by_css_selector('i.glyphicon.glyphicon-pencil').click()
sleep(3)
driver.find_element_by_css_selector('input[name="valid_date"]').click()
sleep(3)
lala = driver.find_elements_by_css_selector('div.datepicker-days tbody tr')
l = r.choice(lala)
sleep(3)
l.click()
