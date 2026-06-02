import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def wait_frame_to_be_avaible_and_switch(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        frame_test = wait.until(EC.frame_to_be_available_and_switch_to_it((locator_type, locator)))
        return frame_test

    def wait_until_element_to_be_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element

    def presence_of_all_elements_located(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        elements = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return elements

    def iterate_through_elements(self, locator_type, locator, target_text):
        wait = WebDriverWait(self.driver, 10)
        all_elements = self.presence_of_all_elements_located(locator_type, locator)
        for element in all_elements:
            if element.text == target_text:
                element.click()
                break

    def presence_of_element_located(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.presence_of_element_located((locator_type, locator)))
        return element



