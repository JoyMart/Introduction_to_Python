#
#
#                       Creating html file from python
#
#

f = open("html_assignment.html", "x")

file = open("html_assignment.html", 'a')
file.write("<html> \n<body> \nStay tuned for our amazing summer sale! \n</body> \n</html>")
file.close()

webopen = open("html_assignment.html", "r")
print(webopen.read())

