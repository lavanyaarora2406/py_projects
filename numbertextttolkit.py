print("Welcome to the Number & Text Toolkit!")


while True:
    print("""
    Choose an option:
    1. Check if a number is prime
    2. Reverse a string
    3. Count vowels in a string
    4. Convert Celsius to Fahrenheit
    5. Quit
    """)

    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        try:
            num = int(input("Enter a number: "))

            if num < 2:
                is_prime = False
            else:
                is_prime = True
                for i in range(2, num):
                    if num % i == 0:
                        is_prime = False
                        break

            if is_prime:
                print(num, "is a prime number.")
            else:
                print(num, "is NOT a prime number.")

        except ValueError:
            print("That's not a valid number. Please try again.")
            

    elif choice == "2":
        text = input("Enter a string to reverse: ")
        reversed_text = text[::-1]
        print("Reversed:", reversed_text)

    elif choice == "3":
        text = input("Enter a string to count vowels in: ")
        text = text.lower()
        vowels = "aeiou"
        count = 0
        for letter in text:
            if letter in vowels:
                count += 1
        print("Number of vowels:", count)

    elif choice == "4":
        print("""
        a. Celsius to Fahrenheit
        b. Fahrenheit to Celsius
        """)
        sub_choice = input("Choose a or b: ")

        try:
            if sub_choice == "a":
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = (celsius * 9/5) + 32
                print(celsius, "C is", fahrenheit, "F")

            elif sub_choice == "b":
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = (fahrenheit - 32) * 5/9
                print(fahrenheit, "F is", celsius, "C")

            else:
                print("Invalid sub-choice.")

        except ValueError:
            print("That's not a valid temperature. Please try again.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
        
        