from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from base.base_driver import BaseDriver

class SigaProfile(BaseDriver):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    #LOCATORS
    ALL_CUSTOM_PROFILES = "//div[@class='jqx-listitem-element jqx-listitem-element-custom-scheme']"
    OK_BUTTON = "ctl00_ContentsHolder_btnOK"

    #GET LOCATORS
    def getCustomProfiles(self):
        return self.presence_of_all_elements_located(By.XPATH, self.ALL_CUSTOM_PROFILES)
    def getOkButton(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.OK_BUTTON)

    #ACTIONS
    def enterCustomProfiles(self, profile_name):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        self.iterate_through_elements(By.XPATH, self.ALL_CUSTOM_PROFILES, profile_name)

    def enterOkButton(self):
        okbutton = self.getOkButton()
        okbutton.click()

    ##################################BUSINESS METHODS########################################
    def selectingProfile(self, perfil_1, perfil_opcional):
        try:
            self.enterCustomProfiles(perfil_1)
        except:
            self.enterCustomProfiles(perfil_opcional)
        self.enterOkButton()