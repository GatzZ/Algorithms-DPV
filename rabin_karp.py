def rabin_karp(text, pat):  # monte carlo version
    Q = 11111111111111111111111  # 23 digits of  1, a prime number
    R = 10  # Radix
    N = len(text)
    M = len(pat)
    RM = R ** (M - 1)
    pat_hash = int(pat) % Q
    txt_hash = int(text[:M]) % Q
    print "pat:", pat_hash
    print "txt:", txt_hash
    print "-----------------------------------"
    if pat_hash == txt_hash:  # match at beginning
        return 0
    i = M
    while i < N:
        txt_hash = (txt_hash - RM * int(text[i - M]) % Q) % Q  # remove leading digit
        txt_hash = (txt_hash * R + int(text[i])) % Q  # add trailing digit
        print "pat:", pat_hash
        print "txt:", txt_hash
        print "-----------------------------------"
        if txt_hash == pat_hash:
            return i - M + 1
        i += 1
    return M


text = "3141592653589793"
pat = "26535"
idx = rabin_karp(text, pat)
print idx
print text
for i in range(idx):
    print "",
print pat
