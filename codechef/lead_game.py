# 1st method======
# n = int(input())    #no. of rounds
# n = 5                    #no. of rounds
# lead = []
# for i in range(n):
#     p1, p2 = list(map(int, input().split()))
#     ms = max(p1, p2) - min(p1, p2)
#     leader = max(p1, p2)
#     lead.append(ms)
#     win = max(lead)

# print(win)
# print(leader)



# 2nd method======
# n = 5                    #no. of rounds
# lead = 0
# s1 = 0
# s2 = 0
# for i in range(n):
#     s1, s2 = list(map(int, input().split()))
#     if s1 > s2:
#         diff = s1-s2 
#         if diff > lead:
#             lead = diff
#             w = 1

#     else:
#         diff = s2-s1
#         if diff > lead:
#             lead = diff
#             w = 2
# print(w, lead)


# 3rd method======
n = int(input())
s1 = 0
s2 = 0
lead = 0
for i in range(n):
    s1,s2 = map(int, input().split())
    if s1 > s2:
        diff = s1 - s2
        if diff > lead:
            lead = diff
            w = 1
    else:
        diff = s2 - s1
        if diff > lead:
            lead = diff
            w = 2

print(w, lead)        