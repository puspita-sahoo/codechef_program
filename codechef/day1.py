##ATM

x, y = map(int, input().split(" "))
if x % 5 == 0 and y > x+0.5:
    y = y - (x + 0.5)
elif (x + 0.5) > y:
    print("Insufficient funds")
else:
    y = y
print(y)










