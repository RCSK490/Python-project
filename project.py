import random
a=random.randint(1,101)
k=-1
while(k!=a):
  k=int(input("guess the number between 1to 100 ,both includive)"))
  if(k<a):
       print("the guessed number is low")
  elif(k>a):
       print("the guessed number is high")
print("guessed number is correct")
  