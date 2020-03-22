class Calculator :
# This function adds two numbers
	def add(self, x, y):
   		return x + y

# This function subtracts two numbers
	def subtract(self, x, y):
   		return x - y

# This function multiplies two numbers
	def multiply(self, x, y):
   		return x * y

# This function divides two numbers
	def divide(self, x, y):
   		return x / y

# This function squares one number 
	def square_number (self, x): 
    		return x ** 2

# This function derives the square root of a number 
	def square_root(self, x):
    		return x**0.5

if __name__ == "__main__":
	print("Select operation.")
	print("1.Add")
	print("2.Subtract")
	print("3.Multiply")
	print("4.Divide")
	print('5.Square_number')
	print('6.Square_root')

# Take input from the user
	choice = input("Enter choice(1/2/3/4/5/6): ")



	if choice == '1':
    		num1 = float(input("Enter first number: "))
    		num2 = float(input("Enter second number: "))

    		print(num1,"+",num2,"=", add(num1,num2))

	elif choice == '2':
    		num1 = float(input("Enter first number: "))
    		num2 = float(input("Enter second number: "))

    		print(num1,"-",num2,"=", subtract(num1,num2))

	elif choice == '3':
    		num1 = float(input("Enter first number: "))
    		num2 = float(input("Enter second number: "))

    		print(num1,"*",num2,"=", multiply(num1,num2))

	elif choice == '4':
    		num1 = float(input("Enter first number: "))
    		num2 = float(input("Enter second number: "))

    		print(num1,"/",num2,"=", divide(num1,num2))

	elif choice == '5': 
    		num = float(input("Enter number: "))

    		print(num,'**2','=', square_number(num))
    
	elif choice == '6':
    		num = float(input('Enter number: '))
    
    		print(num,'**0.5', '=', square_root(num))
   
	else:
    		print("Invalid input")
