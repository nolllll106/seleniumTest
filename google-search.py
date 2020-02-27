# coding:utf-8
from selenium import webdriver

if __name__ == "__main__":
    driver = webdriver.Chrome()

    driver.get('https://youtube.com/')
    
    searchElement = driver.find_element_by_id("search")
    searchElement.send_keys('千鳥')

    driver.find_element_by_id("search-icon-legacy").click()
    #driver.quit()