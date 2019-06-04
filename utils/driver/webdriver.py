# -- encoding:utf-8 --

from utils.abs import Singleton
from config import DRIVER
from selenium import webdriver
from utils.logs import debug

@Singleton
class WebDriver():

    driver = None

    def __init__(self):
        if self.driver == None:
            debug("WebDriver -> 初始化driver: %s" % DRIVER)
            if DRIVER == 'Chrom':
                self.driver = webdriver.Chrome()
            else:
                self.driver = webdriver.Firefox()
        else:
            debug("WebDriver -> %s driver已经实例化。" % DRIVER)

    def get_driver(self):
        debug("WebDriver -> %s 获取并返回当前driver 实例。")
        return self.driver

driver = WebDriver().get_driver()
debug("webdriver.py -> %s 实例化并返回当前driver 实例" % str(driver))