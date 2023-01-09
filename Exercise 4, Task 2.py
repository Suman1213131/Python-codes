print ("Star Wars name generator") 
print (" ") 
  
first_name = input ("enter your first name> ") 
last_name = input ("enter your last name> ") 
mother_maiden_name = input ("enter your Mother's maiden name> ") 
city_born = input ("enter the city you were born in> ") 
  
f_name = (first_name[0:3]+last_name[0:2]) 
l_name = (mother_maiden_name[0:2]+city_born[0:3]) 
print(" ") 
  
print ("Your Stars Wars name is >" , f_name , l_name) 
 
