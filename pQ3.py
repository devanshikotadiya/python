# user_input = input("Please enter something: ")
    
#     # Try to convert the input to an integer
# int_input = int(user_input)
# print("You entered: {int_input} (Datatype: int)")

#     # Try to convert the input to a float
# float_input = float(user_input)
# print("You entered: {float_input} (Datatype: float)")
        
#        # If the input is not a number, check if it's a boolean
# if user_input.lower() == "true":
#     print("You entered: True (Datatype: bool)")
# elif user_input.lower() == "false":
#     print("You entered: False (Datatype: bool)")
# else:
#         # If the input is not a number or a boolean, it's a string
#     print("You entered: '{user_input}' (Datatype: str)")

# string=34
# print(type(string))
# string="bhavy"
# print(type(string))
# string=boolen
# print(type(string))
# string=""
# print(type(string))
# string=34.0
# print(type(string))

# def print_input_with_datatype():
#     user_input = input("Please enter something: ")

#     if user_input.isdigit():
#         print(f"You entered: {user_input} (Datatype: int)")
#     elif user_input.replace('.', '', 1).isdigit():
#         print(f"You entered: {user_input} (Datatype: float)")
#     elif user_input.lower() == "true" or user_input.lower() == "false":
#         print(f"You entered: {user_input} (Datatype: bool)")
#     else:
#         print(f"You entered: '{user_input}' (Datatype: str)")

# if __name__ == "__main__":
#     print_input_with_datatype()

# user_input = input("Please enter something: ")

# if user_input.isdigit():
#     print(f"You entered: {user_input} (Datatype: int)")
# elif user_input.replace('.', '', 1).isdigit():
#     print(f"You entered: {user_input} (Datatype: float)")
# elif user_input.lower() == "true" or user_input.lower() == "false":
#     print(f"You entered: {user_input} (Datatype: bool)")
# else:
#     print(f"You entered: '{user_input}' (Datatype: str)")


user = input("Please enter: ")

if user.isdigit():
    print("You entered: " + user + " (Datatype: int)")
elif user.replace('.', '', 1).isdigit():
    print("You entered: " + user+ " (Datatype: float)")
elif user.lower() == "true" or user.lower() == "false":
    print("You entered: " + user + " (Datatype: bool)")
else:
    print("You entered: '" + user + "' (Datatype: str)")



