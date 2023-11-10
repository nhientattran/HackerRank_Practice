# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

# Example

# There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:

# 0.400000
# 0.400000
# 0.200000
# Function Description

# Complete the plusMinus function in the editor below.

# plusMinus has the following parameter(s):

# int arr[n]: an array of integers

def plusMinus(arr):
    length = len(arr)
    pos = 0
    neg = 0
    zer = 0
    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zer += 1
    print("{:.6f}".format(pos/length))
    print("{:.6f}".format(neg/length)) 
    print("{:.6f}".format(zer/length))

# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# Example
# arr = [1,3,5,7,9]

# The minimum sum is 1+3+5+7=16 and the maximum sum is 3+5+7+9 =24. The function prints 16 24

def miniMaxSum(arr):
    arr = sorted(arr)
    minSum = sum(arr[i] for i in range(0, len(arr)-1))
    maxSum = sum(arr[i] for i in range(1, len(arr)))
    print(f"{minSum} {maxSum}")

# Given a time in -hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

# Example

# s == '12:01:00PM'
# Return '12:01:00'.

# s == '12:01:00AM'
# Return '00:01:00'.

def timeConversion(s):
    for i in range(len(s)):
        if s[i] == 'P':
            sub = int(s[:2])
            if sub < 12:
                return str(sub+12) + s[2:i]
            else:
                return s[:i]
        elif s[i] == 'A':
            sub = int(s[:2])
            if sub == 12:
                return '0' + str(sub-12) + s[2:i]
            else:
                return s[:i]
