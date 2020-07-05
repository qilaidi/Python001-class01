from time import sleep

from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get("https://shimo.im")
    browser.maximize_window()
    browser.find_elements_by_xpath('//*[@class="entries"]//button')[1].click()
    browser.find_element_by_xpath('//input[@name="mobileOrEmail"]').send_keys("qilaidihaha@gmail.com")
    browser.find_element_by_xpath('//input[@name="password"]').send_keys("test123!")
    browser.find_element_by_xpath('//button[@type="black"]').click()
    browser.implicitly_wait(10)
    browser.find_element_by_xpath('//*[@href="/dashboard/favorites"]').click()
except Exception as e:
    print(e)
finally:
    browser.close()
