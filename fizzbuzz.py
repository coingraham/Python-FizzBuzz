number = int(input("please enter a number: "))

FizzBuzz = False

while not FizzBuzz:
    number = int(input("please enter a number: "))
    num = number
    if num % 3 == 0 and num % 5 == 0:
        FizzBuzz = True
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
   
        


    
   