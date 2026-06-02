import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def setup(request):
    options = Options()
    options.add_argument("--headless=new")  # modo headless
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver = webdriver.Chrome()
    driver.get("https://demo.aduanas.gob.do/")
    #driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture
def credentials():
    username = os.environ.get("PINES_USER")
    password = os.environ.get("PINES_PASS")
    viafirma_user = os.environ.get("PINES_USER_VIAFIRMA")
    viafirma_pass = os.environ.get("PINES_PASSW_VIAFIRMA")
    company_name = os.environ.get("COMPANY_NAME")
    supplier = os.environ.get("SUPPLIER_NAME")
    mail_importer = os.environ.get("MAIL_IMPORTER")
    phone_importer = os.environ.get("PHONE_IMPORTER")
    test_admin = os.environ.get("TEST_ADMIN")
    test_warehouse = os.environ.get("TEST_WAREHOUSE")

    # Validaciones básicas
    assert username is not None, "PINES_USER environment variable not set"
    assert password is not None, "PINES_PASS environment variable not set"
    assert viafirma_user is not None, "PINES_USER_VIAFIRMA environment variable not set"
    assert viafirma_pass is not None, "PINES_PASSW_VIAFIRMA environment variable not set"
    assert company_name is not None, "COMPANY_NAME environment variable not set"
    assert supplier is not None, "SUPPLIER_NAME environment variable not set"
    assert mail_importer is not None, "MAIL_IMPORTER environment variable not set"
    assert phone_importer is not None, "PHONE_IMPORTER environment variable not set"
    assert test_admin is not None, "TEST_ADMIN environment variable not set"
    assert test_warehouse is not None, "TEST_WAREHOUSE environment variable not set"

    return {
        "username": username,
        "password": password,
        "viafirma_user": viafirma_user,
        "viafirma_pass": viafirma_pass,
        "company_name": company_name,
        "supplier": supplier,
        "mail_importer": mail_importer,
        "phone_importer": phone_importer,
        "test_admin": test_admin,
        "test_warehouse": test_warehouse
    }

