name=input("Enter name of the File: ")#Taking the name of the file from the user
alpha = name + ".txt"

try:#Trying to open the file to check if it exists
    file1=open(alpha,"r")
    file1.close()

except:#If the file does not exist then it has been made
    file1=open(alpha,"w+")
    file1.write("")
    file1.close()

vo = ("AEIOUaeiou")
file1 = open(alpha,'w')
data = input("Enter the data: ")
file1.write(data)
file1.close()

file2=open(alpha,'r')
sent = file2.read()
file2.close()

L = sent.split()
ch = ""
diffs = []

for i in L:
    if i[0] not in vo:
        diffs.append(i)
        
for i in diffs:
    ch = ch + i + ' '

file3 = open(alpha,'w')
file3.write(ch)
file3.close()        

file4 = open(alpha,'r')
print(file4.read())
file4.close()
