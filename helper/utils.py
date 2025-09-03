from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Utilspageobject:
    def __init__(self, driver):
        self.driver = driver

    def wait_until_visible(self, element):
     WebDriverWait(self.driver,30).until(EC.presence_of_element_located(element))
