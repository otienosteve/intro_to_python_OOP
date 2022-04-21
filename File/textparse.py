
# fileData= open("text.txt","r")
# print(fileData.read())

with open("text.txt","r") as content:
   
    ls=[]
    #extract the different lines in that text file
    data=content.readlines()
    for i in data:
        first=i[0].upper()
        editedtxt="*"+first+i[1:len(i)]
        ls.append(editedtxt)
    with open("output.txt","a") as output:
        for i in ls:
            output.write(i)

        
    #capitalize the first word
    #append an *