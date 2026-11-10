import math
import random
print('=== CRAZY CALCULATOR ===')
print('Not normal calculator, this is CRAZY!')
name = input('Enter your name: ')
print('Hello ' + name + '! Lets calculate crazy things')
while True:
    print(' ')
    print('=== MENU ===')
    print('1. Power Calculator')
    print('2. Square and Cube')
    print('3. Age in Days Calculator')
    print('4. BMI Calculator')
    print('5. Love Calculator')
    print('6. Salary Calculator')
    print('7. EMI Calculator')
    print('8. Lucky Number')
    print('9. Pizza Calculator')
    print('10. Exit')
    choice = input('Choose 1 to 10: ')
    if choice == '1':
        a = float(input('Enter base number: '))
        b = float(input('Enter power: '))
        result = a ** b
        print(str(a) + ' power ' + str(b) + ' = ' + str(result))
    elif choice == '2':
        a = float(input('Enter number: '))
        print('Square = ' + str(a * a))
        print('Cube = ' + str(a * a * a))
        print('Square Root = ' + str(math.sqrt(a)))
    elif choice == '3':
        age = int(input('Enter your age in years: '))
        print('You are ' + str(age * 365) + ' days old!')
        print('You are ' + str(age * 12) + ' months old!')
        print('You are ' + str(age * 365 * 24) + ' hours old!')
        print('You are ' + str(age * 365 * 24 * 60) + ' minutes old!')
    elif choice == '4':
        weight = float(input('Enter weight in kg: '))
        height = float(input('Enter height in feet: '))
        height_m = height * 0.3048
        bmi = weight / (height_m * height_m)
        print('Your BMI = ' + str(round(bmi, 2)))
        if bmi < 18.5:
            print('You are Thin! Eat more!')
        elif bmi < 25:
            print('Perfect! You are Fit!')
        elif bmi < 30:
            print('Little Overweight!')
        else:
            print('Gym Time Bro!')
    elif choice == '5':
        your_name = input('Enter your name: ')
        crush = input('Enter crush name: ')
        love = random.randint(50, 100)
        print(your_name + ' + ' + crush + ' = ' + str(love) + '% Love!')
        if love > 90:
            print('Made For Each Other! Shaadi Pakki!')
        elif love > 75:
            print('Strong Love!')
        else:
            print('Try Harder Bro!')
    elif choice == '6':
        salary = float(input('Enter monthly salary: '))
        print('Yearly Salary = Rs ' + str(salary * 12))
        print('Daily Salary = Rs ' + str(round(salary / 30, 2)))
        print('Hourly Salary = Rs ' + str(round(salary / 30 / 8, 2)))
        print('After 10 years you will earn Rs ' + str(salary * 12 * 10))
    elif choice == '7':
        loan = float(input('Enter loan amount: '))
        months = int(input('Enter months: '))
        interest = loan * 0.1
        total = loan + interest
        emi = total / months
        print('Total to pay = Rs ' + str(total))
        print('Monthly EMI = Rs ' + str(round(emi, 2)))
    elif choice == '8':
        lucky = random.randint(1, 100)
        print(name + ' your lucky number today is ' + str(lucky))
        if lucky > 80:
            print('Today is your lucky day!')
        else:
            print('Normal day!')
    elif choice == '9':
        people = int(input('How many people: '))
        slices = people * 3
        pizzas = slices / 8
        print('You need ' + str(round(pizzas, 1)) + ' pizzas')
        print('Total slices needed: ' + str(slices))
        print('Cost will be Rs ' + str(round(pizzas * 300, 2)))
    elif choice == '10':
        print('Bye ' + name + '! Crazy Calculator Closed!')
        break
    else:
        print('Wrong choice! Try again')
