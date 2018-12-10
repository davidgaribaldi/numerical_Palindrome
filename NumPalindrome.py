# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 11:24:24 2018

@author: davidg
"""

def NumericalPalindrome(num):
    n = 0
    length = len(num) - 1
    for digit in num:
        if digit != num[length - n]:
            print('This is not a numerical palindrome')
            break
        else:
            n += 1
        if n == length:
            print('the number,', num, ', is a numerical palindrome')
            
            
input_Number = input("If you give me a number, I'll tell if you it's a palindrome: ")
NumericalPalindrome(input_Number)
