import stack


for i in range(4):
    user_input = input('Enter a word: ')
    stack.push(user_input)

current_doc = " ".join(stack.stack)

print(f"The current document is: {current_doc}")

user_input = input('Would you like to undo?: ')
if user_input.upper() == 'Y':
    stack.stack.pop()
    current_doc = " ".join(stack.stack)

print(f"The current document is: {current_doc}")
