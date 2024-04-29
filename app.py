from calculate_func import do_addition , do_substraction, do_division
from multiply import do_multiplication
from area import calculate_area_rectangle
def main():
    print("Welcome to the calculator app")
    print("""Select the function from the given options:
1. ADD
2. Substract
3. Multiply
4. Division
        """)
    
    user_input = input("Select the function;")
    a = int(input("Enter num1:"))
    b = int(input("Enter num2:"))

    if user_input == '1':
        result = do_addition(a , b)
    elif user_input == '2':
        result = do_substraction(a , b)
    elif user_input == '3':
        result = do_multiplication(a , b)
    elif user_input == '4':
        result = do_division(a , b)
    else:
        print("Invalid Choice")

    print(f"Result : {result}")

main()