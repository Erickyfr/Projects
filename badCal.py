from functools import reduce
from operator import mul
import sys

Nums = []
#opera = int(input("How many operations do you intend to use: "))
op =input("What operation do you want to use('+','-','*','/'): ")
mount = input("How many number do you want to use: ")
mounts = int(mount)
for i in range(mounts):
    Num = float(input("Enter a number: "))
    Nums.append(Num)
if op == '/':
    Num = float(input("Enter the divisor: "))
    if Num == 0:
        print("Cannot divide by Zero")
        sys.exit()
        
        
if op == '+':
    add = sum(Nums)
    print("Number is: ", add)
elif op == '-':
    minus = Nums[0]
    for nu in Nums[1:]:
        minus -= nu
    print("Number is: ", minus)
elif op == '*':
    mu_t = reduce(mul, Nums)
    print("Number is: ", mu_t)
elif op == '/':
    s_um = sum(Nums)
    d_iv = s_um//Num
    print("Number is: ", d_iv)
else:
    print("Invalid Operation because ", op + " is not an Operator")