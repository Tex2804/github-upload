import flask
import cmath
from math import sqrt
import math
import collections


def main1(a,b,c):
  d = (b**2) - (4*a*c)

  sol1 = (-b-cmath.sqrt(d))/(2*a)
  sol2 = (-b+cmath.sqrt(d))/(2*a)

  e=((-b)/(2*a))


  n =abs(d) 
  primeFactors(n)
  k=primeFactors(n)
  l= ([item for item, count in collections.Counter(k).items() if count > 1])

  #Driver code
  g=(multiplyList(k))
  h=(multiplyList(l))
  j=g/h**2
  v=e+h**2
  m=e-h**2
  return 'The solution are {4} and {5} the solutions unsimplified are {0} √{1}/{2} unsimplfied and {3} √{1}/{2} unsimplified'.format(v,j,2*a,m,sol1,sol2)

  




#https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/

    # Python program to print prime factors


# A function to print all prime factors of
# a given number n
def primeFactors(n):
	prime=[]
	# Print the number of two's that divide n
	while n % 2 == 0:
		prime.append (2)
		n = n / 2
		
	# n must be odd at this point
	# so a skip of 2 ( i = i + 2) can be used
	for i in range(3,int(math.sqrt(n))+1,2):
		
		# while i divides n , print i and divide n
		while n % i== 0:
			prime.append (int(i))
			n = n / i
			
	# Condition if n is a prime
	# number greater than 2
	if n > 2:
		prime.append (int(n))
	return prime	
# Driver Program to test above function



#https://stackoverflow.com/questions/9835762/how-do-i-find-the-duplicates-in-a-list-and-create-another-list-with-them

 

# Python program to multiply all values in the
# list using traversal

def multiplyList(myList) :
	
	# Multiply elements one by one
	result = 1
	for x in myList:
		result = result * x
	return result
	
if __name__ == "__main__":
  a = int(input("a is:"))
  b = int(input("b is:"))
  c = int(input("c is:"))
  main(a,b,c)