filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

lines = lines.replace('Python','Java')

for line in lines:
    print(line.strip())