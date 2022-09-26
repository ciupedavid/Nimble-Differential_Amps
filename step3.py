import pywinauto.keyboard
import os
import time

# Run LTSPICE

os.startfile(r'C:\Users\davciupe\Downloads\AC_Simulation.asc')
pywinauto.keyboard.send_keys("%{S}")
pywinauto.keyboard.send_keys("{R}")
time.sleep(1)
pywinauto.keyboard.send_keys("%{V}")
pywinauto.keyboard.send_keys("{V}")
pywinauto.keyboard.send_keys("{DOWN}")
pywinauto.keyboard.send_keys("{DOWN}")
pywinauto.keyboard.send_keys("{DOWN}")
pywinauto.keyboard.send_keys("{UP}")
pywinauto.keyboard.send_keys("{ENTER}")
time.sleep(1)
pywinauto.keyboard.send_keys("^{TAB}")
pywinauto.keyboard.send_keys("%{F}")
pywinauto.keyboard.send_keys("{E}")
pywinauto.keyboard.send_keys("{ENTER}")
pywinauto.keyboard.send_keys("%{F4}")