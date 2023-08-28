name = input("whet is your name? ")
age = input("how old are you? ")

print(f"My name is {name} and I am {age} years old") 



first_number=int(input('first_number'))
secound_number=int(input('secound_number'))
operation=input('whet do you whant do do (/*-+)')

if operation =='+':
    print (first_number + secound_number)

elif operation =="-":
    print(first_number- secound_number)

elif operation == "*":
    print(first_number*secound_number)
elif operation =="/":
    print(first_number/secound_number)
else :
    print("rong")




bus_capacity = 30
people_inbus = int(input("how many people are in the bus ?"))
want_to_ride = int(input("how many want to take the bus ?"))
empty_seat = bus_capacity - people_inbus

if empty_seat>=want_to_ride :
    print("you can gat in")

else :
    print("you can not enter the bus")