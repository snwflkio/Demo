import re
import os
import datetime
from shutil import copyfile

#####################################################################
# Function to parse input HTML and remove "section" div class to
# extract the newly formatted HTML. Then draggable options are 
# stripped to remove the ability to move the components.
#
# Takes input as parameter (HTML to parse)
#####################################################################
def parseHTML(inp):
    name = 'TODO'
    directory = '../Creations/'
    cd = os.path.dirname(os.path.abspath(__file__))
    time = str(datetime.datetime.now())
    directory += time 
   
    # Create all the directories we need (This is in the directory above the project)
    if not os.path.exists(directory):
        os.makedirs(directory)
    if not os.path.exists(directory + "/wwwroot/"):
        os.makedirs(directory + "/wwwroot/")
    if not os.path.exists(directory + "/wwwroot/css/"):
        os.makedirs(directory + "/wwwroot/css/")
    if not os.path.exists(directory + "/wwwroot/scripts/"):
        os.makedirs(directory + "/wwwroot/scripts/")

    # Copy the manifest         : /wwwroot/manifest.json
    copyfile(cd + '/Assets/manifest.json', directory + "/wwwroot/manifest.json" )
    # Copy the service worker   : /ServiceWorker.json
    copyfile(cd + '/Assets/ServiceWorker.js', directory + "/ServiceWorker.js")
    # Copy the index            : /Index.html
    copyfile(cd + '/Assets/index.html', directory + "/index.html")
    # Copy the assets           : /wwwroot/css/site.css, /wwwroot/js/site.js
    copyfile(cd + '/wwwroot/css/site.css', directory + '/wwwroot/css/site.css')
    copyfile(cd + '/wwwroot/scripts/site.js', directory + '/wwwroot/scripts/site.js')

    # Replace all tags in the files
    updateFile(directory + "/wwwroot/manifest.json", '%NAME%', name)
    updateFile(directory + "/wwwroot/manifest.json", '%SHORT_NAME%', name)
    updateFile(directory + "/wwwroot/manifest.json", '%DESCRIPTION%', "Some random words here")
    updateFile(directory + "/ServiceWorker.js", '%NAME%', name)

    # Update content in HTML
    updateFile(directory + "/index.html", '%CONTENT%', cleanHTML(inp))
    
def cleanHTML(html):
    html = html.replace(' ondrop="drop(event)" ', "")
    html = html.replace('ondragover="allowDrop(event)" ', "")
    html = html.replace('draggable location', "")
    return html

def updateFile(fileName, tag, value):
    with open(fileName, 'r') as f:
       data = f.read()
    data = data.replace(tag, value)
    with open(fileName, 'w') as f:
        f.write(data)
####################################################################
# Use this to manually test function with saved HTML file (test.html)
#####################################################################
# with open ("test.html", "r") as myfile:
#    data=myfile.readlines()
#
# htmlString = ""
# for i in range(0, len(data)):
# 	htmlString += data[i];
#
# parseHTML(htmlString)
