import pywinauto.keyboard
import pywinauto.mouse
import os
import time
import json

# This script runs the LTSpice AC_Simulation to get the V(out)
with open(r'inAMPNoise.json') as d:
    nimbleData = json.load(d)['Nimble'][0]

os.startfile(nimbleData['ltspice']+ '\\' + nimbleData['device'] + '\\' + 'Noise_Simulation.asc')

pywinauto.keyboard.send_keys("%{S}")
pywinauto.keyboard.send_keys("{R}")
time.sleep(0.5)
pywinauto.keyboard.send_keys("%{V}")
pywinauto.keyboard.send_keys("{V}")
pywinauto.keyboard.send_keys("{DOWN}")
pywinauto.keyboard.send_keys("{DOWN}")
pywinauto.keyboard.send_keys("{DOWN}")
pywinauto.keyboard.send_keys("{ENTER}")
time.sleep(0.5)
pywinauto.keyboard.send_keys("^{TAB}")
pywinauto.mouse.right_click(coords=(50, 300))
pywinauto.keyboard.send_keys("{TAB}")
pywinauto.keyboard.send_keys("{TAB}")
pywinauto.keyboard.send_keys("{TAB}")
pywinauto.keyboard.send_keys("{TAB}")
pywinauto.keyboard.send_keys("{TAB}")
pywinauto.keyboard.send_keys("{SPACE}")
pywinauto.keyboard.send_keys("{ENTER}")
pywinauto.keyboard.send_keys("%{F}")
pywinauto.keyboard.send_keys("{E}")
pywinauto.keyboard.send_keys("{ENTER}")
pywinauto.keyboard.send_keys("%{F4}")

time.sleep(0.5)

extra_files_remove = nimbleData['ltspice'] + nimbleData['device']
os.remove(extra_files_remove + '\\' + 'AC_Simulation.asc')
os.remove(extra_files_remove + '\\' + 'Noise_Simulation.asc')
os.remove(extra_files_remove + '\\' + 'Transient_Simulation.asc')
os.remove(extra_files_remove + '\\' + 'Noise_Simulation.log')
os.remove(extra_files_remove + '\\' + 'Noise_Simulation.raw')
os.remove(extra_files_remove + '\\' + 'Noise_Simulation.op.raw')