from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep



@when('Click on the cart icon')
def click_cart_icon(context):
    # context.driver.find_element(By.CSS_SELECTOR,"a[href='/gp/cart/view.html?ref_=nav_cart']").click()
    # context.driver.implicitly_wait(4)
    context.app.header.click_cart_btn()
    sleep(4)


@then('Verify {ex_text} message shows')
def amazon_cart_empty(context,ex_text):
    # expected_result = 'Your Amazon Cart is empty'
    # actual_result = context.driver.find_element(By.CSS_SELECTOR,".a-row.sc-your-amazon-cart-is-empty").text
    # assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
    context.app.search_result_page.verify_cart_is_empty(ex_text)