students={
    "10101010":{
        "Name":"Amy Harrison",
        "Course":"BIT",
        "Year":1
        },
    "01010101":{
            "Name":"Alexander Moore",
            "Course":"Computer Science",
            "Year":1
            },
    "01110111":{
        "Name":"Jason Marshall",
        "Course":"CIT","Year":2
        },
    "01001110":{
        "Name":"Seren Hussain",
        "Course":"BIT",
        "Year":2
        }
    }
 
print('Student Database Program\n\nThere are '+str(len(students))+' students in the database')
while True:
    stu = input('Enter the student id> ')
    try:
        print('\nFirst name: {name}\nLast name: {lname}\nCourse name: {cname}\nYear: {year}'.format(name=students[stu]['Name'].split(' ')[0],lname=students[stu]['Name'].split(' ')[-1],cname=students[stu]['Course'],year=str(students[stu]['Year'])))
        print("")
        print("Student found:")
    except:
        print("")
        print("error!")
        print('Student id',stu,'not found')
