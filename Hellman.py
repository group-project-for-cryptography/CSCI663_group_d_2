import random
def fast_raise_power_books(x, n, p):
  nb = bin(n)[2:]
  result = 1
  for i in range(len(nb)):
   result = result * result % p
   if nb[i] ==  '1':
    result = (result * x) % p
  return result

def isPrime(n):
  for i in range(100):
    a = random.randrange(1,n)
    if fast_raise_power_books(a,n-1,n) != 1:
      return False
    return True
    
def generatePrime(n):
  lower = 10**n
  higher = 10**(n+1)
  while True:
    p = random.randrange(lower,higher)
    if (isPrime(p)):
      return p
def generateBase(n):
  return int(random.randrange(2,n-2))

n=15
p = generatePrime(n)
g = generateBase(p)
Alice_key = int(input("Please input Alice Private key: "))
Bob_key = int(input("Pleae input Bob Private key: "))
Alice = fast_raise_power_books(g,Alice_key,p)
Bob = fast_raise_power_books(g,Bob_key,p)
SharedKey_Alice = fast_raise_power_books(Bob,Alice_key,p)
SharedKey_Bob = fast_raise_power_books(Alice,Bob_key,p)
print(SharedKey_Alice) 
print(SharedKey_Bob)

