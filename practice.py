i=1
while i <= 5:
  mark=int (input(f"Enter marks {i}:"))
  if mark > 75:
      print("A")
  elif 65 < mark < 75 :
      print("B")  
  elif 55 < mark < 64 :
      print("C")
  elif 55 < mark < 64 :
      print("S")      
  else:
      print("fail")    
i=i+1      