# author(s): CH Vasudeva Reddy (echvred)
import traceback
import time
from os import getenv as getenv
from behave import given, when, then, use_step_matcher
from selenium.common.exceptions import\
    TimeoutException, StaleElementReferenceException,\
    NoSuchFrameException, ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

A_VERY_LONG_WAIT = 30

use_step_matcher("re")

@given("I open CP")
def step_impl(context):
    context.browser.get("https://cp.nrws.ericsson.net/tmo")

@when("I fill in the login form")
def step_impl(context):
    try:
        time.sleep(5)
        context.browser.find_element_by_id('input')
        userfield = context.browser.find_element_by_css_selector('input.style-scope.paper-input')
        userfield.send_keys(getenv('CP_USR'))
        #userfield = context.browser.driver.find_elements_by_xpath("html/body/my-app-template/e-login-page/div/div[2]/form/div/div/div[1]/paper-input[1]/paper-input-container/div[2]/div/input")
        #userfield.send_keys(getenv('CP_USR'))
        time.sleep(5)
        userfield.send_keys(Keys.TAB)
        pwdfield = context.browser.switch_to.active_element
        pwdfield.send_keys(getenv('CP_PWD')
    except NoSuchElementException:
        traceback.print_exc()
# @then("I submit the login form")
# def step_impl(context):
    # context.browser.find_element_by_id('login-button').click()

# @when("I logout")
# def step_impl(context):
    # context.browser.find_element_by_css_selector('icon').click()

# @then("I verify that I have logged out successfully")
# def step_impl(context):
    # #time.sleep(5)
    # WebDriverWait(context.browser, A_VERY_LONG_WAIT).until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#userName')))

