import pywinauto.keyboard
import pywinauto.mouse
import os
import time
import json

# This script runs the LTSpice AC_Simulation to get the V(out)
with open(r'inAMPNoise.json') as d:
    nimbleData = json.load(d)['Nimble'][0]

os.startfile(nimbleData['project_location']+ '\\' + nimbleData['device'] + '\\' + 'Noise_Simulation.asc')
time.sleep(0.25)
pywinauto.keyboard.send_keys("%{S}")
pywinauto.keyboard.send_keys("{R}")
time.sleep(1)
pywinauto.keyboard.send_keys("%{V}")
time.sleep(1)
pywinauto.keyboard.send_keys("{V}")
time.sleep(1)
pywinauto.keyboard.send_keys("{DOWN}")
pywinauto.keyboard.send_keys("{DOWN}")
pywinauto.keyboard.send_keys("{DOWN}")
pywinauto.keyboard.send_keys("{ENTER}")
time.sleep(0.25)
pywinauto.keyboard.send_keys("^{TAB}")
time.sleep(0.25)
pywinauto.mouse.right_click(coords=(50, 300))
pywinauto.keyboard.send_keys("{TAB}")
pywinauto.keyboard.send_keys("{TAB}")
pywinauto.keyboard.send_keys("{TAB}")
pywinauto.keyboard.send_keys("{TAB}")
pywinauto.keyboard.send_keys("{TAB}")
pywinauto.keyboard.send_keys("{SPACE}")
pywinauto.keyboard.send_keys("{ENTER}")
pywinauto.keyboard.send_keys("^TAB")
pywinauto.keyboard.send_keys("%{F}")
pywinauto.keyboard.send_keys("{E}")
pywinauto.keyboard.send_keys("{ENTER}")
pywinauto.keyboard.send_keys("%{F4}")

time.sleep(0.5)

extra_files_remove = nimbleData['project_location'] + nimbleData['device']
zip_remove_nimble = extra_files_remove + '\\' + 'Nimble - ' + nimbleData['device'] + ' G' + nimbleData['gain'] + '.zip'
zip_remove_ltspice = extra_files_remove + '\\' + 'LTspice - ' + nimbleData['device'] + ' G' + nimbleData['gain'] + '.zip'
# os.remove(extra_files_remove + '\\' + 'AC_Simulation.asc')
# os.remove(extra_files_remove + '\\' + 'Noise_Simulation.asc')
# os.remove(extra_files_remove + '\\' + 'Transient_Simulation.asc')
# os.remove(extra_files_remove + '\\' + 'Noise_Simulation.log')
# os.remove(extra_files_remove + '\\' + 'Noise_Simulation.raw')
# os.remove(extra_files_remove + '\\' + 'Noise_Simulation.op.raw')
# os.remove(zip_remove_nimble)
# os.remove(zip_remove_ltspice)