from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support.ui import Select
from base.base_driver import BaseDriver

class SigaGenPin(BaseDriver):
    def __init__(self, driver): #wait)
        self.driver = driver
        super().__init__(driver)

    ############### LOCATORS #################
    LOOPA_BUSINESS = "//*[@id='stbEconomy']/img[1]"
    APPLICANT_TYPE = "cboEconomyType"
    BUSINESS_FIELD = "txtName"
    SEARCH_BUTTON = "btnSearch"
    ALL_BUSINESS = "//td[@class='listD' and @columnname='EconomyName']"
    INVOICE_FIELD = "txtBillNo"
    ALL_INVOICES = "//td[@class='listTdCenter' and @columnname='BillNo']"
    CHECK_BOX = "grdList_ctl02_CheckBoxButton"
    SELECT_BUTTON = "btnSelect"
    SUBMIT_PIN_BUTTON = "ctl00$ContentsHolder$btnSubmit"
    OK_BUTTON = "//*[@id='btnConfirm']"

    ########### GET LOCATORS ##########
    def getLoopaBusiness(self):
        return self.wait_until_element_to_be_clickable(By.XPATH, self.LOOPA_BUSINESS)

    def getApplicantType(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.APPLICANT_TYPE)

    def getBusinessField(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.BUSINESS_FIELD)

    def getSearchButton(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.SEARCH_BUTTON)

    def getAllBusiness(self):
        return self.presence_of_all_elements_located(By.XPATH, self.ALL_BUSINESS)

    def getInvoiceField(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.INVOICE_FIELD)

    def getAllInvoices(self):
        return self.presence_of_all_elements_located(By.XPATH, self.ALL_INVOICES)

    def getCheckBox(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.CHECK_BOX)

    def getSelectButton(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.SELECT_BUTTON)

    def getSubmitPinButon(self):
        return self.wait_until_element_to_be_clickable(By.NAME, self.SUBMIT_PIN_BUTTON)

    def getOkButtonGenPin(self):
        return self.wait_until_element_to_be_clickable(By.XPATH, self.OK_BUTTON)

    ############# ACTIONS ##########
    # 51
    def enterLoopaBusiness(self):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        self.wait_frame_to_be_avaible_and_switch(By.ID, "popupFrame1")
        loopa = self.getLoopaBusiness()
        loopa.click()

    def enterApplicantType(self, tipo_aplicante):  # Empresa Importadora
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        self.wait_frame_to_be_avaible_and_switch(By.ID, "popupFrame2")
        Applicant = self.getApplicantType()
        drp = Select(Applicant)
        drp.select_by_visible_text(tipo_aplicante)

    def enterBusinessField(self, business):  # "CARIBETRANS SAS"
        busin = self.getBusinessField()
        busin.send_keys(business)

    def enterSearchButton(self):
        button = self.getSearchButton()
        button.click()

    def enterAllBusiness(self, business):  # "CARIBETRANS SAS"
        self.iterate_through_elements(By.XPATH, self.ALL_BUSINESS, business)

    def enterInvoiceField(self, invoice):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        self.wait_frame_to_be_avaible_and_switch(By.ID, "popupFrame1")
        invo_field = self.getInvoiceField()
        invo_field.send_keys(invoice)

    def enterSearchButton2(self):
        button = self.getSearchButton()
        button.click()

    def enterAllInvoices(self, invoice):
        all_invo = self.presence_of_all_elements_located(By.XPATH, self.ALL_INVOICES)
        for i in all_invo:
            if i.text == invoice:
                i.click()
                checkbox = self.getCheckBox()
                checkbox.click()
                time.sleep(1)
                select_button = self.getSelectButton()
                select_button.click()
                break

    def enterSubmitPinButton(self):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        button = self.getSubmitPinButon()
        button.click()

    def enterOkButtonGenPin(self):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        self.wait_frame_to_be_avaible_and_switch(By.ID, "_MESSAGE_IFR_MESSAGE_")
        ok_button = self.getOkButtonGenPin()
        ok_button.click()

##################################### BUSINESS METHODS #########################################

    def EmpresaPines(self, TipodeEmpresa, Contribuyente, Todos):
        self.enterLoopaBusiness()
        self.enterApplicantType(TipodeEmpresa)
        self.enterBusinessField(Contribuyente)
        self.enterSearchButton()
        self.enterAllBusiness(Todos)

    def CamposSeleccionandoFactura(self, factura):
        self.enterInvoiceField(factura)
        self.enterSearchButton2()
        self.enterAllInvoices(factura)

    #This method combines EmpresaPines() and CamposSeleccionandoFactura(), in case the company cannot be selected.
    def ConAgenteSinAgente(self, TipodeEmpresa, Contribuyente, Todos, factura):
        try:
            self.EmpresaPines(TipodeEmpresa, Contribuyente, Todos)
        except Exception as e:
                print(f"Usuario no es agente de Aduanas: {e}")
        finally:
            self.CamposSeleccionandoFactura(factura)

    def PresentandoPin(self):
        self.enterSubmitPinButton()
        self.enterOkButtonGenPin()


