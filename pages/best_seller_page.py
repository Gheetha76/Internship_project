from selenium.webdriver.common.by import By
from pages.base_page import Page

class Bestsellerpage(Page):
    TOP_MENU = (By.CSS_SELECTOR, 'div.celwidget.c-f ul a')
    TEXT_TOP_MENU = (By.ID, 'zg_banner_text')

    def bestseller_menu_links(self):
        self.find_elements(*self.TOP_MENU)



    def get_text_top_menu(self):
        self.get_text(*self.TEXT_TOP_MENU)



    def verify_top_menu_count(self, number):
           self.verify_number_elements(number, *self.TOP_MENU)