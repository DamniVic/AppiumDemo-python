#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from appium import webdriver

capabilities = {}
capabilities['platformName'] = 'Android'
capabilities['deviceName'] = 'Android Emulator'
capabilities['platformVersion'] = '4.4.2'
capabilities['unicodeKeyboard'] = 'True'
capabilities['resetKeyboard'] = 'True'
capabilities['appPackage'] = 'com.hskj.damnicomniplusvic.aar'
capabilities['appActivity'] = '.activity.MainActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
button = driver.find_element_by_name('button')
swip = driver.find_element_by_class_name('android.widget.ImageView')
point = swip.location
driver.swipe(point['x']+10, point['y']+10, 500, 800, 3000)
button.click()
driver.quit()
