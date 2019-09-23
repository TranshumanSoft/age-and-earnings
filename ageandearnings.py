print("Hi. You only and tribute in Spain if you're age is higher than 16.")
while True:
    age = int(input("How old are you?"))
    if age >= 16:
        print("Sorry, probably you must pay taxes.")
        break
    else:
        print("Congrats! You mustn't pay taxes!")
earnings = float(input("How much money do you earn per month?"))
if earnings >= 1000:
    print("Sorry, you must pay taxes.")
else:
    print("Well, you mustn't pay taxes, but you don't earn so much money :/")
