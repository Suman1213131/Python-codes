enter_text = input("enter some text> ") 
print("") 
print("Analysis of text") 
print("----------------") 
print("") 
  
vowels = 0 
enter_text.lower() 
for v in enter_text: 
    if(v == 'a' or v == 'e' or v == 'o' or v == 'i' or v == 'u'): 
        vowels = vowels + 1 
     
digits = 0 
enter_text.lower() 
for d in enter_text: 
    if(d == '9'or d == '8' or d == '7' or d == '6' or d == '5' or d == '4' or d == '3' or d == '2' or d == '1' or d == '0'): 
        digits = digits + 1 
     
consonants = 0 
enter_text.lower() 
for c in enter_text: 
    if(c == 'b' or c == 'c' or c == 'd' or c == 'f' or c == 'g' or c == 'h' or c == 'j' or c == 'k' or c == 'l' or c == 'm' or c == 'n' or c == 'p' or c == 'q' or c == 'r' or c == 's' or c == 't' or c == 'v' or c == 'x'or c == 'z' or c == 'w' or c == 'y'): 
        consonants = consonants + 1 
  
whitespace = 0 
enter_text.lower() 
for w in enter_text: 
    if(w == ' ' or w == ' '): 
        whitespace = whitespace + 1 
         
punctuation = 0 
enter_text.lower() 
for p in enter_text: 
    if(p == '.' or p == ',' or p == '?' or p == ';' or p == '!' or p == ':' or p == "'" or p == '()' or p == '@' or p == '/'): 
        punctuation = punctuation + 1 
  
print("total number of vowels in the text are>" , vowels) 
print("total number of digits in the text are>" , digits) 
print("total number of consonants in the text are>" , consonants) 
print("total number of whitespace  in the text are>" , whitespace) 
print("total number of punctuation  in the text are>" , punctuation) 
