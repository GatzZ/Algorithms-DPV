Alphabet = [chr(i + ord("A")) for i in xrange(26)]
print Alphabet


def kmp_substring(text, pat):
    dfa = {c: [0] * len(pat) for c in Alphabet}
    state = 0
    X = 0  # restart position
    # bulid the dfa array
    dfa[pat[0]][0] = 1
    for i in xrange(1, len(pat)):
        for c in Alphabet:
            dfa[c][i] = dfa[c][X]  # mismatched
        dfa[pat[i]][i] = i + 1  # matched case
        X = dfa[pat[i]][X]

    for i, c in enumerate(text):
        state = dfa[c][state]
        if state == len(pat):
            return i - len(pat) + 1
    return len(text)


text = "AABRAACADABRAACAADABRA"
pat = "AACAA"
idx = kmp_substring(text, pat)
print idx
print text
for i in range(idx):
    print "",
print pat
