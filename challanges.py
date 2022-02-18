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


wk4_16 = int(input("Enter a number: "))
num2 = int(input("Now enter a much HIGHER number: "))
for i in range(wk4_16, num2):







