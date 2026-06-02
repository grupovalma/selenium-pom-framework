from selenium.webdriver.support.ui import Select
class Utils:
       ### 58 Printing PIN (SEARCHING PIN INFO HOMEPAGE)
    def PrintingandAssePin(self):
        self.driver.switch_to.default_content()
        self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "contentFrame")))
        Id_pin = self.wait.until(EC.element_to_be_clickable((By.ID, "ctl00_ContentsHolder_txtPinNo"))).get_attribute("value")

        assert Id_pin.strip(), "ERROR: No se Genero el Pin"
        print("Generated Pin No: ", Id_pin)
        print("---------------------------------------------------------------")