selenium-pom-framework Portfolio project showcasing QA Automation skills with Python, Selenium, Pytest, POM

QA Automation Framework
Overview

This project automates the generation of test PINs required for integration testing between different systems.
Previously, testers had to manually create import declarations, retrieve generated invoices, and generate payment PINs. 
This automation eliminates the manual effort by executing the complete workflow end-to-end.

Workflow:

•	Login using secure credentials managed through GitHub Secrets.
•	Create an import declaration.
•	Retrieve the generated declaration and invoice.
•	Navigate to the payment module.
•	Generate a payment PIN.
•	Repeat the process automatically through Pytest execution.
•	Display generated PINs in the execution output.

Technologies: 

•	Python
•	Selenium WebDriver
•	Pytest
•	Page Object Model (POM)
•	GitHub Actions
•	Chrome Headless
•	GitHub Secrets

CI/CD The automation runs automatically through GitHub Actions on a scheduled basis using Ubuntu runners, Chrome Headless, and Pytest.
xvfb-run -a pytest -s

Test Coverage The repository contains an end-to-end test that reproduces the complete workflow previously performed manually by testers.

Framework Structure: 

pages/          Pages Object Classes
tests/          Test cases 
utilities/      Reusable helper methods
data/           Test Data
configfiles/    Configuration Files
base/           Base classes and driver setup
.github/        Github Actions CI/CD pipeline

Skills demonstrated:

Selenium
Pytest test execution
Page Object Model - POM
Github Actions CI/CD
Secure credential management with Github Secrets
End to end business workflow
