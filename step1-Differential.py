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
        with open(r'step1j.json') as d:
            self.nimbleData = json.load(d)['Nimble'][0]

    def test_export(self):
        driver = self.driver
        driver.set_window_size(1920, 1080)
        # driver.maximize_window()
        driver.get('https://beta-tools.analog.com/noise/')

        #  time.sleep(2)
        # skip cookies
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"body.ember-application:nth-child(2) div.consent-dialog:nth-child(1) div.modal.fade.in.show div.modal-dialog div.modal-content div.modal-body div.short-description > a.btn.btn-success:nth-child(2)"))).click()
        #   time.sleep(2)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#choose-sensor-tab"))).click()
        #  time.sleep(1)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#svg2005"))).click()
        #   time.sleep(1)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#resistance-1-input"))).send_keys(Keys.CONTROL + "a")
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#resistance-1-input"))).send_keys(Keys.DELETE)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#resistance-1-input"))).send_keys(self.nimbleData['resistance_input'])
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#capacitance-1-input"))).send_keys(Keys.CONTROL + "a")
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#capacitance-1-input"))).send_keys(Keys.DELETE)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#capacitance-1-input"))).send_keys(self.nimbleData['capacitance_input'])
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"body.ember-application.modal-open:nth-child(2) div.adi-modal:nth-child(4) div.modal.fade.in.show:nth-child(1) div.modal-dialog div.modal-content form.modal-footer div.button-row > button.btn.btn-primary:nth-child(1)"))).click()
        time.sleep(2)
        # drag and drop
        pyautogui.moveTo(930, 300)
        pyautogui.dragTo(930, 400, button='left', duration=0.5)
        #  time.sleep(1)
        # amplifier configuration
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#diff-se-wiring-button"))).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#diff-diff-wiring-button"))).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"body.ember-application:nth-child(2) div.adi-modal.modal-fills-window:nth-child(5) div.modal.fade.in.show:nth-child(1) div.modal-dialog div.modal-content div.modal-body div.configure-amp.configure-signal-chain-item div.top-area section.config-section div.config-area:nth-child(2) div.config-more-inputs div.left-right div.diff-se-amp-types:nth-child(1) > div.adi-radio:nth-child(1)"))).click()
        #  time.sleep(1)
        # gain selection
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#amp-gain-2"))).send_keys(Keys.CONTROL + "a")
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#amp-gain-2"))).send_keys(Keys.DELETE)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#amp-gain-2"))).send_keys(self.nimbleData['gain'])
        #  time.sleep(1)
        # scale selector

        position = value_to_position(self.nimbleData['scale_selector'])
        self.scrollToValue(position, driver)

        time.sleep(2)
        pyautogui.click(595, 685)
        # time.sleep(1)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#filter-0"))).send_keys(self.nimbleData['device'])
        time.sleep(2)
        pyautogui.click(170, 330)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"body.ember-application.modal-open:nth-child(2) div.adi-modal.modal-fills-window:nth-child(5) div.modal.fade.in.show:nth-child(1) div.modal-dialog div.modal-content div.modal-body div.configure-amp.configure-signal-chain-item div.adi-modal:nth-child(5) div.modal.fade.in.show:nth-child(1) div.modal-dialog div.modal-content form.modal-footer div.button-row > button.btn.btn-primary:nth-child(1)"))).click()
        time.sleep(1)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"body.ember-application:nth-child(2) div.adi-modal.modal-fills-window:nth-child(5) div.modal.fade.in.show:nth-child(1) div.modal-dialog div.modal-content form.modal-footer div.button-row > button.btn.btn-primary:nth-child(1)"))).click()
        pyautogui.click(1725, 1038)
        time.sleep(2)
        # adding a filter
        pyautogui.moveTo(1000, 310)
        pyautogui.dragTo(1100, 410, button='left', duration=0.5)
        time.sleep(1)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#single-stage-design-button"))).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#hp-diff-wiring-button"))).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"body.ember-application.modal-open:nth-child(2) div.adi-modal.modal-fills-window:nth-child(5) div.modal.fade.in.show:nth-child(1) div.modal-dialog div.modal-content div.modal-body div.configure-filter.configure-signal-chain-item div.top-area section.config-section div.adi-sub-tab-container div.sub-tab-content-container div.sub-tab-content:nth-child(2) div.sub-tab-input-config div.config-input-row:nth-child(2) div.adi-radio-group > div.adi-radio:nth-child(1)"))).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#fp-input"))).send_keys(Keys.CONTROL + "a")
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#fp-input"))).send_keys(Keys.DELETE)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#fp-input"))).send_keys(self.nimbleData['filter_frequency'])

        # circuit settings
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"body.ember-application.modal-open:nth-child(2) div.adi-modal.modal-fills-window:nth-child(5) div.modal.fade.in.show:nth-child(1) div.modal-dialog div.modal-content div.modal-body div.configure-filter.configure-signal-chain-item div.top-area section.config-section div.adi-sub-tab-container div.sub-tab-content-container button.tab-button-area.enabled.next:nth-child(3) > div.tab-button.enabled.next"))).click()
        time.sleep(2)

        self.scrollToRCValue(self.nimbleData['rc_scale'], driver)

        # export data
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#filter-inputs-circuit-tab-button"))).click()
        time.sleep(2)
        pyautogui.doubleClick(1825, 1038)
        time.sleep(2)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#next-steps-tab"))).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"body.ember-application:nth-child(2) div.tab-content:nth-child(2) div.download-area div.download-individual-buttons div.download-button-row:nth-child(1) button.btn.btn-primary:nth-child(1) > span:nth-child(1)"))).click()
        time.sleep(4)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"body.ember-application:nth-child(2) div.tab-content:nth-child(2) div:nth-child(1) div.download-area div.download-individual-buttons div.download-button-row:nth-child(1) > button.btn.btn-primary:nth-child(2)"))).click()
        time.sleep(6)

    @staticmethod
    def scrollToValue(value: int, driver):
        driver.execute_script(
            f"document.querySelector('#rscale-slider').value = {value}; document.querySelector('#rscale-slider').dispatchEvent(new Event('input'));")

    @staticmethod
    def scrollToRCValue(value: int, driver):
        driver.execute_script(
            f"document.querySelector('#rc-r1-slider').value = {value}; document.querySelector('#rc-r1-slider').dispatchEvent(new Event('input'));")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()


def value_to_position(value):
    # html/js values
    minpos = 1
    maxpos = 10000
    # slider values
    minimum_slider_value = 10
    maximum_slider_value = 10000000
    # logarith function
    minval = log(minimum_slider_value)
    maxval = log(maximum_slider_value)
    # scale & postion equations
    scale = (maxval - minval) / (maxpos - minpos)
    rposition = minpos + (log(value) - minval) / scale
    return rposition
