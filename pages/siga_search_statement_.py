from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from base.base_driver import BaseDriver
from pages.siga_statement_page import SigaStatement

class SigaSearchStatement(BaseDriver):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    ################################################### LOCATORS ############################################
    SEARCH_DECLARATION_FIELD = "ctl00$ContentsHolder$stbDeclarationNo"
    LOOPA_ADMIN_BUTTON = "//*[@id='ctl00_ContentsHolder_stbCustoms']/img[1]"
    SEARCH_ADMIN_BUTTON = "btnSearch"
    SUBMIT_DEC_FIELD = "ctl00_ContentsHolder_btnSearch"
    ALL_DECLARATIONS = "//td[@class='listTdCenter' and @columnname='ImpDeclarationNo']"
    ALL_ADMINS = "//td[@class='listD' and @columnname= 'AreaName']"
    SUB_MENU_DECLARACION_FIELD = "//a[text()='Declaración de Importación']"

    ########################################## GET LOCATORS ############################################
    def getSearchDeclaField(self):
        return self.wait_until_element_to_be_clickable(By.NAME, self.SEARCH_DECLARATION_FIELD)
    def getLoopaAdminButton(self):
        return self.wait_until_element_to_be_clickable(By.XPATH, self.LOOPA_ADMIN_BUTTON)
    def getSearchaAdminButton(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.SEARCH_ADMIN_BUTTON)
    def getAllAdmins(self):
        return self.presence_of_all_elements_located(By.XPATH, self.ALL_ADMINS)
    def getSubmitDec_Field(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.SUBMIT_DEC_FIELD)
    def getAllDclaself(self):
        return self.presence_of_all_elements_located(By.XPATH, self.ALL_DECLARATIONS)
    def getSubmenuDecField(self):
        return self.wait_until_element_to_be_clickable(By.XPATH, self.SUB_MENU_DECLARACION_FIELD)


    ################################# ACTIONS ##################################
    def enterSearchDeclaField(self, declar_no):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        decla_field = self.getSearchDeclaField()
        decla_field.send_keys(declar_no)
    def enterLoopaAdminButton(self):
        loopa_admin = self.getLoopaAdminButton()
        loopa_admin.click()

    def enterSearchaAdminButton(self, admin):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        self.wait_frame_to_be_avaible_and_switch(By.ID, "popupFrame1")
        search_admin_Button = self.getSearchaAdminButton()
        search_admin_Button.click()

    def enterAllAdmins(self, admin):
        self.iterate_through_elements(By.XPATH, self.ALL_ADMINS, admin)

    def enterSubmitDec_Field(self):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        dec_submit = self.getSubmitDec_Field()
        dec_submit.click()

    def enterAllDclaself(self, declar_no):
        self.iterate_through_elements(By.XPATH, self.ALL_DECLARATIONS, declar_no)


    def enterSubmenuDecField(self):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "leftFrame")
        decla_submenu = self.getSubmenuDecField()
        decla_submenu.click()


   ########################################### BUSINESS METHODS ##############################################
    def AdministracionDeFactura(self, Administracion, Seleccionando):
        self.enterLoopaAdminButton()
        self.enterSearchaAdminButton(Administracion)
        self.enterAllAdmins(Seleccionando)
        self.enterSubmitDec_Field()

