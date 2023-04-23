# fizz = mulitple of 3
# buzz = mulitple of 5
# fizzbuzz = both
turn = 1

while turn <= 100:
    printer = 0
    if (turn/3).is_integer():
        printer = 1
        if (turn/5).is_integer():
            printer = 0
            print("FizzBuzz")
        if printer == 1:
            print("Fizz")
    else:
        if (turn/5).is_integer():
            print("Buzz")
        else:
            print(turn)
    turn = turn+1
