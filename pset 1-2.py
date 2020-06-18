iteration = len(s) - 1
ans = 0
for x in range(iteration):
    if s[x:x+3] == 'bob':
        ans += 1
print("Number of times bob occurs is: " + str(ans))
