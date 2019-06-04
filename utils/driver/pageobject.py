# -- encoding:utf-8 --

from utils.driver.webdriver import driver
from utils.logs import debug

class PageObject():
    url = None
    page_flag_xpath = None
    page_flag_keyword = None

    def __init__(self):
        self.driver = driver
        debug("PageObject -> %s 获取当前driver的实例" % driver)

    def open_and_check(self, url):
        debug("PageObject -> %s 打开并检测指定url页面")
        self.driver.get(url)

    def check_if_page_opened(self):
        flag_element = self.driver.find_element_by_xpath(self.page_flag_xpath)
        if self.page_flag_keyword == flag_element.text:
            return True
        else:
            return False
