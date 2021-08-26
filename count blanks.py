name=input("Enter name of the File: ")#Taking the name of the file from the user
alpha = name + ".txt"

try:#Trying to open the file to check if it exists
    file1=open(alpha,'r')
    file1.close()

except:#If the file does not exist then it has been made
    file1=open(alpha,'w+')
    file1.write("")
    file1.close()

count_blanks = 0
data = input("Enter the data you want checked: ")#Gettimg data from the user
file1 = open(alpha,'w')
file1.write(data)#Writing the data into the file
file1.close()
file2 = open(alpha,'r')
for i in file2.read():
    if i == " ":
        count_blanks+=1
print(count_blanks)        
    
