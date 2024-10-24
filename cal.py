import math
import cmath
import sympy as sp

# Define symbolic variable for sympy
x = sp.symbols('x')

def basic_operations():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice(1/2/3/4): ")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid input")

def trigonometry():
    print("Select operation:")
    print("1. Sine (sin)")
    print("2. Cosine (cos)")
    print("3. Tangent (tan)")
    
    choice = input("Enter choice(1/2/3): ")
    
    angle = float(input("Enter angle in degrees: "))
    radians = math.radians(angle)
    
    if choice == '1':
        print(f"sin({angle}) = {math.sin(radians)}")
    elif choice == '2':
        print(f"cos({angle}) = {math.cos(radians)}")
    elif choice == '3':
        print(f"tan({angle}) = {math.tan(radians)}")
    else:
        print("Invalid input")

def logarithms():
    print("Select operation:")
    print("1. Natural log (ln)")
    print("2. Logarithm base 10 (log10)")
    
    choice = input("Enter choice(1/2): ")
    
    num = float(input("Enter number: "))
    
    if choice == '1':
        print(f"ln({num}) = {math.log(num)}")
    elif choice == '2':
        print(f"log10({num}) = {math.log10(num)}")
    else:
        print("Invalid input")

def power_and_roots():
    print("Select operation:")
    print("1. Power")
    print("2. Square root")
    
    choice = input("Enter choice(1/2): ")
    
    if choice == '1':
        base = float(input("Enter base: "))
        exponent = float(input("Enter exponent: "))
        print(f"{base} ^ {exponent} = {math.pow(base, exponent)}")
    elif choice == '2':
        num = float(input("Enter number: "))
        print(f"Square root of {num} = {math.sqrt(num)}")
    else:
        print("Invalid input")

def factorial():
    num = int(input("Enter a number to find the factorial: "))
    if num < 0:
        print("Factorial is not defined for negative numbers")
    else:
        print(f"Factorial of {num} is {math.factorial(num)}")

def solve_equation():
    equation = input("Enter an equation to solve (e.g., 'x**2 - 4 = 0'): ")
    solution = sp.solve(equation, x)
    print(f"The solution to the equation is: {solution}")

def derivative():
    expression = input("Enter an expression to differentiate (e.g., 'x**2 + 2*x + 1'): ")
    derivative_expr = sp.diff(expression, x)
    print(f"The derivative of the expression is: {derivative_expr}")

def integral():
    expression = input("Enter an expression to integrate (e.g., 'x**2 + 2*x + 1'): ")
    integral_expr = sp.integrate(expression, x)
    print(f"The integral of the expression is: {integral_expr}")

def complex_numbers():
    real = float(input("Enter the real part: "))
    imaginary = float(input("Enter the imaginary part: "))
    complex_num = complex(real, imaginary)
    
    print(f"Complex number: {complex_num}")
    print(f"Modulus: {abs(complex_num)}")
    print(f"Phase: {cmath.phase(complex_num)}")

def scientific_calculator():
    while True:
        print("\n*** Advanced Scientific Calculator ***")
        print("1. Basic Operations")
        print("2. Trigonometry")
        print("3. Logarithms")
        print("4. Power and Roots")
        print("5. Factorial")
        print("6. Solve Equation")
        print("7. Derivative")
        print("8. Integral")
        print("9. Complex Numbers")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            basic_operations()
        elif choice == '2':
            trigonometry()
        elif choice == '3':
            logarithms()
        elif choice == '4':
            power_and_roots()
        elif choice == '5':
            factorial()
        elif choice == '6':
            solve_equation()
        elif choice == '7':
            derivative()
        elif choice == '8':
            integral()
        elif choice == '9':
            complex_numbers()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

# Run the calculator
scientific_calculator()
