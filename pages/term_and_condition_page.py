from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
class TermAndConditionPage(Page):


    PRIVACY_NOTICE_LINK = (By.CSS_SELECTOR,'a[href="https://www.amazon.com/privacy"]')
    PRIVACY_PAGE_CHECK = (By.CSS_SELECTOR,'.help-service-content')

    def open_term_condition_page(self):
        self.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')
        sleep(3)
        self.refresh()

    def open_privacy_notice_page(self):
            self.click(*self.PRIVACY_NOTICE_LINK)

    def open_new_page(self):
            self.driver.get('https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ')
            sleep(3)
            self.refresh()

    def open_new_window(self, window_id):
            self.switch_to_window(window_id)

    def verify_amazon_privacy_page_open(self, expted_text):
            self.verify_partial_text(expted_text, *self.PRIVACY_PAGE_CHECK)

    def switch_to_original_windows(self):
            self.get_current_window()