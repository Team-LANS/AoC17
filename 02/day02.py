# PART 1 ######################################################################

m = [list(map(int, row.split())) for row in open('input.txt', 'r').read().split("\n")]

print(sum([max(row) - min(row) for row in m]))
