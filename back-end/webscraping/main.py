from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import pandas as pd

web_url = "https://www.cleanmetrics.com/carbonscopedata/browsepcli.aspx"
groupSelectorName = "ctl00$MainContent$group"
categorySelectorName = "ctl00$MainContent$category"
commoditySelectorName = "ctl00$MainContent$process"

#Initialize Firefox Webdriver, need Geckodriver downloaded and added to path
driver = webdriver.Firefox()
driver.get(web_url)

groupSelector = Select(driver.find_element_by_name(groupSelectorName))

def getOptions(selector, attr) :
    return [o.get_attribute(attr) for o in selector.options]


groupSelector.select_by_value("Food Commodities")
categorySelector = Select(driver.find_element_by_name(categorySelectorName))
categorySelector.select_by_value('Fruits/Berries')
commoditySelector = Select(driver.find_element_by_name(commoditySelectorName))
print(getOptions(commoditySelector))