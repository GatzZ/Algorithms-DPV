Alphabet = [chr(i + ord("A")) for i in xrange(26)]


def boyer_moore(text, pat):
    right = {c: -1 for c in Alphabet}
    for i, c in enumerate(pat):
        right[c] = i
    print right
    i = 0
    while i <= len(text) - len(pat):
        print text
        for k in xrange(i):
            print "",
        print pat
        print "-------------------"
        skip = 0
        for j in xrange(len(pat) - 1, -1, -1):
            if text[i + j] != pat[j]:
                skip = j - right[text[i + j]]
                if skip < 1:  # keep move to right
                    skip = 1
                break
        if skip == 0:
            return i

        i += skip
    return len(text)


text = "ABACADABRAC"
pat = "ABRA"
idx = boyer_moore(text, pat)
print idx
print text
for i in range(idx):
    print "",
print pat
