n1 = int(input())
n2 = int(input())

hcf = 0
mn = min(n1, n2)
for i in range(1, mn+1):
    if mn % i == 0 and n2 % i == 0:
        hcf = i
print(hcf)

