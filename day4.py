n = int(input().strip())

if n < 0:
    print("Negative input — stopping.")
else:
    for i in range(n-1, -1, -1):   # start at n-1, go down to 0
        print(i ** 2)
