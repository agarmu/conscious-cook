global groupSelector, categorySelector, commoditySelector, catOpt, comOpt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import pandas as pd

# Declare constants (not really constants)
web_url = "https://www.cleanmetrics.com/carbonscopedata/browsepcli.aspx"
groupSelectorName = "ctl00$MainContent$group"
categorySelectorName = "ctl00$MainContent$category"
commoditySelectorName = "ctl00$MainContent$process"

#Initialize Firefox Webdriver, need Geckodriver downloaded and added to path
driver = webdriver.Firefox()
driver.get(web_url)

groupSelector = Select(driver.find_element_by_name(groupSelectorName))
categorySelector = Select(driver.find_element_by_name(categorySelectorName))
commoditySelector = Select(driver.find_element_by_name(commoditySelectorName))

def getOptions(selector, attr) :
    return [o.get_attribute(attr) for o in selector.options]

catOpt, comOpt = getOptions(categorySelector, 'value'), getOptions(commoditySelector, 'value')

def redefine():
    global groupSelector, categorySelector, commoditySelector, catOpt, comOpt
    groupSelector = Select(driver.find_element_by_name(groupSelectorName))
    categorySelector = Select(driver.find_element_by_name(categorySelectorName))
    commoditySelector = Select(driver.find_element_by_name(commoditySelectorName))
    catOpt, comOpt = getOptions(categorySelector, 'value'), getOptions(commoditySelector, 'value')

