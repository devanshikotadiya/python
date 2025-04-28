##continue statement
print("1. continue statement:")
number = 0
for number in range(10):
    if number == 5:
        continue  

    print(number)

print('Loop is a exist. :(')

###break statement
print("2. break statement:")
number = 0
for number in range(10):
    if number == 5:
        break   

    print('Number is ' + str(number))
print('Loop is a exist. :(')

## pass statement
print("3. pass statement:")
for i in range(5):
  if i == 3:
    pass  # Placeholder for future code
  print(i)