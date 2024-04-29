from calculate_func import do_addition , do_substraction
from multiply import do_multiplication
def main():
    print("Welcome to the calculator app")
    print("""Select the function from the given options:
1. ADD
2. Substract
3. Multiply
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
    else:
        print("Invalid Choice")

    print(f"Result : {result}")

main()