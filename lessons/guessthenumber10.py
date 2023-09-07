my_number_string: str = input("Guess a number: ")
my_number: int = int(my_number_string)
correct_number: int = 10

if my_number != correct_number:
    print("Wrong")
else: 
    print("Right")