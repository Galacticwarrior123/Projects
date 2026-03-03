def match_words(words):
    ctr = 0
    lst = []

    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
        print(lst)
        return ctr
    
count = match_words(['abc', 'xyz', 'aga', 'feg'])
print(count)