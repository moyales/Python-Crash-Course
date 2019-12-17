#try:
#    print(5/0)
#except ZeroDivisionError:
#    print("You dumbass, you cannot divide by zero.")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        ans = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("Can't divide by zero, dumbass.")
    else:
        print(ans)