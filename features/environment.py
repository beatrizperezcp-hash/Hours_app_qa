from selenium import webdriver
from docx import  document as dc


def before_all(context):
    context.driver = webdriver.Edge()
    context.driver.maximize_window()

