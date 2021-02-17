import random
def passw(numDigits):
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(numDigits):
        secretNum += str(numbers[i])
    return int(secretNum)

number_len = 4
passw = tuple(i for i in str(passw(number_len)))

on = 0
while (on != number_len):
    on = 0
    present = 0
    guess = str(input("Guess the 4-digit code: "))
    guess = list(i for i in guess)

    while len(guess) != len(set(guess)):
        print("No digits can repeat!")
        guess = str(input("Guess the 4-digit code: "))
        guess = list(i for i in guess)

    for x, X in zip(guess, passw):
        if x == X:
            on += 1

    for position, number in enumerate(guess):
        if number in passw and number != passw[position]:
            present += 1

    if on == number_len:
	    print("You guessed correctly!")
    else:
	    print("Number of digits in the right place:", on)
	    print("Number of digits guessed correctly but in the wrong place:", present)