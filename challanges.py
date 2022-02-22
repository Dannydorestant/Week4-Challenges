import string

wk4_1 = 12 + 12
print(wk4_1)


wk4_2 = "12" + "12"
print(wk4_2)


wk4_3 = input("What is your Thot Number?")
print(str(wk4_3))
print(type(wk4_3))


wk4_4 = input("What's your name?")
print("Your name used to be " + wk4_4 + ". But now it's Thot" + wk4_3)


wk4_5 = input("What name did your parents give you?").upper()
print(wk4_5)


wk4_6 = input("What's your name?")
chars = len(wk4_6)
print("There are", chars, "characters in your name.")


wk4_7 = input("What's your name?")
print(wk4_7[-2:])


wk4_8 = input("What's your name?")
rev = wk4_8[::-1]
print(rev)


wk4_9 = float(input(" Please Enter a number : "))
cube = wk4_9 ** 3
print(f'{cube:g}')


wk4_10 = float(input(" Please Enter a number : "))

for num in range(13):
    value = num * wk4_10
    print(f'{wk4_10:g} X {num} = {value:g}')


wk4_11 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
result = wk4_11 * num2
print(f'{result:g}')


wk4_12 = float(input("Enter your First number: "))
num2 = float(input("Enter your Second number: "))
num3 = float(input("Enter your Third number: "))


def results():
    total = wk4_12 * num2 + num3
    print(f'{wk4_12:g} x {num2:g} + {num3:g} = {total:g}')


results()


wk4_13 = 0
adding: bool = True
while adding:
    plus = float(input(f"Your current total is {wk4_13:g}, How much do you want to add to it? "))
    wk4_13 = wk4_13 + plus
    more = input("Do you want to add more? Yes or No? ").upper()
    if more == "NO":
        adding: bool = False
        print(f'Your Grand Total is {wk4_13:g} \n')
    else:
        print(f'Your Grand Total is {wk4_13:g} \n')


wk4_14 = ['red', 'green', 'blue', 'orange', 'white', 'black', 'gold', 'purple', 'yellow', 'magenta']
for color in wk4_14:
    print(color)


wk4_15 = float(input(" What do you think your grade is in this class? Scale of 1 to 100: "))
is_passing: bool = True
if wk4_15 < 70:
    is_passing: bool = False

if is_passing:
    print("Passing")
else:
    print("Failing")


wk4_16 = int(input("Enter your Starting number: "))
num2 = int(input("Enter your Ending number: "))
num2 = num2 + 1   # Include the last number in the range in the sum, not sure if necessary
result = 0
for i in range(wk4_16, num2):
    result += i
print(f'All the numbers in your Range add up to {result}')

wk4_17 = range(100, -1, -1)
for i in wk4_17:
    print(i)


wk4_18 = input("Enter a letter: ").lower()
letter = list(string.ascii_lowercase)

print(letter.index(wk4_18))

wk4_19 = input("Please type in the following letters: ABCD: ").upper()
a = wk4_19[0]
b = wk4_19[1]
c = wk4_19[2]
d = wk4_19[3]

print(f'{a}/{b}*{c})-{d}')

wk4_20 = int(input("Enter a number: "))
if wk4_20 % 2 == 0:
    print(f'{wk4_20} is an Even Number')
else:
    print(f'{wk4_20} is an Odd Number')
print("\n")

wk4_21 = int(input("Enter a number: "))
print("This is too hard, or i'm dumb")
print("\n")

wk4_22 = int(input("Set a Max Number: "))
for i in range(0, wk4_22 + 1):
    if i % 2 != 0:
        print(i)
print("\n")
wk4_23 = list(string.ascii_lowercase)
for i in wk4_23:
    letters = wk4_23.index(i) + 1
    if letters % 3 == 0:
        print(i)
print("\n")
wk4_24 = "I have no idea what you mean by this???"
a = 2
b = 3
c = 20
d = 3
print(f'{a}{b}')
print(c + d)
print("\n")
wk4_25 = list(string.ascii_lowercase)
shift = int(input("You are at letter A. How many letters would you like to shift to the right? "))
looper: bool = True
current_letter = 0
while looper:
    for i in wk4_25:
        letters = wk4_25.index(i)
        if letters == current_letter + shift:
            letter = letters
            print(f'You are now at letter {wk4_25[letter]}')
    looper: bool = False
















