from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

AMAZON_CUSTOMER_SERVICE = (By.CSS_SELECTOR,'a[href="/gp/help/customer/display.html?nodeId=508510&ref_=nav_cs_customerservice"]')
WELCOME_CUSTOMER = (By.CSS_SELECTOR,'h1.fs-heading.bolded')
ISSUE_CARD = (By.CSS_SELECTOR,'.issue-card-container')
UI_ELEMENTS = (By.CSS_SELECTOR,'.issue-card-wrapper')
SEARCH_HELP_LIBRARY = (By.XPATH,'//h2[text()="Search our help library"]')
INPUT_FIELD = (By.CSS_SELECTOR,'.a-input-text.a-span12')
TOPICS_ALL_HELP = (By.XPATH,'//h2[text()="All help topics"]')
ALL_HELP_TOPICS = (By.CSS_SELECTOR,'.help-topics')

@when('Click on Amazon Customer Service tab')
def click_amazon_customer_service(context):
    context.driver.find_element(*AMAZON_CUSTOMER_SERVICE).click()

@when('Check for UI elements are visible')
def check_ui_elements(context):
    context.driver.find_element(*WELCOME_CUSTOMER)
    context.driver.find_element(*ISSUE_CARD)
    # context.driver.find_element(*UI_ELEMENTS)

@then('Verify all {num} UI elements')
def verify_ui_elements(context,num):
    num = int(num)
    num3 = context.driver.find_elements(*UI_ELEMENTS)
    assert len(num3) == num, f'Error, expected {num}  but got only {len(num3)}'

@then('Check for search help library')
def search_help_library(context):
    context.driver.find_element(*SEARCH_HELP_LIBRARY)

@then('Check for input field to search library')
def check_input_field(context):
    context.driver.find_element(*INPUT_FIELD)


@then('Check for all help topics')
def check_all_help_topics(context):
    context.driver.find_element(*TOPICS_ALL_HELP)

@then('Verify all {h1} links under all help topics')
def verify_link(context,h1):
    h1 = int(h1)
    h2 = context.driver.find_elements(*ALL_HELP_TOPICS)
    assert len(h2) == h1, f'Error, expected {h1} but there is only {len(h2)}'