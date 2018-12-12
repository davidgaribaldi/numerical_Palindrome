x = 999
y = 999
z = x * y
palindrome_List = []

def NumericalPalindrome(num):
    n = 0
    length = len(num) - 1
    for digit in num:
        if digit != num[length - n]:
            return 0
        else:
            n += 1
        if n == length:
            palindrome_List.append(num)
            return 1

palindrome = NumericalPalindrome(str(z))
while z >= (100 * 100):
    palindrome = NumericalPalindrome(str(z))
    z -= 1

for palindrome in palindrome_List:
    print(palindrome)
    while int(palindrome) % x != 0 and x > 100:
        x -= 1
    if int(palindrome) % x == 0 and x > 99:
        y = int(palindrome) // x
        if y < 999 and y > 100:
            print(x, y, palindrome)
            break
    x = 999

