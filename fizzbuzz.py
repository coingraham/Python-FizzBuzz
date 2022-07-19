

for number in range(101):

    fizzbuzz = ""

    if number % 3 == 0:
        fizzbuzz += "Fizz"
    if number % 5 == 0:
        fizzbuzz += "Buzz"

    print(fizzbuzz or number)
