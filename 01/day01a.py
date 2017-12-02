s = "1122"

# ugly list comprehension
print(sum([int(s[i]) * (s[i] == s[(i + 1) % len(s)]) for i in range(len(s))]))
