#What is the largest prime factor of the number 600851475143 ?
from prime import primes
def foo():
   b =int(600851475143**.5 +1)
   prime_list = primes(b)

   for i in reversed(prime_list):
      if 600851475143%i==0:
         print i
         break

foo()
#ans: 6857  
