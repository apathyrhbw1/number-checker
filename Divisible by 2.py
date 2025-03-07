import time
print("Hello user, may I know your name?")

name = input("Enter your name: ")
time.sleep(1)
print("Hello," + name, "how are you?")
time.sleep(1)

while True:
	check_number = (int(input("insert any number: ")))
	check_number = abs(check_number)
	
	if check_number % 2 == 0:
		print("number", + check_number, "is an even number.")
		
	else:
		print("number", + check_number, "is an odd number.")