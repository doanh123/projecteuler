def foo():
  a = 1
  for i in xrange(20,1,-1):
     if a%i==0:
        pass
     else:
        a*=i
  print a

foo()
