p = 28151

for g in range(2, p):
    if len(set(pow(g, i, p) for i in range(1, p))) == p - 1:
        print(g)
        break