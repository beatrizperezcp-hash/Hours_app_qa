from selenium.webdriver.common.by import By

from helper.page_objects.main_functions_poo import Mainfunctionspageobject as mainpo
from behave import step

@step("access to the web")
def access_web(context):
 po_main=   mainpo(context.driver)
 po_main.open_url("https://register-hours.onrender.com/")
 po_main.wait_until_visible((By.XPATH, '//label//*[normalize-space(text())="Inicio"]/following::div[@data-baseweb="select"]'))

