#print("hello world")
# Program - Find the sum of a 3 digit number entered by the user
"""import math
print(math.factorial(8))

import keyword
#print(keyword.kwlist)
#print(keyword.softkwlist)
import random
print(random.randint(0, 99))
import datetime
#print(datetime.datetime.now()) """

#number=int(input("enter a number: "))

#i=1
#while(i<=10):
  #  print(number,'*',i,"=",number*i)
  #  i+=1


import random
jackpot=random.randint(0, 100)
guess=int(input("enter the guessing number:  "))
attempt=1
while guess!=jackpot:
    if guess<jackpot:
        print("your guess is low than jackpot")


    else:
        print("your guess is higher than jackpot")
    guess=int(input("enter the guessing number: "))
    attempt+=1
else:
    print("hurrah you win!")
    print("your total attempt is: ",attempt)
