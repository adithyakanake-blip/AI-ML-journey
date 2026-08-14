n = 5

# Top half (including center row)
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

# Bottom half
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)
