name=input("Enter name of the File: ")#Taking the name of the file from the user
alpha = name + ".txt"

try:#Trying to open the file to check if it exists
    file1=open(alpha,"r")
    file1.close()

except:#If the file does not exist then it has been made
    file1=open(alpha,"w+")
    file1.write("")
    file1.close()
    print ("File created")

kent = []
num = int(input("Enter the number of lines you want: "))
for i in range(0,num):
    sent = input ("Enter the line: ")
    kent.append(sent+'\n')

file1 = open(alpha,'w')
file1.writelines(kent)
file1.close()

file2 = open(alpha,'r')
L = file2.readlines()
file2.close()

copy = []

for i in L:
    if i[0].isupper():
        copy.append(i)
        
newname=input("Enter name of the File you want to copy to: ")
beta = newname + ".txt"

try:
    file1=open(beta,"r")
    file1.close()

except:
    file1=open(beta,"w+")
    file1.write("")
    file1.close()
    print ("File created")

file3 = open(beta,'w')
file3.writelines(copy)
print('copied')
file3.close()

file4 = open(beta,'r')
text = file4.readlines()
for i in text:
    print (i)

file4.close()    

