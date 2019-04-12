import subprocess
import getpass
import os

def uploadApp(fileName):
	cd = os.path.dirname(os.path.abspath(__file__))
	subprocess.call(cd + "/gitUpload.sh " + fileName + " " + "Generated Creation:  " + fileName + " by " + getpass.getuser(), shell=True)
