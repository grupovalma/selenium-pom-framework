from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support.ui import Select
from base.base_driver import BaseDriver

class SigaSearchingPin(BaseDriver):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    ############### LOCATORS #################
    NEW_PIN_BUTTON = "ctl00_ContentsHolder_btnNew"
    ADD_PIN_BUTTON = "ctl00_ContentsHolder_btnAdd"
    PIN_NUMBER = "ctl00_ContentsHolder_txtPinNo"

    ################# GET LOCATORS################################
    def getNewPinButton(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.NEW_PIN_BUTTON)

    def getAddPinButton(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.ADD_PIN_BUTTON)

    def getPrintPinId(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.PIN_NUMBER)

    ################################### ACTIONS################################
    def enterNewPinButton(self):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        time.sleep(2)
        new = self.getNewPinButton()
        new.click()

    def enterAddPinButton(self):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        add = self.getAddPinButton()
        add.click()

    def enterPrintPinId(self):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        element = self.getPrintPinId()
        value = element.get_attribute("value")

        assert value.strip(), "El Pin no pudo ser Generado"
        print("Pin Generado: ", value)
        print("------------------------------------------------------------------")

    ##################################### BUSINESS METHODS #########################################
    def NuevoyAgregandoPin(self):
        self.enterNewPinButton()
        self.enterAddPinButton()
