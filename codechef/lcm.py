n1 = int(input())
n2 = int(input())

mx = max(n1, n2)
while True:
    if mx % n1 == 0 and mx % n2 == 0:
        lcm = mx
        break
    mx += 1
print(lcm)    






