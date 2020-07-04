from time import sleep

from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get("https://shimo.im")
    browser.maximize_window()
    browser.find_elements_by_xpath('//*[@class="entries"]//button')[1].click()
    browser.find_element_by_xpath('//*[@type="mobileOrEmail"]//input').click().send_keys("qilaidihaha@gmail.com")
    sleep(1)
except Exception as e:
    print(e)
