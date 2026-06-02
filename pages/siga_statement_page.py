import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support.ui import Select
from base.base_driver import BaseDriver

class SigaStatement(BaseDriver):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    ######################################################################LOCATORS###################################################################
    DEC_ADMIN_LOOPA = "//*[@id='ctl00_ContentsHolder_stbLocalCustoms']/img[1]"  # SelAdminLoopa
    SEARCH_ADM_BUTTON = "btnSearch"
    ALL_ADMINS_1 = "//td[@class='listD' and @columnname='AreaName']"  # SearchingAdmin
    SELECTING_MANIFEST_TYPE = "ctl00_ContentsHolder_cboClearanceType"  # SelManType
    INVOICE_FIELD = "ctl00_ContentsHolder_stbBL"
    DEPARTURE_DESTINY_LOOPA = "//*[@id='ctl00_ContentsHolder_stbDestinationLocation']/img[1]"
    DESTINY_ADMIN = "cboAreaCode"#11
    SEARCH_BUTTON = "btnSearch"
    STORE_ALMACEN = "//td[@class='listD' and @columnname='LocationName']"
    IMPOTER_LOOPA = "//*[@id='ctl00_ContentsHolder_ctl07']/img[1]"
    IMPORTER_TYPE = "cboEconomyType"
    SEARCH_IMPORTER_BUTTON = "btnSearch"
    ALL_IMPORTERS = "//td[@class='listD' and @columnname='EconomyName']"
    PROVIDER_SEARCH_BUTTON = "//*[@id='ctl00_ContentsHolder_ctl09']/img[1]"
    PROVIDER_TYPE = "cboEconomyType"
    PROVIDER_NAME = "txtName"
    ALL_PROVIDERS = "//td[@class='listD' and @columnname='EconomyName']"
    IMPORTER_FIELD = "txtName"
    ADD_PROVIDER_BUTTON = "ctl00_ContentsHolder_btnAddSupplier"
    REGIME_LOOPA = "//*[@id='ctl00_ContentsHolder_stbRegimen']/img[1]"
    REGIME_SEARCH_BUTTON = "btnSearch"
    ALL_REGIMES = "//td[@class='listTd' and @columnname='RegimenName']"
    PRODUCT_LOOPA = "//*[@id='ctl00_ContentsHolder_ctl13']/img[1]"
    PRODUCT_NAME = "txtProductName"
    SEARCH_BUTTON_PRODUCT = "btnSearch"
    ALL_PRODUCTS = "//td[@class='listTd' and @columnname='ProductName']"
    PRODUCT_STATE = "ctl00_ContentsHolder_cboProductStatusName"
    FOB_FIELD = "ctl00_ContentsHolder_ntbFOBValue"
    WEIGHT_FIELD_P = "ctl00_ContentsHolder_ntbWeight"
    PRODUCT_QUANTITY =  "ctl00_ContentsHolder_ntbQty"
    DESCRITION_FIELD = "ctl00_ContentsHolder_txtProductRemark"
    ADD_PRODUCT_BUTTON = "ctl00_ContentsHolder_btnAddDetail"
    DOCUMENT_TYPE_DD = "ctl00_ContentsHolder_cboRequiredDocumentCode"
    REF_NUMBER = "ctl00_ContentsHolder_txtRequiredDocumentNo"
    EMITIDO_FIELD = "ctl00_ContentsHolder_txtBizDocIssuerName"
    MAIL_FIELD = "ctl00_ContentsHolder_txtBizDocIssuerEmail"
    PHONE_FIELD = "ctl00_ContentsHolder_txtBizDocIssuerTel"
    ADD_DOC_FIELD = "ctl00_ContentsHolder_btnAddDocuments"
    ATTACH_FIELD = "fucAttach_filer_input"
    FLETE_FIELD = "ctl00$ContentsHolder$ntbFreightValue"
    INSURANCE_FIELD = "ctl00_ContentsHolder_ntbInsurance"
    GROSS_WEIGHT_FIELD = "ctl00_ContentsHolder_ntbTotalWeight"
    DEC_BOX_FIELD = "ctl00$ContentsHolder$chkGenerateNoYN"
    DEC_NUM_FIELD = "ctl00_ContentsHolder_stbDeclarationNo"
    SUBMIT_BUTTON = "ctl00$ContentsHolder$ctl01"
    NO_SUBMIT_BUTTON = "//img[@alt='No']"
    YES_SUBMIT_BUTTON = "/html/body/table/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/img[1]"
    OK_SUBMIT_BUTTON = "btnConfirm"
    INVOICE_INFO_FIELD = "ctl00_ContentsHolder_txtBillNo"

    ########################################################################GET LOCATORS###################################################################################
    def getDecAdminLoopa(self):
        return self.wait_until_element_to_be_clickable(By.XPATH, self.DEC_ADMIN_LOOPA)
    def getSearchAdminButton(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.SEARCH_ADM_BUTTON)
    def getAllAdministrations(self):
        return self.presence_of_all_elements_located(By.XPATH, self.ALL_ADMINS_1)
    def getSelectingManType(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.SELECTING_MANIFEST_TYPE)
    def getInvoiceField(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.INVOICE_FIELD)
    def getDepartLoopa(self):
        return self.wait_until_element_to_be_clickable(By.XPATH, self.DEPARTURE_DESTINY_LOOPA)
    def getDestinyAdmin(self):  # 11
        return self.wait_until_element_to_be_clickable(By.ID, self.DESTINY_ADMIN)
    def getSearchButton(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.SEARCH_BUTTON)
    def getStore(self):
        return self.presence_of_all_elements_located(By.XPATH, self.STORE_ALMACEN)
    def getImporterLoopa(self):
        return self.wait_until_element_to_be_clickable(By.XPATH, self.IMPOTER_LOOPA)
    def getImporterType(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.IMPORTER_TYPE)
    def getSearchingImporterButton(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.SEARCH_IMPORTER_BUTTON)
    def getImporterName(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.IMPORTER_FIELD)
    def getAllImporters(self):
        return self.presence_of_all_elements_located(By.XPATH, self.ALL_IMPORTERS)
    def getProviderSearchButton(self):
        return self.wait_until_element_to_be_clickable(By.XPATH, self.PROVIDER_SEARCH_BUTTON)
    def getProviderType(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.PROVIDER_TYPE)
    def getProviderName(self):
        return self.wait_until_element_to_be_clickable(By.NAME, self.PROVIDER_NAME)
    def getAddProvider(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.ADD_PROVIDER_BUTTON)
    def getRegimeLoopa(self):
        return self.wait_until_element_to_be_clickable(By.XPATH, self.REGIME_LOOPA)
    def getRegimeSearchLoopa(self):
        return self.wait_until_element_to_be_clickable(By.NAME, self.REGIME_SEARCH_BUTTON)
    def getProductLoopa(self):
        return self.wait_until_element_to_be_clickable(By.XPATH, self.PRODUCT_LOOPA)
    def getProductName(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.PRODUCT_NAME)
    def getSearchButtonProduct(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.SEARCH_BUTTON_PRODUCT)
    def getAllProducts(self):
        return self.presence_of_all_elements_located(By.XPATH, self.ALL_PRODUCTS)
    def getProductState(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.PRODUCT_STATE)
    def getFob(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.FOB_FIELD)
    def getWeightProduct(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.WEIGHT_FIELD_P)
    def getProductQa(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.PRODUCT_QUANTITY)
    def getProductDescriptio(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.DESCRITION_FIELD)
    def getAddProduct(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.ADD_PRODUCT_BUTTON)
    def getDocumentType(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.DOCUMENT_TYPE_DD)
    def getRefDocNumber(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.REF_NUMBER)
    def getIssuedEmitid(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.EMITIDO_FIELD)
    def getMail(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.MAIL_FIELD)
    def getPhone(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.PHONE_FIELD)
    def getAddDocument(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.ADD_DOC_FIELD)
    def getAttachField(self):
        return self.presence_of_element_located(By.ID, self.ATTACH_FIELD)
    def getFleteField(self):
        return self.wait_until_element_to_be_clickable(By.NAME, self.FLETE_FIELD)
    def getInsuranceField(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.INSURANCE_FIELD)
    def getGrossWeightField(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.GROSS_WEIGHT_FIELD)
    def getGenDeclaNumber(self):
        return self.wait_until_element_to_be_clickable(By.NAME, self.DEC_BOX_FIELD)
    def getDecNumVal(self):
        return self.presence_of_element_located(By.ID, self.DEC_NUM_FIELD)
    def getSubmitDeclaButton(self):
        return self.wait_until_element_to_be_clickable(By.NAME, self.SUBMIT_BUTTON)
    def getNobuttonSubmit(self):
        return self.wait_until_element_to_be_clickable(By.XPATH, self.NO_SUBMIT_BUTTON)
    def getYesbuttonSubmit(self):
        return self.wait_until_element_to_be_clickable(By.XPATH, self.YES_SUBMIT_BUTTON)
    def getMessageSubmitOk(self):
        return self.wait_until_element_to_be_clickable(By.ID, self.OK_SUBMIT_BUTTON)
    def getInvoiceGeneration(self):
        return self.presence_of_element_located(By.ID, self.INVOICE_INFO_FIELD)

    ####################################################################### ACTIONS ##################################################################

    def enterDecAdminLoopa(self):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        admin_loopa = self.getDecAdminLoopa()
        admin_loopa.click()

    def enterSearchAdminButton(self):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        self.wait_frame_to_be_avaible_and_switch(By.ID, "popupFrame1")
        searchButton = self.getSearchAdminButton()
        searchButton.click()

    def enterAllAdministrations(self, admin):
        self.iterate_through_elements(By.XPATH, self.ALL_ADMINS_1, admin)

    def enterSelectingManType(self, mani_type):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        destiny = self.getSelectingManType()
        drp = Select(destiny)
        drp.select_by_visible_text(mani_type)

    def enterInvoiceField(self, invoice_num):
        self.getInvoiceField().send_keys(invoice_num)

    def enterDepartLoopa(self):
        self.getDepartLoopa().click()

    def enterDestinyAdmin(self, admin):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        self.wait_frame_to_be_avaible_and_switch(By.ID, "popupFrame1")
        time.sleep(1)
        dest_admin = self.getDestinyAdmin()
        drp = Select(dest_admin)
        for i in drp.options:
            if i.text == admin:
                drp.select_by_visible_text(admin)
                break

        self.getSearchButton().click()

    def enterStore(self, store):
        self.iterate_through_elements(By.XPATH, self.STORE_ALMACEN, store)

    def enterImporterLoopa(self):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        self.getImporterLoopa().click()

    def enterImporterType(self, importype):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        self.wait_frame_to_be_avaible_and_switch(By.ID, "popupFrame1")
        impo_type = self.getImporterType()
        drp = Select(impo_type)
        drp.select_by_visible_text(importype)

    def enterImporterName(self, importername):
        time.sleep(1)
        self.getImporterName().send_keys(importername)

    def enterSelectingImporter(self):
        time.sleep(1)
        self.getSearchingImporterButton().click()
        self.getImporterName()

    def enterSelectedImporter(self, importername):
        self.iterate_through_elements(By.XPATH, self.ALL_IMPORTERS, importername)

    def enterProvideLoopa(self):
        time.sleep(1)
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        self.getProviderSearchButton().click()

    def enterProviderType(self, providertype):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        self.wait_frame_to_be_avaible_and_switch(By.ID, "popupFrame1")
        protye = self.getProviderType()
        drp = Select(protye)
        drp.select_by_visible_text(providertype)

    def enterProviderName(self, provider):
        name = self.getProviderName().send_keys(provider)
        self.getSearchButton().click()

    def enterSelectingProvider(self, provider):
        self.iterate_through_elements(By.XPATH, self.ALL_PROVIDERS, provider)

    def enterAddProvider(self):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        add_provider = self.getAddProvider().click()

    def enterRegimeLoopa(self):
        time.sleep(1)
        regime_loopa = self.getRegimeLoopa()
        regime_loopa.click()

    def enterRegimeSearchLoopa(self):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        self.wait_frame_to_be_avaible_and_switch(By.ID, "popupFrame1")
        self.getRegimeSearchLoopa().click()
    def enterAllRegimes(self, regime):
        self.iterate_through_elements(By.XPATH, self.ALL_REGIMES, regime)

    def enterProductLoopa(self):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        self.getProductLoopa().click()

    def enterProductName(self, productName):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        self.wait_frame_to_be_avaible_and_switch(By.ID, "popupFrame1")
        product_name = self.getProductName()
        product_name.send_keys(productName)

    def enterProductSearch(self):
        self.getSearchButtonProduct().click()
    def enterAllProducts(self, productName):
        self.iterate_through_elements(By.XPATH, self.ALL_PRODUCTS, productName)

    def enterProductState(self, state):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        product_state = self.getProductState()
        drp = Select(product_state)
        drp.select_by_visible_text(state)
        time.sleep(1)

    def enterFOB(self, fobprice):
        fob_field = self.getFob()
        fob_field.click()
        fob_field.send_keys(fobprice)

    def enterProductWeight(self, weight):
        weight_product = self.getWeightProduct()
        weight_product.click()
        weight_product.send_keys(weight)

    def enterProductQuantity(self, quantity):
        product_qa = self.getProductQa()
        product_qa.click()
        product_qa.send_keys(quantity)

    def enterProductDescriptio(self, desc):
        description = self.getProductDescriptio()
        description.click()
        description.send_keys(desc)

    def enterAddProduct(self):
        add = self.getAddProduct()
        add.click()
        time.sleep(1)

    def enterDocumentType(self, docutype):
        dot = self.getDocumentType()
        drp = Select(dot)
        drp.select_by_visible_text(docutype)

    def enterRefDocNumber(self, ref):
        ref_num = self.getRefDocNumber()
        ref_num.send_keys(ref)

    def enterIssuedEmitido(self, emitido):
        issued = self.getIssuedEmitid()
        issued.click()
        issued.send_keys(emitido)

    def enterMail(self, mail):

        mail_field = self.getMail()
        mail_field.click()
        mail_field.send_keys(mail)

    def enterPhone(self, phone1):
        phone_field = self.getPhone()
        phone_field.click()
        phone_field.send_keys(phone1)

    def enterAddDocument(self):
        add_button = self.getAddDocument()
        add_button.click()
        time.sleep(1)

    def enterAttachField(self):
        attachment = self.getAttachField()
        file_path = os.path.abspath("data/[FAC-001] - Prueba Factura.jpg")
        attachment.send_keys(file_path)
        time.sleep(1)

    def enterFleteField(self, flete):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        flete_field = self.getFleteField()
        flete_field.click()
        flete_field.send_keys(flete)

    def enterInsuranceField(self, insurance):
        flete_field = self.getInsuranceField()
        flete_field.click()
        flete_field.send_keys(insurance)

    def enterGrossWeightField(self, bruto):
        flete_field = self.getGrossWeightField()
        flete_field.click()
        flete_field.send_keys(bruto)

    def enterGenDeclaNumber(self):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        declaGenbox = self.getGenDeclaNumber()
        declaGenbox.click()

    def enterDecNumVal(self):
        element = self.getDecNumVal()
        value = element.get_attribute("value")
        print("Declaración Generada: ", value)
        return value

    def enterSubmitDeclaButton(self):
        submit = self.getSubmitDeclaButton()
        submit.click()
    def enterNobuttonSubmit(self):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        self.wait_frame_to_be_avaible_and_switch(By.ID, "popupFrame1")
        no_button = self.getNobuttonSubmit()
        no_button.click()

    def enterYesbuttonSubmit(self):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        self.wait_frame_to_be_avaible_and_switch(By.ID, "popupFrame2")
        yes = self.getYesbuttonSubmit()
        yes.click()

    def enterOkButtonafterSubmit(self):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        self.wait_frame_to_be_avaible_and_switch(By.ID, "_MESSAGE_IFR_MESSAGE_")
        ok_button = self.getMessageSubmitOk()
        ok_button.click()

    def enterInvoiceGeneration(self):
        self.driver.switch_to.default_content()
        self.wait_frame_to_be_avaible_and_switch(By.ID, "contentFrame")
        element = self.getInvoiceGeneration()
        value = element.get_attribute("value")
        print("Factura Generada: ", value)
        return value

    ##################################### BUSINESS METHODS #########################################

    def IntroAdminTypeInvoiceDeposito(self, administracion, tipo_manifiesto, factura, administracion_destino, nombre_destino):
        self.enterDecAdminLoopa()
        self.enterSearchAdminButton()
        self.enterAllAdministrations(administracion)
        self.enterSelectingManType(tipo_manifiesto)
        self.enterInvoiceField(factura)
        self.enterDepartLoopa()
        self.enterDestinyAdmin(administracion_destino)
        self.enterStore(nombre_destino)

    def ImportadorTipo(self, tipo_importador, nombre, seleccionar):
        self.enterImporterLoopa()
        self.enterImporterType(tipo_importador)
        self.enterImporterName(nombre)
        self.enterSelectingImporter()
        self.enterSelectedImporter(seleccionar)

    def Provider(self, tipoProveedor, Proveedor, Seleccionar):
        self.enterProvideLoopa()
        self.enterProviderType(tipoProveedor)
        self.enterProviderName(Proveedor)
        self.enterSelectingProvider(Seleccionar)
        self.enterAddProvider()

    def flujo_importador_proveedor(self, tipo_importador, nombre, seleccionar, tipo_proveedor, proveedor, selecc_proveedor):
        try:
            # Intentar Importador
            self.ImportadorTipo(tipo_importador, nombre, seleccionar)
            print("Importador ejecutado correctamente")
        except Exception as e:
            print(f"Importador bloqueado o preseleccionado: {e}")
        finally:
            # Provider siempre se ejecuta
            self.Provider(tipo_proveedor, proveedor, selecc_proveedor)
            print("Provider ejecutado correctamente")


    def Regime(self, Regimen):
        self.enterRegimeLoopa()
        self.enterRegimeSearchLoopa()
        self.enterAllRegimes(Regimen)

    def Producto(self, NombreProducto, Seleccionar, Estado, FOB, Peso, Cantidad, Descripcion):
        self.enterProductLoopa()
        self.enterProductName(NombreProducto)
        self.enterProductSearch()
        self.enterAllProducts(Seleccionar)
        self.enterProductState(Estado)
        self.enterFOB(FOB)
        self.enterProductWeight(Peso)
        self.enterProductQuantity(Cantidad)
        self.enterProductDescriptio(Descripcion)
        self.enterAddProduct()

    def Documento(self, TipoDocumento, Referencia, Emitido, correo, Telefono):
        self.enterDocumentType(TipoDocumento)
        self.enterRefDocNumber(Referencia)
        self.enterIssuedEmitido(Emitido)
        self.enterMail(correo)
        self.enterPhone(Telefono)
        self.enterAddDocument()
    def FleteSeguroPeso(self, Flete, Seguro, PesoBruto):
        self.enterFleteField(Flete)
        self.enterInsuranceField(Seguro)
        self.enterGrossWeightField(PesoBruto)

    def GenerandoDeclaracion(self):
        self.enterGenDeclaNumber()
        self.enterDecNumVal()
    def PresentandoDeclaracion(self):
        self.enterSubmitDeclaButton()
        self.enterNobuttonSubmit()
        self.enterYesbuttonSubmit()
        self.enterOkButtonafterSubmit()

