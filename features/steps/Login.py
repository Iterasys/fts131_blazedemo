import time

from behave import *
from selenium import *
from selenium.webdriver.common.by import By

@when(u'clico em Home')
def step_impl(context):
    # context.driver.find_element(By.LINK_TEXT, 'home').click()
    # context.driver.find_element(By.CSS_SELECTOR, 'a[href=home]').click()
    # context.driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()
    context.driver.find_element(By.CSS_SELECTOR, 'a:nth-child(3)').click()
    time.sleep(2)

@then(u'exibe a pagina de Login')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.panel-heading').text == 'Login'
    time.sleep(2)

@when(u'preencho "email" e "senha"')
def step_impl(context):
    context.driver.find_element(By.ID, 'email').send_keys('correia@iterasys.com.br')
    context.driver.find_element(By.ID, 'password').send_keys('123456')
    time.sleep(2)

@when(u'clico em Login')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').click()
    time.sleep(2)

@then(u'exibe a mensagem de pagina expirada')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.message').text == 'Page Expired'