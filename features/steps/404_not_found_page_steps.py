from behave import *

@given('Store original window')
def store_original_window(context):
    context.original_window = context.app.not_found_page.store_original_window()


@when('Click on a dog image')
def click_dog_img(context):
    context.app.not_found_page.click_dog_img()


@when('Switch to new window')
def switch_window(context):
    context.app.not_found_page.switch_to_new_window()
