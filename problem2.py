#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
from fibonaccigenerator import fib

def foo():
   sum = 0
   a = fib()
   while True:
     b=a.next()
     if b>4000000:
        break
     if b%2==0:
        sum +=b

   print sum

foo()
#ans: 4613732   
