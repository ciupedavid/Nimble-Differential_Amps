import unittest
import pyautogui
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from numpy import *
import math
import time
from decimal import Decimal

class TestNimble(unittest.TestCase):

    def setUp(self):
        # Chrome Driver instance
        self.driver = webdriver.Chrome()
        #driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_export(self):
        driver = self.driver
        driver.set_window_size(1920, 1080)

        # USER VARIABLES:
        #Sensor
        resistance_input = "1"
        capacitance_input = "1f"
        #Configure Amplifier Stage
        gain = "2"
        device = "LTC6228"
        rvalue = "500k" # issues when changing from 2.74 to 2.76
        c2value = "1.5p"
        
        #converting kino, Mega
        d1 = {'k': 1000,'M': 1000000}
        def text_to_num1(text):
            if text[-1] in d1:
                num, magnitude = text[:-1], text[-1]
                return float(num) * d1[magnitude]
            else:
                return Decimal(text)
        new_rvalue = text_to_num1(rvalue)

        #converting from femto, pico, nano, micro
        d2 = {'f': 0.000000000000001, 'p':0.000000000001, 'n':0.000000001, 'u':0.000001}
        def text_to_num2(text):
            if text[-1] in d2:
                num, magnitude = text[:-1], text[-1]
                return float(num) * d2[magnitude]
            else:
                return Decimal(text)
        new_c2value = text_to_num2(c2value)
        
        #Configure Filter Stage
        type = "high pass"
        spec = "1st order"
        filter_freq = 100 #100hz
        circuit_RC = "1.07kΩ"

        # RVALUE Value to Position
        # If the value is less than or equal to 0 then we use minpos  
        def val_to_pos_rvalue(value):
            minpos = 1
            maxpos = 10000
            minval = math.log(10)
            maxval = math.log(10000000)
            scale = (maxval - minval) / (maxpos - minpos)
            global rposition
            rposition = minpos + (math.log(value) - minval) / scale
            return (rposition)
        val_to_pos_rvalue(new_rvalue)
        
        # C2 Value to Position
        def val_to_pos_c2value(value):
            minpos = 1
            maxpos = 10000
            minval = math.log(1e-13)
            maxval = math.log(0.000001)
            scale = (maxval - minval) / (maxpos - minpos)
            global c2position
            c2position = minpos + (math.log(value) - minval) / scale
            return (c2position)
        val_to_pos_c2value(new_c2value)

        
        # Nimble Beta Website:
        driver.get('https://beta-tools.analog.com/noise/')
        # Accept cookies
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body.ember-application:nth-child(2) div.consent-dialog:nth-child(1) div.modal.fade.in.show div.modal-dialog div.modal-content div.modal-body div.short-description > a.btn.btn-success:nth-child(2)"))).click()
        # Select sensor tab
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#choose-sensor-tab"))).click()
        # Select Voltage sensor 
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#svg123"))).click()
        # Input resitance and capacitance
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#resistance-input"))).send_keys(Keys.CONTROL + "a")
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#resistance-input"))).send_keys(Keys.DELETE)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#resistance-input"))).send_keys(resistance_input)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#capacitance-input"))).send_keys(Keys.CONTROL + "a")
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#capacitance-input"))).send_keys(Keys.DELETE)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#capacitance-input"))).send_keys(capacitance_input)
        driver.find_element(By.CSS_SELECTOR, "body.ember-application.modal-open:nth-child(2) div.adi-modal:nth-child(4) div.modal.fade.in.show:nth-child(1) div.modal-dialog div.modal-content form.modal-footer div.button-row > button.btn.btn-primary:nth-child(1)").click()

        # Drag and Drop Amplifier
        pyautogui.moveTo(1150, 400, 1)
        pyautogui.dragTo(1150, 500, button='left', duration=0.5)
        
        # Amp Configuration
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#amp-gain-2"))).clear()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#amp-gain-2"))).send_keys(gain)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#amp-gain-2"))).send_keys(Keys.ENTER)
        
        # Select specific AMP
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#text6747-2-6 > tspan.schematic-edit-icon.schematic-part-edit-selection-link.schematic-edit-selection-link"))).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#filter-0"))).send_keys(device)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#device-table > div.slick-pane.slick-pane-top.slick-pane-left > div.slick-viewport.slick-viewport-top.slick-viewport-left > div > div"))).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#partSelectModal2 > div.modal.fade.in.show > div > div > form > div > button.btn.btn-primary"))).click()

        # Resitance slider value
        self.scrollToRValue(rposition, driver)
        time.sleep(2)
        
        # C2 slider value
        self.scrollToC2Value(c2position, driver)
        time.sleep(2)

        # Use this Amplifier button
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#config-signal-chain-item-modal > div.modal.fade.in.show > div > div > form > div > button.btn.btn-primary"))).click()

        # Drag and drop Load Filther
        pyautogui.moveTo(1250, 400, 1)
        pyautogui.dragTo(1250, 500, button='left', duration=0.5)

        # Configure Filter Stage
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#single-stage-design-button"))).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#hp-se-wiring-button"))).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#filter-order-radio-group > div:nth-child(1) > label > input[type=radio]"))).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#fp-input"))).send_keys(Keys.CONTROL + "a")
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#fp-input"))).send_keys(Keys.DELETE)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#fp-input"))).send_keys(filter_freq)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#config-signal-chain-item-modal > div.modal.fade.in.show > div > div > div.modal-body > div > div.top-area > section.config-section > div > div.sub-tab-content-container > button.tab-button-area.enabled.next"))).click()
        
        # Load Filter slider value
        time.sleep(2)
        filter_slider = driver.find_element(By.CSS_SELECTOR, "#rc-cgov-slider")
        move = ActionChains(driver)
        move.click_and_hold(filter_slider).move_by_offset(70, 0).release().perform()
        time.sleep(2)

        # Use this Filter Circuit button
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#config-signal-chain-item-modal > div.modal.fade.in.show > div > div > form > div > button.btn.btn-primary"))).click()
        
        #Select Next Steps tab
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#next-steps-tab"))).click()

        #download data
        #WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#next-steps-container > div.download-area > div.download-individual-buttons > div:nth-child(1) > button:nth-child(1) > span"))).click()
        #WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#next-steps-container > div.download-area > div.download-individual-buttons > div:nth-child(1) > button:nth-child(2) > span"))).click()
        
        #download all data
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#next-steps-container > div.download-area > div.download-all-button"))).click()
        WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "#downloading-modal")))

    @staticmethod
    def scrollToRValue(value: int, driver):
        driver.execute_script(f"document.querySelector('#rscale-slider').value = {rposition}; document.querySelector('#rscale-slider').dispatchEvent(new Event('input'));")
         
    @staticmethod
    def scrollToC2Value(value: int, driver):
        driver.execute_script(f"document.querySelector('#c2-slider').value = {c2position}; document.querySelector('#c2-slider').dispatchEvent(new Event('input'));")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
