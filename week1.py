def delchar(str,c):
  if len(c)==1:
  	str=str.replace(c,"")
  return str
def shuffle(l1,l2):
  l1.extend(l2)
  l1.sort()
  return l1
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def primeproduct(num):
    if num < 4:  
        return False

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            if is_prime(i) and is_prime(num // i):
                return True
    return False
# code containing 3 functions 1 to delete all the charectes if matched other check prime and 3 to shuffle 2 list
