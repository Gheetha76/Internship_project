from pages.base_page import Page
from time import sleep
from support.logger import logger


class MainPage(Page):

    def open_main(self):
        logger.info('Opening https://www.amazon.com/ ')
        self.driver.get('https://www.amazon.com/')
        sleep(3)
        self.driver.refresh()
