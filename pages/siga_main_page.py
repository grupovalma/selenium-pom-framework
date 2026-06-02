from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support.ui import Select
from base.base_driver import BaseDriver

class SigaMainMenu(BaseDriver):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    ###LOCATORS
    NEW_DECLARATION_BUTTON = "//*[@id='ctl00_ContentsHolder_btnNew']"
    RECAUDACION_MENU = "//a[text()='Recaudación']"
    PIN_SUB_MENU = "//a[text()='PIN']"
    ### GET LOCATORS
    def getNewDeclButton(self):
        return self.wait_until_element_to_be_clickable(By.XPATH,self.NEW_DECLARATION_BUTTON)

    def getRecaudacionMenu(self):
        return self.wait_until_element_to_be_clickable(By.XPATH, self.RECAUDACION_MENU)

    def getPinMenu(self):
        return self.wait_until_element_to_be_clickable(By.XPATH, self.PIN_SUB_MENU)

    ########################## ACTIONS ##############################
    def entertNewDeclButton(self):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        time.sleep(1)
        self.getNewDeclButton().click()

    def enterRecaudacionMenu(self):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "leftFrame")
        menu_recaudacion = self.getRecaudacionMenu()
        menu_recaudacion.click()
    def enterPinMenu(self):
        time.sleep(1)
        submenu_pin = self.getPinMenu()
        submenu_pin.click()

    ##################################### BUSINESS METHODS #########################################
    def Menues(self):
        self.enterRecaudacionMenu()
        self.enterPinMenu()

