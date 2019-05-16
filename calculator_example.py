# First attempt at making a calculator
print('What kind of operation would you like to do? (+ - * /) ?')
Opp = input()
print('Enter the first number')
Num1 = input()
print('Enter the second number')
Num2 = input()

if Opp == '+':
    Answer = int(Num1) + int(Num2)
elif Opp == '-':
    Answer = int(Num1) - int(Num2)
elif Opp == '*':
    Answer = int(Num1) * int(Num2)
elif Opp == '/':
    Answer = int(Num1) / int(Num2)
else:
    print('You entered an incorrect opperation')
    
print('The answer is ' + str(Answer))
