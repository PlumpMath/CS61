"""
Code Writer : EOF
Code file   : exercise_4.py
Code date   : 2014.12.13

Exercise 4: expt()

Attention here. 
      Every new line can not start by a blank.
"""

def my_expt(base,power):

    ret = 1
    while(power > 0):
	ret = base*ret
        power = power -1

    return ret

print(my_expt(2,3))
