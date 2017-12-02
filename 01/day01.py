s = "123123"

# PART 1 ######################################################################
# ugly list comprehension
print(sum([int(s[i]) * (s[i] == s[(i + 1) % len(s)]) for i in range(len(s))]))


# PART 2 ######################################################################
print(sum([int(s[i]) * (s[i] == s[(i + len(s) // 2) % len(s)]) for i in range(len(s))]))
