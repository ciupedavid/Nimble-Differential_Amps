import pywinauto.keyboard
import os
import time
import json

# This script runs the LTSpice AC_Simulation to get the V(out)
with open(r'paths.json') as d:
    paths = json.load(d)['Unzip'][0]

os.startfile(paths['LTspice_run'])
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