markOne= float(input ("enter your first mark> ")) 
weight_of_first_mark = float(input ("enter your weight of the first mark> ")) 
total_markOne = ((markOne/100) * weight_of_first_mark) 
print(" ")
 
markTwo= float(input ("enter your second mark> ")) 
weight_of_second_mark = float(input ("enter your weight of the second mark> ")) 
total_markTwo = ((markTwo/100) * weight_of_second_mark) 
print(" ") 
 
markThree= float(input ("enter your third mark> ")) 
weight_of_third_mark = float(input ("enter your weight of the third mark> ")) 
total_markThree = ((markThree/100) * weight_of_third_mark) 
 
 
print("")
print("The overall mark for the marks and weight input is")
print("Mark1 =", markOne,"Weight1 =", weight_of_first_mark,"%", "weighted mark =",markOne, "x", weight_of_first_mark, "=" ,total_markOne, "%")
print("Mark2 =", markTwo,"Weight2 =", weight_of_second_mark,"%", "weighted mark =",markTwo, "x", weight_of_second_mark, "=" ,total_markTwo, "%")
print("Mark3 =", markThree,"Weight3 =", weight_of_third_mark,"%", "weighted mark =",markThree, "x", weight_of_third_mark, "=" ,total_markThree, "%")
 
totalmark = total_markOne + total_markTwo + total_markThree 
print("")
print("Overall mark is", total_markOne,"%", "+",total_markTwo, "%","+", total_markThree, "%","=", totalmark,"%")


