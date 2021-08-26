name=input("Enter name of the File: ")#Taking the name of the file from the user
alpha = name + ".txt"

try:#Trying to open the file to check if it exists
    file1=open(alpha,"r")
    file1.close()

except:#If the file does not exist then it has been made
    file1=open(alpha,"w+")
    file1.write("")
    file1.close()
    
file1 = open(alpha,'w')
data = input("Enter the data you want: ")
file1.write(data)
file1.close()

file2 = open(alpha,'r')
read = file2.read()
L = read.split()
file2.close()

ch = ""
for i in L:
    ch = ch + i + ' '


file3 = open(alpha,'w')
file3.write(ch)
file3.close()

file4 = open(alpha,'r')
print(file4.read())
file4.close()
