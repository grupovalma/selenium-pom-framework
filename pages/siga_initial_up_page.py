from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support.ui import Select

from base.base_driver import BaseDriver


class SigaUserPass(BaseDriver):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    ####################################### LOCATORS ########################################
    USER_NO_VIAFIRMA_FIELD = "ctl00_ContentsHolder_txtAccount"
    PASS_NO_VIA_FIRMA_FIELD = "ctl00_ContentsHolder_txtPassword"
    OK_BUTTON_NO_VIA_FIELD = "ctl00_ContentsHolder_btnLogin"
    #------------------VIA FIRMA-------------------------------#
    ID_VIAFIRMA_FIELD = "ctl00_ContentsHolder_txtCedularNo"
    ID_VIAFIRMA_FIELD2 = "username"
    LOGIN_BUTTON_VIAFIRMA = "ctl00_ContentsHolder_btnLogin"
    PASS_PIN_VIAFIRMA_FIELD = "verify-code"
    ACCEPT_VIAFIRMA_BUTTON = "accept"
    OK_PIN_BUTTON_VIAFIRMA = "(//div[@id='verify-button'])[1]"

    ######################################RETURNING LOCATORS#####################################
    def getUserNoVia(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.USER_NO_VIAFIRMA_FIELD)

    def getPassNoVia(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.PASS_NO_VIA_FIRMA_FIELD)

    def getOkButtonNoVia(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.OK_BUTTON_NO_VIA_FIELD)

    # ---------------------------------------------VIA FIRMA-------------------------------#
    def getIDVia(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.ID_VIAFIRMA_FIELD)
    def getIDVia2(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.ID_VIAFIRMA_FIELD2)
    def getLoginButtonVia(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.LOGIN_BUTTON_VIAFIRMA)
    def getPassPinVia(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.PASS_PIN_VIAFIRMA_FIELD)
    def getAcceptVia(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.ACCEPT_VIAFIRMA_BUTTON)
    def getOkPinButton(self):
        return self.wait_until_element_to_be_clickable(By.XPATH, self.OK_PIN_BUTTON_VIAFIRMA)


    ######################################### ACTIONS ################################################
    def enterUserNoVia(self, username):
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        self.getUserNoVia()
        self.getUserNoVia().send_keys(username)

    def enterPassNoVia(self, password):
        self.getPassNoVia()
        self.getPassNoVia().send_keys(password)

    def enterOkButtonNoVia(self):
        self.getOkButtonNoVia().click()

    # ------------------VIA FIRMA-------------------------------#
    def enterCedula(self, cedula):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        id = self.getIDVia()
        id.send_keys(cedula)

    def enterLoginButton(self, cedula2, pin_number):
        login_button = self.getLoginButtonVia()
        login_button.click()
        time.sleep(2)
        parwhandle = self.driver.current_window_handle
        print(parwhandle)
        all_handles = self.driver.window_handles

        for i in all_handles:
            if i != parwhandle:
                self.driver.switch_to.window(i)
                user = self.getIDVia2()
                user.send_keys(cedula2)
                accept_button = self.getAcceptVia()
                accept_button.click()
                pinnumber = self.getPassPinVia()
                pinnumber.send_keys(pin_number)
                verify_button = self.getOkPinButton()
                verify_button.click()
                break

        self.driver.switch_to.window(parwhandle)
        self.driver.switch_to.default_content()

    ##################################BUSINESS METHODS########################################
    def No_Via_Firma_Launch(self, username, password):
        self.enterUserNoVia(username)
        self.enterPassNoVia(password)
        self.enterOkButtonNoVia()

    def Viafirma(self, cedula, cedula2, pinnum):
        self.enterCedula(cedula)
        self.enterLoginButton(cedula2, pinnum)



