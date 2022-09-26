import unittest
import pyautogui

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


class TestNimble(unittest.TestCase):

    def setUp(self):
        # driver instance
        self.driver = webdriver.Chrome()

    def test_export(self):
        driver = self.driver
        driver.set_window_size(1920, 1080)
        #driver.maximize_window()

        # resistance input
        resistance_input = "1000"
        # capacitance input
        capacitance_input = "100f"
        # gain
        gain = "1"
        # LT1994 AD8132 AD8476
        device = "AD8132"
        # filter frequency
        frequency_filter = "100"
        # app URL
        driver.get('https://beta-tools.analog.com/noise/')
        time.sleep(2)
        # skip cookies
        driver.find_element(By.CSS_SELECTOR, "body.ember-application:nth-child(2) div.consent-dialog:nth-child(1) div.modal.fade.in.show div.modal-dialog div.modal-content div.modal-body div.short-description > a.btn.btn-success:nth-child(2)").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "#choose-sensor-tab").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "#svg123").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "#resistance-input").send_keys(Keys.CONTROL + "a")
        driver.find_element(By.CSS_SELECTOR, "#resistance-input").send_keys(Keys.DELETE)
        driver.find_element(By.CSS_SELECTOR, "#resistance-input").send_keys(resistance_input)
        driver.find_element(By.CSS_SELECTOR, "#capacitance-input").send_keys(Keys.CONTROL + "a")
        driver.find_element(By.CSS_SELECTOR, "#capacitance-input").send_keys(Keys.DELETE)
        driver.find_element(By.CSS_SELECTOR, "#capacitance-input").send_keys(capacitance_input)
        driver.find_element(By.CSS_SELECTOR, "body.ember-application.modal-open:nth-child(2) div.adi-modal:nth-child(4) div.modal.fade.in.show:nth-child(1) div.modal-dialog div.modal-content form.modal-footer div.button-row > button.btn.btn-primary:nth-child(1)").click()
        time.sleep(2)
        # app URL
        #driver.get('https://beta-tools.analog.com/noise/#session=dKetqSwm6USugQOACQqJGg&step=yIZhPwRQQcODzwYmd9b18Q')
        #time.sleep(7)
        # drag and drop
        pyautogui.moveTo(930, 300)
        pyautogui.dragTo(930, 400, button='left', duration=0.5)
        time.sleep(1)
        # amplifier configuration
        driver.find_element(By.CSS_SELECTOR, "#svg23").click()
        driver.find_element(By.CSS_SELECTOR, "#diff-diff-wiring-button").click()
        driver.find_element(By.CSS_SELECTOR, "body.ember-application:nth-child(2) div.adi-modal.modal-fills-window:nth-child(5) div.modal.fade.in.show:nth-child(1) div.modal-dialog div.modal-content div.modal-body div.configure-amp.configure-signal-chain-item div.top-area section.config-section div.config-area:nth-child(2) div.config-more-inputs div.left-right div.diff-se-amp-types:nth-child(1) > div.adi-radio:nth-child(1)").click()
        time.sleep(1)
        # gain selection
        driver.find_element(By.CSS_SELECTOR, "#amp-gain-2").send_keys(Keys.CONTROL+"a")
        driver.find_element(By.CSS_SELECTOR, "#amp-gain-2").send_keys(Keys.DELETE)
        driver.find_element(By.CSS_SELECTOR, "#amp-gain-2").send_keys(gain)
        time.sleep(1)
       # scale selector

        self.scrollToValue(2574, driver)

        pyautogui.click(595, 685)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "#filter-0").send_keys(device)
        time.sleep(1)
        pyautogui.click(170, 330)
        driver.find_element(By.CSS_SELECTOR, "body.ember-application.modal-open:nth-child(2) div.adi-modal.modal-fills-window:nth-child(5) div.modal.fade.in.show:nth-child(1) div.modal-dialog div.modal-content div.modal-body div.configure-amp.configure-signal-chain-item div.adi-modal:nth-child(5) div.modal.fade.in.show:nth-child(1) div.modal-dialog div.modal-content form.modal-footer div.button-row > button.btn.btn-primary:nth-child(1)").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "body.ember-application:nth-child(2) div.adi-modal.modal-fills-window:nth-child(5) div.modal.fade.in.show:nth-child(1) div.modal-dialog div.modal-content form.modal-footer div.button-row > button.btn.btn-primary:nth-child(1)").click()
        # pyautogui.click(1725,1000)
        time.sleep(1)
        # adding a filter
        pyautogui.moveTo(1000, 310)
        pyautogui.dragTo(1100, 410, button='left', duration=0.5)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "#single-stage-design-button").click()
        driver.find_element(By.CSS_SELECTOR, "#hp-diff-wiring-button").click()
        driver.find_element(By.CSS_SELECTOR, "body.ember-application.modal-open:nth-child(2) div.adi-modal.modal-fills-window:nth-child(5) div.modal.fade.in.show:nth-child(1) div.modal-dialog div.modal-content div.modal-body div.configure-filter.configure-signal-chain-item div.top-area section.config-section div.adi-sub-tab-container div.sub-tab-content-container div.sub-tab-content:nth-child(2) div.sub-tab-input-config div.config-input-row:nth-child(2) div.adi-radio-group > div.adi-radio:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR, "#fp-input").send_keys(Keys.CONTROL+"a")
        driver.find_element(By.CSS_SELECTOR, "#fp-input").send_keys(Keys.DELETE)
        driver.find_element(By.CSS_SELECTOR, "#fp-input").send_keys(frequency_filter)
        time.sleep(1)
        # circuit settings

        time.sleep(1)

        #export data
        driver.find_element(By.CSS_SELECTOR, "#filter-inputs-circuit-tab-button").click()
        time.sleep(2)
        pyautogui.doubleClick(1825, 1038)
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, "#next-steps-tab").click()
        driver.find_element(By.CSS_SELECTOR, "body.ember-application:nth-child(2) div.tab-content:nth-child(2) div.download-area div.download-individual-buttons div.download-button-row:nth-child(1) button.btn.btn-primary:nth-child(1) > span:nth-child(1)").click()
        time.sleep(4)
        driver.find_element(By.CSS_SELECTOR, "body.ember-application:nth-child(2) div.tab-content:nth-child(2) div:nth-child(1) div.download-area div.download-individual-buttons div.download-button-row:nth-child(1) > button.btn.btn-primary:nth-child(2)").click()
        time.sleep(3)

    @staticmethod
    def scrollToValue(value: int, driver):
        driver.execute_script("document.querySelector('#rscale-slider').value = 2574; document.querySelector('#rscale-slider').dispatchEvent(new Event('input'));")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
