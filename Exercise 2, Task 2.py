print('Python stores Employee wage calculator program')
print()
num_hours = int(input('please enter the number of hours worked by employee> '))
sales = float(input('please enter the number of sales for employee> £'))
 
wages = 0.0
normal_hours = 0
overtime_hours = 0
commission = 0.0
 
if num_hours <= 40:
    normal_hours = num_hours
    
if num_hours > 40:
    normal_hours = 40
    overtime_hours = num_hours - 40
 
if sales > 1.00 and sales < 99.99:
    commission = sales * 5 / 100.0
 
if sales > 100.0 and sales < 299.99:
    commission = sales * 10 / 100.0
 
if sales > 300.0:
    commission = sales * 15 / 100.0
 
wages = normal_hours * 9.50 + overtime_hours * (9.50 * 1.5) + commission
 
print()
print('Number of hours worked @ normal rate = ', normal_hours, ' x £', 9.50)
print('Number of hours worked @ overtime rate = ', overtime_hours, ' x £', 9.50 * 1.5)
print('comission earned = £', commission)
 
print ('Total wage = £', wages)
