#练习
car = input("hello, what kind of car do you want? ")
print("let me see if i can find you a "+car)

people = input("how many people will come here for dinner? ")
people = int(people)
if people > 8:
    print("sorry, there is no table left!")
else:
    print("we have extra tables for you!")

numbers = input("enter a number and i will tell you whether it can be divided by 10: ")
numbers = int(numbers)
if numbers % 10 == 0:
    print("it can be divided by 10")
else:
    print("it can't be divided by 10")

#练习
prompt = ("please write down the ingredient you want to add into the pizza: ")
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print('we will add this for you!')

prompt = ("how old are you: ")
while True:
    message = input(prompt)
    if message == 'quit':
        break
    elif int(message) < 3:
        print("your price ticket is 0")
    elif int(message) >= 3 and int(message) < 12:
        print("your price ticket is 10")
    else:
        print("your price ticket is 15")

responses = {}
polling_active = True
while polling_active:
    name = input("\nwhat is your name? ")
    response = input("which mountain would you like to climb? ")
    responses[name] = response
    repeat = input("would you let another person to answer this question? ")
    if repeat == 'no':
        polling_active = False
print("---polling results---")
for name,response in responses.items():
    print(name + " would like to climb "+ response)
