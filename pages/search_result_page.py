from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultPage(Page):
    SEARCH_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, '.a-row.sc-your-amazon-cart-is-empty')
    PRODUCT_ADD = (By.CSS_SELECTOR, '#add-to-cart-button')
    THANKS_BUTTON = (By.CSS_SELECTOR, '.a-button-input[aria-labelledby="attachSiNoCoverage-announce"]')
    CART_ADD = (By.CSS_SELECTOR, 'a[href="/cart?ref_=sw_gtc"]')
    SUB_TOTAL_ITEM = (By.CSS_SELECTOR, '#sc-subtotal-label-buybox')



    def verify_search_result(self, result):
        self.verify_text(result,*self.SEARCH_RESULT)


    def verify_cart_is_empty(self,text):
        self.verify_text(text,*self.EMPTY_CART_TEXT)

    def click_add_to_cart_btn(self):
        self.click(*self.PRODUCT_ADD)
        self.click(*self.THANKS_BUTTON)
        self.click(*self.CART_ADD)

    def verify_count_of_items_in_cart(self,text):
        self.verify_text(text,*self.SUB_TOTAL_ITEM)