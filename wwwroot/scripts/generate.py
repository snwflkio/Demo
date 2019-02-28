import re

#####################################################################
# Function to parse input HTML and remove "section" div class to
# extract the newly formatted HTML. Then draggable options are 
# stripped to remove the ability to move the components.
#
# Takes input as parameter (HTML to parse)
#####################################################################
def parseHTML(input):
	htmlStartTemplate = "<html>\n<head>\n<script src=\"./test.js\"></script>\n<link rel=\"stylesheet\" href=\"./test.css\"/>\n</head>\n<body>\n<div class=\"main\">\n"
	newHtmlIndex = input.find("<div class=\"section\">")
	re.DOTALL
	newHtml = input[newHtmlIndex:]
	newHtml = re.sub(r"ondrop=\"drop\(event\)\"", "", newHtml)
	newHtml = re.sub(r"ondragover=\"allowDrop\(event\)\"", "", newHtml)
	newHtml = re.sub(r"draggable location", "", newHtml)
	newHtml = htmlStartTemplate + newHtml
	f = open("new.html","w+")
	f.write(newHtml)
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