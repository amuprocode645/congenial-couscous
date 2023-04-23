## fizz = mulitple of 3
## buzz = mulitple of 5
## fizzbuzz = both
TURN = 1
while TURN <= 100:
    PRINTER = 0
    if (TURN/3).is_integer():
        PRINTER = 1
        if (TURN/5).is_integer():
            PRINTER = 0
            print("FizzBuzz")
        if PRINTER == 1:
            print("Fizz")
    else:
        if (TURN/5).is_integer():
            print("Buzz")
        else:
            print(TURN)
    TURN = TURN+1