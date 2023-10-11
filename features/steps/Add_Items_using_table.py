from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

ITEM1_SEARCH = (By.ID,'twotabsearchtextbox')
SEARCH1_BUTTON = (By.ID,'nav-search-submit-button')
ITEM_NAME = (By.XPATH,'//span[@class="a-color-state a-text-bold"]')


@when('Testing for {the_item}')
def item_searching(context,the_item):
    # context.driver.find_element(*ITEM1_SEARCH).send_keys(the_item)
    # context.driver.find_element(*SEARCH1_BUTTON).click()
    context.app.header.search_product(the_item)

@then('Verify searching {expected_item} is correct')
def verify_product_name(context,expected_item):
     name_items  = context.driver.find_element(*ITEM_NAME).text
     assert expected_item == name_items , f'Error, expected {expected_item} did not match {name_items}'