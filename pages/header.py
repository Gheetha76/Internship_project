from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


class Header(Page):

    SEARCH_FIELD = (By.ID,'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    PARTICULAR_PRODUCT = (By.CSS_SELECTOR, ".a-section.aok-relative.s-image-fixed-height")
    RETURN_ORDERS_BTN = (By.ID, 'nav-orders')
    SIGNIN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-signin-button')
    LANG_SELECTION = (By.CSS_SELECTOR, ".icp-nav-flag-us")
    SPANISH_LANG = (By.CSS_SELECTOR, '#nav-flyout-icp [href="#switch-lang=es_US"]')
    DEPT_SELECTION = (By.ID, 'searchDropdownBox')
    SUB_HEADER_DEPT = (By.CSS_SELECTOR, '#searchDropdownDescription option[value="search-alias={SUB_STR}"]')
    NEW_ARRIVALS = (By.CSS_SELECTOR, 'a[href="/New-Arrivals/b/?_encoding=UTF8&node=17020138011&ref_=sv_sl_6"]')
    WOMENS_NEW_ARRIVALS = (By.CSS_SELECTOR, '.mm-merch-panel img[src*="https://m.media-amazon.com/images/G/01//AMAZON_FASHION/2022/"]')
    ALL_DROPDOWN = (By.ID, 'searchDropdownBox')
    SELECT_PRODUCT_HOODIE = (By.CSS_SELECTOR,'.s-image-padding')
    GOTO_CART_ICON = (By.CSS_SELECTOR, 'a[href="/gp/cart/view.html?ref_=nav_cart"]')
    BEST_SELLER_BTN = (By.CSS_SELECTOR, 'a[href="/gp/bestsellers/?ref_=nav_cs_bestsellers"]')

    def get_sub_header_dept_locator(self, dept):
        return [*self.SUB_HEADER_DEPT[0], *self.SUB_HEADER_DEPT[1].replace('{SUB_STR}', dept)]


    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)


    def hover_lang(self):
       actions = ActionChains(self.driver)
       lang = self.find_element(*self.LANG_SELECTION)
       actions.move_to_element(lang)
       actions.perform()

    def hover_new_arrivals(self):
           actions = ActionChains(self.driver)
           new_arrivals = self.find_element(*self.NEW_ARRIVALS)
           actions.move_to_element(new_arrivals)
           actions.perform()

    def select_dept(self, dept):
           dept_selection = self.find_element(*self.DEPT_SELECTION)
           select = Select(dept_selection)
           select.select_by_value(f'search-alias={dept}')

    def click_product(self):
        self.click(*self.PARTICULAR_PRODUCT)

    def click_orders(self):
        self.click(*self.RETURN_ORDERS_BTN)


    def click_cart_btn(self):
        self.click(*self.GOTO_CART_ICON)


    def click_best_seller_btn(self):
        self.click(*self.BEST_SELLER_BTN)


    def click_signin_from_popup(self):
        self.wait_for_element_clickable_click(*self.SIGNIN_BTN)


    def verify_signin_btn_clickable(self):
        self.wait_for_element_clickable(*self.SIGNIN_BTN)

    def verify_signin_btn_disappears(self):
        self.wait_for_element_clickable(*self.SIGNIN_BTN)


    def verify_spanish_lang(self):
       self.wait_for_element_appear(*self.SPANISH_LANG)

    def verity_dept_selected(self, dept):
        sub_header_locator = self.get_sub_header_dept_locator(dept)
        self.wait_for_element_appear(*sub_header_locator)

    def verify_user_see_deals(self):
        self.wait_for_element_appear(*self.WOMENS_NEW_ARRIVALS)

    def select_hoodie_product(self):
        self.click(*self.SELECT_PRODUCT_HOODIE)








