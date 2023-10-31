'''this module contains my two functions and their test cases'''

def sum_list(a, b=3.141):
  ''''this function will add a and b and also return a sorted list containing their values'''
  list = []
  list.append(a)
  list.append(b)
  list.sort()
  print(list)
  return a + b


def sum_listnew(a, b=3.141,verbose=False):
  ''''this does the same thing but only if verbose is true'''
  if verbose == True:
    list = []
    list.append(a)
    list.append(b)
    list.sort()
    print(list)
    return a + b
  else: print("sorry verbose is false")

if __name__ == '__main__':
  x = sum_list(5, 7)
  print(f"sum = {x}")
  x = sum_list(26)
  print(f"sum = {x}")
  x = sum_list(a=3.141, b=9)
  print(f"sum = {x}")
  x = sum_list(a=9, b=0)
  print(f"sum = {x}")


  x = sum_listnew(5, 7)
  print(f"sum = {x}")
  x = sum_listnew(26, verbose=True)
  print(f"sum = {x}")
  x = sum_listnew(a=3.141, b=9, verbose=True)
  print(f"sum = {x}")
  x = sum_listnew(a=9, b=0, verbose=False)
  print(f"sum = {x}")
