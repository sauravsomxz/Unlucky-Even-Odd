# Author : Saurav Ranjan Maharana
# Date : 18th November, 2019
# Purpose : Learning Py!
# Title : Loop through numbers 1-20
# If number is or number is 13: print("X is unlucky")
# if number is even: print("X is even")
# If number is odd: print("X is odd")

for n in range(1,21): # "n" is number
    if n==4 or n==13:
        state = "Unlucky"
    elif n%2==0:
        state = "Even"
    elif n%2!=0:
        state = "Odd"
    print(f"{n} is {state}")
else:
    print("Good By!")