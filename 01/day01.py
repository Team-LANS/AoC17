s = "123123"


# PART 1 #

print(sum([int(v) * (v == s[(i + 1) % len(s)]) for i, v in enumerate(s)]))


# PART 2 #

print(sum([int(v) * (v == s[(i + len(s) // 2) % len(s)]) for i, v in enumerate(s)]))
