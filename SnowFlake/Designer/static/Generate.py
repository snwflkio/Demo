import re

#####################################################################
# Function to parse input HTML and remove "section" div class to
# extract the newly formatted HTML. Then draggable options are 
# stripped to remove the ability to move the components.
#
# Takes input as parameter (HTML to parse)
#####################################################################
def parseHTML(inp):
    htmlStartTemplate = "<html>\n<head>\n<script src=\"./test.js\"></script>\n<link rel=\"stylesheet\" href=\"./test.css\"/>\n</head>\n<body>\n<div class=\"main\">\n"
    re.DOTALL
    newHtml = inp
    newHtml = re.sub(r"ondrop=\"drop\(event\)\"", "", newHtml)
    newHtml = re.sub(r"ondragover=\"allowDrop\(event\)\"", "", newHtml)
    newHtml = re.sub(r"draggable location", "", newHtml)
    newHtml = htmlStartTemplate + newHtml
    f = open("files/new.html","w+")
    f.write(newHtml)
    f.write("</div>\n</body>\n</html>")
    f.close()
    print("New HTML file generated.")

#####################################################################
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
