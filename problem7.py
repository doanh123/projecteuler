#return the 10001 prime number

from primegen import gen_primes

primes = gen_primes()

for i in xrange(10001):
    print primes.next()


#ans: 104743
