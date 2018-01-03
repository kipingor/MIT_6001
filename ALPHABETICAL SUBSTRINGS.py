# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print "Longest substring in alphabetical order is: beggh"

#In the case of ties, print the first substring.
#For example, if s = 'abcbcd', then your program should print "Longest substring in alphabetical order is: abc"

from itertools import count

j = s[0:0]
for i in range(len(s)):
    for k in count(i + len(j) + 1):
        l = s[i:k]
        if len(l) != (k - i):
            break
        if sorted(l) == list(l):
            j = l

print("Longest substring in alphabetical order is: " + str(j))
