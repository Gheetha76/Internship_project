from behave import given, when, then
from selenium.webdriver.common.by import By

# @given('Open Amazon page')
# def open_amazon(context):
#     context.driver.get('https://www.amazon.com/')


@when('Search for table')
def search_table(context):
    # context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')
    # context.driver.find_element(By.ID, 'nav-search-submit-button').click()
    context.app.header.search_product('table')

@then('Verify search result is correct')
def verify_search_result(context):
    expected_result = '"table"'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '.a-color-state.a-text-bold').text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
