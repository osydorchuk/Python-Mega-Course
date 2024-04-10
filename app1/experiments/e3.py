with open('../files/file_1.txt', 'r') as file:
    print(file.read())

with open('../files/file_1.txt') as file:
    print(file.read())

with open('../files/file_1.txt', 'r') as file:
    content = file.read()
print(content.capitalize())