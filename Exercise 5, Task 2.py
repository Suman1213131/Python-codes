while True:
    amount = int(input('Enter the number of student marks> '))
    marks=[]
    for i in range(amount):
        marks.append(int(input('Please enter mark> ')))
    print('\nThe average mark is '+ str(sum(marks)/len(marks)))
    print('The minimum mark is '+ str(sorted(marks)[0]))
    print('The Maximum mark is '+ str(sorted(marks)[-1]))
    failpass='\nStudent no.\tMark\tResult\n'
    iter=1
    for i in marks:
        failpass=failpass+str(iter)+'\t\t'+str(i) + '\t\t'+('Fail' if i < 40 else 'Pass')+'\n'
        iter=iter+1
    print(failpass)
 
    marks=[]

