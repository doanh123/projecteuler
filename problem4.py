#Find the largest palindrome made from the product of two 3-digit numbers.

def foo():
    c = []
    for i in xrange(999,500,-1):
        for j in xrange(999,500,-1):
           b=i*j
           if palindrome(b):
              c.append(b)
    print max(c)

def palindrome(num):
   a= list(str(num))
   b=a[:]
   b.reverse()
   return a==b

foo()
# ans 906609

 
