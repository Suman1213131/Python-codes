print("Opening file marks.txt for writing\n")
 
file = open("marks.txt","w")
 
amount = int(input('Enter the number of student marks to store> '))
 
marks = []
 
for i in range(amount):
    marks.append(int(input('Enter a Mark> ')))
 
for i in range(len(marks)):
    file.write(f"{marks[i]}\n")
 
print("\nSaved marks to marks.txt")
 
file.close()
 
print(f'\nClosing file')
