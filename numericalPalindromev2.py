# NumericalPalindrome simply tells us if a number is a palindrome. If it is it will return the palindrome otherwise
# it'll return 0 telling us whichever number we gave it wasn't symmetrical.
def isPalindrome(num):
    n = 0
    length = len(num) - 1
    for digit in num: #looking at each digit in the number we gave it to see if its opposite is identical
        if digit != num[length - n]:
            return 0    #if it isn't then return 0 and it'll stop checking
        else:
            n += 1
        if n == length: #if we get this far then all digits checked out and our n is equal to the length of the number
            return int(num)  #so return the number

# findPalindromes starts at x * y and works its way down until it finds a palindrome using the isPalindrome function
# then will check if x is divisible and if it is whether x * y are both between 999 and 100
def findPalindromes(bigNumber):
    x = 999
    while bigNumber >= (100 * 100):
        palindrome = isPalindrome(str(bigNumber)) # Calls the function above
        if palindrome > 0:
            while int(palindrome) % x != 0 and x > 100:
                x -= 1
            if int(palindrome) % x == 0 and x > 99:
                y = int(palindrome) // x
                if y < 999 and y > 100:
                    print(x, y, palindrome)
                    break
            x = 999
        bigNumber -= 1

palindrome = findPalindromes(999*999)

