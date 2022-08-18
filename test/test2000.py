"""
  *
 ***
*****
 ***
  *
"""
number = int(input())
for i in range(number):
    print(" "*(number-1-i),end="")
    print("*"*((2*i)+1))

for j in range(number-2,-1,-1):
    print(" " * (number - 1 - j), end="")
    print("*" * ((2 * j) + 1))
