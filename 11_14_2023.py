# There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.

# Example
# strings = ['ab', 'ab', 'abc']
# queries = ['ab', 'abc', 'bc']


# There are 2 instances of 'ab', 1 of 'abc' and 0 of 'bc'. For each query, add an element to the return array, .

# Function Description

# Complete the function matchingStrings in the editor below. The function must return an array of integers representing the frequency of occurrence of each query string in strings.

# matchingStrings has the following parameters:

# string strings[n] - an array of strings to search
# string queries[q] - an array of query strings
# Returns

# int[q]: an array of results for each query

def matchingStrings(strings, queries):
    out = []
    for q_word in queries:
        count = 0
        for s_word in strings:
            if q_word == s_word:
                count += 1
        out.append(count)
    return out

# Given an array of integers, where all elements but one occur twice, find the unique element.

# Example

# a = [1,2,3,4,3,2,1]

# The unique element is 4.

# Function Description

# Complete the lonelyinteger function in the editor below.

# lonelyinteger has the following parameter(s):

# int a[n]: an array of integers
# Returns

# int: the element that occurs only once

def lonelyinteger(a):
    dic = {}
    for num in a:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1
    for key, value in dic.items():
        if value == 1:
            return key

