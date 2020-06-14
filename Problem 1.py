vowels = "aeiou"
ans = 0
for letter in s:
    if letter in vowels:
        ans += 1
print ("Number of vowels: " + str(ans))
