# 10.6: Create a user friendly exception for an addition function when the user
# does not provide a number.

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    n1 = input("\nFirst Num: ")
    if n1 == 'q':
        break
    n2 = input("Second Num: ")
    if n2 == 'q':
        break
    try:
        ans = int(n1) + int(n2)
    except ValueError:
        print("Fucker, that's not a number")
    else:
        print(ans)
    