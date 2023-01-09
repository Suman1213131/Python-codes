print ("Palindrome checker program")
print("")
enter_word = input("Please enter a word> ").lower()
if(enter_word==enter_word[::-1]):  
      print ("Word", enter_word, "is a palindrome")  
else:  
      print("Word", enter_word, "is not a palindrome")  
