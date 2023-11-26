# You will be given a list of 32 bit unsigned integers. Flip all the bits (1->0 and 0->1 ) and return the result as an unsigned integer.

# Example
# n = 9 10
# 9 10 = 1001 2
# . We're working with 32 bits, so:
# 000000000000000000000000000001001 2 = 9 10
# 111111111111111111111111111110110 2 = 4294967286 10


# Return 4294967286.

# Function Description

# Complete the flippingBits function in the editor below.

# flippingBits has the following parameter(s):

# int n: an integer
# Returns

# int: the unsigned decimal integer result
# Input Format

# The first line of the input contains , the number of queries.
# Each of the next  lines contain an integer, , to process.

def flippingBits(n):
    mask = 2**32 - 1
    return n ^ mask

# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix arr  is shown below:

# 1 2 3
# 4 5 6
# 9 8 9  
# The left-to-right diagonal = 1+5+9 = 15. The right to left diagonal = 3+5+9 = 17. Their absolute difference is |15-17| = 2.

# Function description

# Complete the diagonalDifference  function in the editor below.

# diagonalDifference takes the following parameter:

# int arr[n][m]: an array of integers
# Return

# int: the absolute diagonal difference
# Input Format

# The first line contains a single integer, , the number of rows and columns in the square matrix .
# Each of the next  lines describes a row, , and consists of  space-separated integers .

def diagonalDifference(arr):
    l_to_r = 0
    r_to_l = 0
    i = 0

    while i < len(arr):
        l_to_r += arr[i][i]
        i += 1
    i = 0
    j = len(arr) - 1

    while j >= 0:
        r_to_l += arr[i][j]
        i += 1
        j -= 1
    return abs(l_to_r - r_to_l)



