name=input("Enter name of the File: ")#Taking the name of the file from the user
alpha = name + ".txt"

try:#Trying to open the file to check if it exists
    file1=open(alpha,"r")
    file1.close()

except:#If the file does not exist then it has been made
    file1=open(alpha,"w+")
    file1.write("")
    file1.close()


upper = 0
lower = 0
num = 0

file1 = open(alpha,'w')
data = input("Enter the Data you want checked: ")
file1.write(data)
file1.close()

file2 = open(alpha,'r')
stuff = file2.read()
file2.close()

for i in stuff:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    elif i.isnumeric():
        num+=1


print("The number of upper letters are: ",upper)        
print("The number of lower letters are: ",lower) 
print("The number of numbers are: ",num)         
