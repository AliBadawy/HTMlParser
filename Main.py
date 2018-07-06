import HTMLFunctions



#Create the file
FileName = input("Enter the file name : ")
htmlFile = open(FileName+".HTML","w+")

#Declare the type
Decleration = "<!doctype html>"
htmlFile.write(Decleration+"\n")

#HTML ELEMENT Starting
StartingHTML="<html>"
htmlFile.write(StartingHTML)
#Head section

Title = input("Enter the Title : ")
inFile = ("<head>"+"\n"+"<title>"+"\n"+Title+"\n"+"</title>"+"\n"+"</head>")
htmlFile.write(inFile)

# Showing available options
Tags = ["Text", "paragrahp"]
counter = 0
for i in Tags:
    counter = counter+1
    print(str(counter)+" )"+i+"\n")


choice = input("Enter your choice ")
# Body section
htmlFile.write("\n"+"<body>")





htmlFile.write("\n"+"</body>")

#HTML Element Closing
ClosingHTML="</html>"
htmlFile.write(ClosingHTML)