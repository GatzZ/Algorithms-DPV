def brute_force_substring1(text, pat):
    for i in range(len(text) - len(pat)):
        flag = True
        for j in range(len(pat)):
            if pat[j] != text[i + j]:
                flag = False
                break
        if flag:
            return i


def brute_force_substring2(text, pat):
    i, j = 0, 0
    while i < len(text) and j < len(pat):
        if text[i] == pat[j]:
            j += 1
        else:
            i -= (j - 1)  # move a position to right
            j = 0
        i += 1
    if j == len(pat):
        return i - j
    else:
        return len(text)


text = "ABACADABRAC"
pat = "ABRA"
idx = brute_force_substring1(text, pat)
print idx
print text
for i in range(idx):
    print "",
print pat
print "-----------------------------"

idx = brute_force_substring2(text, pat)
print idx
print text
for i in range(idx):
    print "",
print pat
