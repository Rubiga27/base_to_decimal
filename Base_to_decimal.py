A = input()
B = int(input())
decimal = 0
power = 1
for i in range(len(A) - 1, -1, -1):
    digit = int(A[i])
    decimal += digit * power
    power *= B
print(decimal)

