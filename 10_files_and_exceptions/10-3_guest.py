message = "Welcome to the party! What's your name?"
message += "\nInput your name here: "

while True:
    name = input(message)
    if name == 'quit':
        break
    else:
        filename = 'guest_list.txt'
        with open(filename, 'a') as file_object:
            file_object.write(name + '\n')