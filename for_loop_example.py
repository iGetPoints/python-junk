ans = 0
out1 = 0
out2 = 0

print('choose a number to start adding')
num1 = input()
out1 == num1
print('choose a number to stop adding')
num2 = input()
out2 == num2
num2 == int(num2) + 1

for i in range(int(num1), int(num2)):
    ans = i + ans
print('adding up ' + str(out1) + ' to ' + str(out2) + ' gives you an answer of ' + str(ans))
