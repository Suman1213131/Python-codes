students=[]
 
def start():
    print(" Student management program")
    print(" --------------------------")
    print("")
    print("Main menu")
    print("---------")
    print("")
    
    print("1. Add a student to the list")
    print("2. List students")
    print("3. Sort students into alphabetical order")
    print("4. Clear the List")
    print("5. Exit the program")
    print("6. List options again")
    print ("")
    
start()
while True:
    option=input('enter the option to perform> ')
    if option == '1':
        students.append(input("Enter the student's name> "))
        print(students[-1],'has been added to the list')
    elif option == '2':
        n = 0
        if len(students) > 0:
            stt = 'There are '+str(len(students))+' students in the list including:'
            print("")
            print(stt)
            print("Student No.        Name")
            print("-----------------------")
            for i in students:     
                n+=1
                print(n,"                ",i)
                
        else:
            print('there are no students in the list')
    elif option =='3':
        students=sorted(students)
        print('list sorted')
    
    elif option =='4':
        students=[]
        print('List Clear')
    elif option=='5':
        exit()
    elif option =='6':
        start()
    else:
        print('option does not exist or entered wrong')
