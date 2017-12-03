m = [list(map(int, row.split())) for row in
     open('input.txt', 'r').read().split("\n")]

# PART 1 #

print(sum([max(row) - min(row) for row in m]))


# PART 2 #

print(sum([sum([sum([v // w for w in row if w < v and not v % w]) for v in row]) for row in m]))
