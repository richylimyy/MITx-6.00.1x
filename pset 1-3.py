# define position of letters. a=1, b=2...
pos = "abcdefghijklmnopqrstuvwxyz"

# convert string into list of positions
s_pos = []
for letter in s:
    s_pos.append(pos.index(letter))

# convert list of positions into substring counting list
# each substring is represented by 1,2,3... in their corresponding positions
ss_count = []
counter = 1
for posn in range(len(s_pos)):
    # counting list always starts with 1
    if posn == 0:
        pass
    # if in alphabetical order, add +1 to counting list
    elif s_pos[posn] >= s_pos[posn-1]:
        counter += 1
    # if not, add 1 to counting list
    else:
        counter = 1
    ss_count.append(counter)

# from counting list, find position of substring
ss_len = max(ss_count)
ss_pos = ss_count.index(ss_len) + 1

# print substring
print("Longest substring in alphabetical order is: " + s[ss_pos-ss_len:ss_pos])
