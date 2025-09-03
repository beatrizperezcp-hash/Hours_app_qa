from selenium.webdriver.common.by import By

from helper.utils import Utilspageobject as utils

class Mainfunctionspageobject(utils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.dropdown_elements =(By.XPATH, '//label//*[normalize-space(text())="Inicio"]/following::div[@data-baseweb="select"]')


    def open_url(self, url):
        self.driver.get(url)

    def select_option_dropdown(self):
        self.wait_until_visible(self.dropdown_elements)

