import unittest
import pyautogui

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mpmath import *
import math
import numpy as np

import time

import json
# This script downloads the Nimble data and LTSpice data from Beta-tools-analog
# Note: This script uses PYAUTOGUI which controls the mouse for the drag and drop action.
# While this script is running, please do not move the mouse

class TestNimble(unittest.TestCase):

    def setUp(self):
        # driver instance
        self.driver = webdriver.Chrome()
        with open(r'amptf.json') as d:
            self.nimbleData = json.load(d)['Nimble'][0]

    def test_export(self):
        driver = self.driver
        driver.set_window_size(1920, 1080)
        driver.get('https://beta-tools.analog.com/noise/')

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body.ember-application:nth-child(2) div.consent-dialog:nth-child(1) div.modal.fade.in.show div.modal-dialog div.modal-content div.modal-body div.short-description > a.btn.btn-success:nth-child(2)"))).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#choose-sensor-tab"))).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#svg2005"))).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#resistance-1-input"))).send_keys(Keys.CONTROL + "a")
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#resistance-1-input"))).send_keys(Keys.DELETE)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#resistance-1-input"))).send_keys(self.nimbleData['resistance_input'])
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#capacitance-1-input"))).send_keys(Keys.CONTROL + "a")
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#capacitance-1-input"))).send_keys(Keys.DELETE)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#capacitance-1-input"))).send_keys(self.nimbleData['capacitance_input'])
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body.ember-application.modal-open:nth-child(2) div.adi-modal:nth-child(4) div.modal.fade.in.show:nth-child(1) div.modal-dialog div.modal-content form.modal-footer div.button-row > button.btn.btn-primary:nth-child(1)"))).click()
        time.sleep(1)
        pyautogui.moveTo(930, 300)
        pyautogui.dragTo(930, 400, button='left', duration=0.5)

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#amp-gain-2"))).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#amp-gain-2"))).send_keys(Keys.DELETE)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#amp-gain-2"))).send_keys(self.nimbleData['gain'])
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#amp-gain-2"))).send_keys(Keys.ENTER)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tspan2988-5"))).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#filter-0"))).send_keys(self.nimbleData['device'])
        driver.execute_script("document.querySelector('div.slick-cell.l0.r0.frozen').click();")
        driver.execute_script("document.querySelector('.modal-footer button.btn-primary').click();")
        time.sleep(0.2)
        driver.execute_script("document.querySelector('.modal-footer button.btn-primary').click();")
        time.sleep(0.5)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#next-steps-tab"))).click()
        time.sleep(1)
        # url = driver.current_url()
        # f=open('deviceurl.txt','a')
        # f.write(url)
        # f.close()
        l= driver.current_url
        device_url = self.nimbleData['device']+'URL.txt'
        with open(device_url, 'w') as f:
            f.write(l)
        print(l)
        time.sleep(1)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body.ember-application:nth-child(2) div.tab-content:nth-child(2) div.download-area div.download-individual-buttons div.download-button-row:nth-child(1) button.btn.btn-primary:nth-child(1) > span:nth-child(1)"))).click()
        time.sleep(1)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body.ember-application:nth-child(2) div.tab-content:nth-child(2) div.download-area div.download-individual-buttons div.download-button-row:nth-child(1) button.btn.btn-primary:nth-child(2) > span:nth-child(1)"))).click()

        time.sleep(3)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

# WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ""))).click()

# ada4254
# 1/16
