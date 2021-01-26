
import os
from sys import platform
import subprocess

if platform == "linux" or platform == "linux2" or platform == "darwin":
    os.system('pkill scrcpy')
    os.system('pkill adb')
    os.system("scrcpy --max-size 960")
elif platform == "win32":
    os.system('taskkill /IM scrcpy.exe /F')
    os.system('taskkill /IM adb.exe /F')
    dirpath = os.path.dirname(os.path.abspath(__file__))
    subprocess.Popen(["powershell", "-f", f"{dirpath}/stfservice.ps1"])
    os.system("scrcpy --max-size 960")