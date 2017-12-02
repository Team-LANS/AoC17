m = [list(map(int, row.split())) for row in open('input.txt', 'r').read().split("\n")]

# PART 1 ######################################################################

print(sum([max(row) - min(row) for row in m]))


# PART 2 ######################################################################

def div(l):
    for i, v in enumerate(l):
        for j, w in enumerate(l):
            if i != j:
                if gcd(v, w) > 1:
                    return gcd(v, w)

def gcd(a,b):
    print(a, ", ", b)
    while b:
        a, b = b, a % b
    print(a)
    return a


print(sum([div(row) for row in m]))
