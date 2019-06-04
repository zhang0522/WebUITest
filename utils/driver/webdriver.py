# -- encoding:utf-8 --

from utils.abs import Singleton
from config import DRIVER
from selenium import webdriver


@Singleton
class WebDriver():

    __driver = None

    def __init__(self):
        if self.__driver == None:
            if DRIVER == 'Chrom':
                self.__driver = webdriver.Chrome()
            else:
                self.__driver = webdriver.Firefox()

    def get_driver(self):
        return self.__driver