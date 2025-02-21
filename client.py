import requests
from colorama import Fore, init

init(autoreset=True)  # Initialize colorama

SERVER_URL = "http://localhost:5000"

def perform_calculation():
    print(Fore.CYAN + "\nArithmetic Calculator Client")
    print(Fore.YELLOW + "=============================")
    
    try:
        num1 = int(input(Fore.WHITE + "Enter first number: "))
        num2 = int(input(Fore.WHITE + "Enter second number: "))
        
        print(Fore.GREEN + "\nAvailable operations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (×)")
        print("4. Division (÷)")
        
        choice = input(Fore.WHITE + "\nSelect operation (1-4): ")
        
        operations = {
            '1': 'add',
            '2': 'subtract',
            '3': 'multiply',
            '4': 'divide'
        }
        
        if choice not in operations:
            print(Fore.RED + "Invalid operation selection!")
            return

        operation = operations[choice]
        
        payload = {
            "num1": num1,
            "num2": num2
        }
        
        response = requests.post(
            f"{SERVER_URL}/{operation}",
            json=payload
        )
        
        if response.status_code == 200:
            result = response.json().get('result')
            print(Fore.GREEN + f"\nResult: {result}")
        else:
            error = response.json().get('error', 'Unknown error')
            print(Fore.RED + f"\nError: {error}")
            
    except ValueError:
        print(Fore.RED + "Invalid input! Please enter valid numbers.")
    except requests.exceptions.ConnectionError:
        print(Fore.RED + "Could not connect to the server. Make sure it's running!")
    except Exception as e:
        print(Fore.RED + f"An error occurred: {str(e)}")

if __name__ == "__main__":
    while True:
        perform_calculation()
        continue_calc = input(Fore.WHITE + "\nPerform another calculation? (y/n): ").lower()
        if continue_calc != 'y':
            print(Fore.CYAN + "Goodbye!")
            break