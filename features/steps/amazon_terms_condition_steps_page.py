from behave import given, when, then

@given('Open Amazon Term and Conditions page')
def open_term_condition_page(context):
    context.app.term_and_condition_page.open_term_condition_page()


@when('Click on Amazon Privacy Notice link')
def open_privacy_notice_page(context):
    context.app.term_and_condition_page.open_privacy_notice_page()


@when('Switch to the newly opened window')
def open_new_window(context):
    context.app.term_and_condition_page.open_new_page()


@then('Verify {text} Amazon Privacy Notice page is opened')
def verify_amazon_privacy_page_open(context, text):
        context.app.term_and_condition_page.verify_amazon_privacy_page_open(text)


@then('User can close new window and switch back to original')
def switch_to_original_windows(context):
        context.app.term_and_condition_page.switch_to_original_windows()