# Nimble-Differential_Amps

Python & Libraries Install
Install
Go to the following link to download and install Python.
https://www.python.org/downloads/windows/


Verify
To check if you already have Python on your Windows machine open the command-line applicaiton:

1. Press Win + R
2. Type cmd
3. Press Enter
4. Type python --version
Using the --version switch will show you the version that’s installed. If you see a version less than 3.9.13, which was the most recent version at the time of writing, then you’ll want to upgrade your installation.


Add Python Path to Environment Variables
Setting up the Python path to system variables alleviates the need for using full paths. It instructs Windows to look through all the PATH folders for “python” and find the install folder that contains the python.exe file.

1. Press Win + R
2. Type cmd
3. Press Enter
4. Type sysdm.cpl and click OK This opens the System Properties window
5. Navigate to the Advanced tab and select Environment Variables
6. Under System Variables, find and select the Path variable
7. Click Edit
8. Select the Variable value field. Add the path to the python.exe file preceded with a semicolon (;). For example, in the image below, we have added “;C:\Python34.”
9. Click OK and close all windows


Libraries installation
In order to run the first script, we need to install ChromeDriver to the folder where the project is located. (Unzip the file in the project path.)
The libraries that we used will be installed by opening the comand-line application (Win+R) and typing the following imports:

- pip install selenium
- pip install pyautogui
- pip install pywinauto
- pip install pandas
- pip install openpyxl


NOTE:  The window resolution for chrome is set at 1920 x 1080. The Scale and Layout for the monitor should be at 100%.
