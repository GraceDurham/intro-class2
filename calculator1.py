import math 

def add (num1, num2):
	add=num1+num2
	return add 

print add(10,10)

def multiply (num1, num2):
	results= num1 * num2 
	return results


results=multiply (10, 2)
print results 

def divide (num1, num2):
	divide_results=num1/num2
	return divide_results

print divide(100,10)

def modulo(num1, num2):
	modulo_results = num1 % num2 
	return modulo_results

print modulo(6,2)	

# power you use two stars 
def power(base, exponents):
	power_results = base ** exponents
	return power_results


print power(10,2)

# This calls the function power when you import math 
print math.pow (10,2)

# call power function within square function pass num and 2 for exponents
def square(num):
	results=power(num, 2)
	return results 

print square(8)


print (4+5) + (9-6)
print (12/2) - 60
print 1 + 2 + 3
print (1+2) * 2
print (3%4)/9 * 9
print 7 * (3+8)
print (1+2) - 3 * (4+5)
print 3(2+3) 



