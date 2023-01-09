print("Opening marks.txt for reading\n")
 
marks = []
 
with open('marks.txt','r') as file:
    for line in file:
        marks.append(int(line.rstrip('\n')))
 
 
average_mark = sum(marks) / len(marks)
max_mark = max(marks)
min_mark = min(marks)
 
for i in range(len(marks)):
    if marks[i] >= 40:
        print(f"Read mark {marks[i]} : result is Pass")
    elif marks[i] < 40:
        print(f"Read mark {marks[i]} : result is Fail")
 
print("\nRead marks from file")
 
file.close()
 
print(f'\nClosing file')
