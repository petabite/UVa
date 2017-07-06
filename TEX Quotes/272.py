#import stdin
from sys import stdin

#read the input file and store it as a list
lines = stdin.readlines()

#join the lines together into one string
lines = ''.join(lines)

# create an empty list that will later store
# the positions of quotations marks
quotes_indexes = []

# loop thru each line in the input file and
# look for quotation marks. If one is found,
# add its index to the quotes_indexes list.
for idx,char in enumerate(lines):
    if char == '"':
        quotes_indexes.append(idx)

# turn the input file back into a list, with
# one character as one element
lines = list(lines)

# loop thru this list and replace each quotation
# using the indexes in quotes_indexes according to
# the problem.
for idx in quotes_indexes[::2]:
        lines[idx] = "``"
for idx in quotes_indexes[1::2]:
        lines[idx] = "''"

# join the input file again
lines = ''.join(lines)

# print the new, edited input file
print(lines, end="")
