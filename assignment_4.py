def prime(n):
      count=0
      for i in range(2,int(n**0.5)):
            if(i*i)==n:
                  count=1
      if(count==1):
            return False
      return True
def evenOdd(n):
      if(n and 1==0):
            return True
      return False
def divisibleByFive(n):
      if(n%5==0):
            return True
      return False
n = int(input())
if(prime(n)):
      print("Number is Prime")
      print("Number is ODD")
      if(divisibleByFive(n)):
            print("Number is divisible by 5")
      else:
            print("Number is not divisible by 5")
else:
      print("Number is Not Prime")
      if(divisibleByFive(n)):
            print("Number is divisible by 5")
      else:
            print("Number is not divisible by 5")
      if(evenOdd(n)):
            print("Number is even")
      else:
            print("Number is ODD")
