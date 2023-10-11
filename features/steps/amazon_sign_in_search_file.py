from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


FOOTER_LINKS = (By.CSS_SELECTOR,'.navFooterDescItem')

@given('Open Amazon page')
def open_amazon_page(context):
    context.app.main_page.open_main()


@when('Click on Returns and orders')
def return_orders(context):
    context.app.header.click_orders()


@when('Click on button from SignIn popup')
def click_signin_from_popup(context):
    context.app.header.click_signin_from_popup()


@when('Wait for 3 sec')
def wait_sec(context):
    sleep(3)


@when('Hover over language options')
def hover_lang(context):
    context.app.header.hover_lang()



@then('Verify Sign In is clickable')
def verify_signin_btn_clickable(context):
    context.app.header.verify_signin_btn_clickable()


# @then('Verify {text} page opens')
# def sign_in_page_opens(context,text):
#     context.app.header.verify_sign_in_page_opens(text)


@then('Verify Sign in page opens')
def sign_in_page(context):
    context.app.sign_in_page.verify_sign_in_page_opened()



# @then('Verify email input field is present')
# def email_input_field(context):
#     context.app.header.verify_email_input_field()


@then('Verify Sign In disappears')
def verify_signin_btn_disappears(context):
    context.app.header.verify_signin_btn_disappears()


@then('Verify footer has {expected_amount} links')
def verify_link_amount(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*FOOTER_LINKS)
    assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'


@then('Verify many links are shown in the footer')
def verify_many_links(context):
    links = context.driver.find_elements(*FOOTER_LINKS)
    assert len(links) > 1, f'Expected at least 2 links, but got {len(links)}'


@then('Verify Spanish option present')
def verify_spanish_lang(context):
    context.app.header.verify_spanish_lang()





