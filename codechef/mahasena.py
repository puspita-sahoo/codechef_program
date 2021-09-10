n = int(input())
a = list(map(int, input().split()))
lucky = []
unlucky = []

for i in a:
    if i % 2 == 0:
        lucky.append(i)
    else:
        unlucky.append(i)
# print(lucky)
# print(unlucky)        
if len(lucky) > len(unlucky):
    print("READY FOR BATTLE")
else:
    print("NOT READY")

