name=input("Enter name of the File: ")#Taking the name of the file from the user
alpha = name + ".txt"

try:#Trying to open the file to check if it exists
    file1=open(alpha,"r")
    file1.close()

except:#If the file does not exist then it has been made
    file1=open(alpha,"w+")
    file1.write("")
    file1.close()

l = []
num = int(input("Enter the number of lines you want checked: "))
for i in range(0,num):
    sent = input("Enter the sentance: ")

    l.append(sent+'\n')

file1 = open(alpha,'w')
file1.writelines(l)
file1.close()
count_vowel = 0
ch = 'AEIOUaeiou'

file2 = open(alpha,'r')
L = file2.readlines()

for i in L:
    if i[len(i)-2] in ch:
        count_vowel+=1
       

print("The number of lines ending with vowels are: ",count_vowel)
        
        
