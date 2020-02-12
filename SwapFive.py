n = k = int(input())

p = 1
while (n * k != (n - k) // 10 + k * p):
    n += 10 * p * (((n % (10 * p)) * k) % (10 * p) // p)
    p *= 10

print(n)
