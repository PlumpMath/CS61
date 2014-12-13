"""
Code Writer : EOF
Code file   : exercise_5.py
Code date   : 2014.12.13

Exercise 5: factors()

"""

def factors(number):

     denoninator = number
     while(denoninator > 1):
          denoninator = denoninator -1
          if(number % denoninator == 0):
             print denoninator
             
factors(20)
