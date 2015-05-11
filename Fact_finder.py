

def find_fact(n):
  l = [] # list to hold the factors of 'n'

  if is_even(n):
  	start = 2
  	step = 1
  else:
  	start= 1
  	step = 2

  for i in range (start, n/2+1, step):
    if (n%i==0):
      l.append(i)


  return l



def is_even(n):
  return n%2==0