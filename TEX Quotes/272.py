from sys import stdin
# lines = [x.strip() for x in stdin.readlines()]
lines = stdin.readlines()
lines = ''.join(lines)
quotes_indexes = []
for idx,char in enumerate(lines):
    if char == '"':
        quotes_indexes.append(idx)
lines = list(lines)
for idx in quotes_indexes[::2]:
        lines[idx] = "``"
for idx in quotes_indexes[1::2]:
        lines[idx] = "''"
lines = ''.join(lines)
print(lines, end="")
