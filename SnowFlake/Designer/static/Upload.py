import subprocess
import os

def uploadApp(fileName):
	cd = os.path.dirname(os.path.abspath(__file__))
	subprocess.call(cd + "/gitUpload.sh " + fileName + " " + "First app attempt", shell=True)
