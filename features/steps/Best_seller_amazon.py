from behave import given, when, then
from selenium.webdriver.common.by import By

# SELLER_BEST_PAGE =(By.CSS_SELECTOR,'a[href="/gp/bestsellers/?ref_=nav_cs_bestsellers"]')
# NUMBER_OF_LINKS =(By.CSS_SELECTOR,'#zg_header a')

TOP_MENU = (By.CSS_SELECTOR, 'div.celwidget.c-f ul a')

@when('Click on best sellers')
def open_best_seller_page(context):
    # context.driver.find_element(*SELLER_BEST_PAGE).click()
     context.app.header.click_best_seller_btn()


@then('Verify this page has {n1} top menu')
def Verify_number_link(context,n1):
    # n1 = int(n1)
    # link_number = context.driver.find_elements(*NUMBER_OF_LINKS)
    # assert len(link_number) == n1 , f'Error, expected {n1} but got only {len(link_number)}'
    context.app.best_seller_page.verify_top_menu_count(n1)



@then('Verify each 5 top menus pages opens')
def verify_top_menu_page_opens(context):
    expected_text_top_menu = ['Amazon Best Sellers', 'Amazon Hot New Releases',
                              'Amazon Movers & Shakers', 'Amazon Most Wished For',
                              'Amazon Gift Ideas']
    actual_text_top_menu = []

    top_menu_links = context.driver.find_elements(*TOP_MENU)
    for menu_link in top_menu_links[:]:
        menu_link.click()
        current_top_menu = context.app.best_seller_page.get_text_top_menu()
        actual_text_top_menu.append(current_top_menu)
        return top_menu_links
    assert actual_text_top_menu == expected_text_top_menu, f'Expected {expected_text_top_menu} did not match actual {actual_text_top_menu}'
