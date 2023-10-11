from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from support.logger import logger

class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_url(self, end_url=''):
        url = f'https://www.amazon.com/{end_url}'
        self.driver.get(url)
        logger.info(f'Opening URL {url}')
        sleep(2)
        self.driver.refresh()

    def click(self, *locator):
        logger.info(f'Clicking on {locator}')
        self.driver.find_element(*locator).click()


    def refresh(self):
         self.driver.refresh()

    def find_element(self, *locator):
        logger.info(f'Searching for {locator}')
        return self.driver.find_element(*locator)


    def find_elements(self, *locator):
        logger.info(f'Searching for number of {locator}')
        return self.driver.find_elements(*locator)

    def get_text(self, *locator):
        logger.info(f'get the text from {locator}')
        return self.driver.find_element(*locator).text


    def input_text(self, text, *locator):
        # e = self.driver.find_element(*locator)
        e = self.find_element(*locator)
        logger.info(f'Inputting text: "{text}"')
        e.send_keys(text)

    def get_current_window(self):
        return self.driver.current_window_handle

    def get_windows(self):
        windows = self.driver.window_handles
        logger.info(f'go to the next windows')
        print(windows)
        return windows

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print(all_windows)
        logger.info(f'Switching to {all_windows[1]}')
        self.driver.switch_to.window(all_windows[1])

    def switch_to_window(self, window_id):
        logger.info(f'Switching for {window_id}')
        # print(f'Switching to {window_id}')
        self.driver.switch_to.window(window_id)

    def close_page(self):
        self.driver.close()

    def wait_for_element_clickable(self, *locator):
        # self.wait.until(
        #     EC.element_to_be_clickable(locator),
        #     message=f'element not clickable: {locator}'
        # )
        self.wait.until(
            EC.element_to_be_clickable(locator))
        logger.info(f'Element not clickable:{locator}')


    def wait_for_element_clickable_click(self, *locator):
        e = self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable:{locator}'
        )
        e.click()

    def wait_for_element_appear(self, *locator):
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element did not appear: {locator}'
        )

    def wait_for_element_disappear(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator))
        logger.info(f'Element did not disappear:{locator}')

    def verify_text(self, expected_text, *locator):
            actual_text = self.find_element(*locator).text
            assert actual_text == expected_text
            logger.info(f'expected {expected_text} did not match actual {actual_text}')

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, \
            f'Error, expected partial text{expected_text}  not in {actual_text}'


    def verify_partial_url(self, expected_part_of_url):
        logger.info(f'expected partial url{expected_part_of_url} ')
        self.wait.until(EC.url_contains(expected_part_of_url))

    def verify_number_elements(self, number, *locator):
        number = int(number)
        elements_count = self.find_elements(*locator)
        assert len(elements_count) == number
        logger.info(f'Expected {number} links but got {len(elements_count)}')





