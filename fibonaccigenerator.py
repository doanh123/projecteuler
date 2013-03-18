def fib():
#generates fibonacci sequence
  a,b = 1,0
  while True:
    yield a
    b = a +b
    yield b
    a = a +b
