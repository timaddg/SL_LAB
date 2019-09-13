temp = input("Input the  temperature  to convert : ")
list1=[]
list2=[]

degree = int(temp[:-1])
choice = temp[-1]

if choice.upper() == "C":
  result = float(round((9 * degree) / 5 + 32))
  tup=(degree,result)
  list1.append(tup)
  print(list1)
  temp = "Fahrenheit"
elif choice.upper() == "F":
  result = float(round((degree - 32) * 5 / 9))
  tup=(degree,result)
  list2.append(tup)
  print(list2)
  temp = "Celsius"
elif choice.upper=="E":
	quit()
  #if user.input =="e":
  	#quit()
  	
  
print("The temperature in", temp, "is", result, "degrees.")

