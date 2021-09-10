n = 7    
for i in range(2, n):
    if n % i == 0:
        prime = 'no'
        break
else:
    prime = 'yes'
print(prime)