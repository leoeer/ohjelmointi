print("{:>4}{:>8}{:>12}".format("x", "2**x", "1/x"))
print("-"*24)
for x in range(1, 11):
    print("{:4.1f}{:8.1f}{:12.8f}".format(x, 2**x, 1/x))