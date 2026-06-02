import pytest
import time
from pages.siga_custom_profile_page import SigaProfile
from pages.siga_generating_pin_page import SigaGenPin
from pages.siga_initial_up_page import SigaUserPass
from pages.siga_main_page import SigaMainMenu
from pages.siga_seaching_pin_page import SigaSearchingPin
from pages.siga_search_statement_ import SigaSearchStatement
from pages.siga_statement_page import SigaStatement
from utilities.utils import Utils
@pytest.fixture(params=["Pin 1", "Pin 2", "Pin 3", "Pin 4", "Pin 5", "Pin 6", "Pin 7", "Pin 8", "Pin 9", "Pin 10"])
def PinRepetition(request):
    print(request.param)
@pytest.mark.usefixtures("setup")
class TestPines:
    def testPinesLocal(self, PinRepetition, credentials):
        ## Username and Password
        ip = SigaUserPass(self.driver)
        try:
            ip.No_Via_Firma_Launch(credentials["username"], credentials["password"])
        except:
            ip.Viafirma(credentials["viafirma_user"], credentials["viafirma_user"], credentials["viafirma_pass"])
        ## Selecting Profile Type
        sp = SigaProfile(self.driver)
        sp.selectingProfile("AGENTE DE ADUANAS", "IMPORTADOR")
        ## Selecting Administration, manifest type, invoice, destination administration, and destination name
        smm = SigaMainMenu(self.driver)
        smm.entertNewDeclButton()
        ss = SigaStatement(self.driver)
        ss.IntroAdminTypeInvoiceDeposito(credentials["test_admin"], "NO MANIFIESTO", "AUTOFAC123",
                                         credentials["test_admin"], credentials["test_warehouse"])
        ### Importer and Supplier
        ss.flujo_importador_proveedor("Empresa Importadora", credentials["company_name"], credentials["company_name"],
                                      "Empresa Proveedora Exterior", credentials["supplier"], credentials["supplier"])
        ### Regime, Declaration
        ss.Regime("DESPACHO A CONSUMO")
        ### Product search fields, Declaration
        ss.Producto("JEANS", "JEANS", "NUEVO", "2500", "100", "3", "Data creada con Selenium")
        ### Documents, including invoices, etc., Declaration
        ss.Documento("FACTURA COMERCIAL", "1234", "Selenium Tester", credentials["mail_importer"], credentials["phone_importer"])
        ### Attached, Freight, Generating and Submitting Declaration
        ss.enterAttachField()
        ss.FleteSeguroPeso("100", "10", "100")
        ss.GenerandoDeclaracion()
        Dec_Number = ss.enterDecNumVal()
        ss.PresentandoDeclaracion()
        ### Looking for an invoice in the tax return
        sis = SigaSearchStatement(self.driver)
        sis.enterSearchDeclaField(Dec_Number)
        sis.AdministracionDeFactura(credentials["test_admin"], credentials["test_admin"])
        sis.enterAllDclaself(Dec_Number)
        invoice = ss.enterInvoiceGeneration()
        sis.enterSubmenuDecField()
        ## Entering the Collection menu and the PIN submenu
        smm.Menues()
        ssp = SigaSearchingPin(self.driver)
        ssp.NuevoyAgregandoPin()
        ## Looking for a company that generates invoices, to create a PIN
        sgp = SigaGenPin(self.driver)
        sgp.ConAgenteSinAgente("Empresa Importadora", credentials["company_name"], credentials["company_name"],
                               invoice)
        ## Presenting Pin
        sgp.PresentandoPin()
        ssp.enterPrintPinId()