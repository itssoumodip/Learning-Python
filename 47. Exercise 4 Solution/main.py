st = input("Enter the Message : ")
words = st.split(" ")
coding = int(input("1 for Coding 0 for Decoding : "))

if (coding):
    n_words = []
    for word in words:
        if (len(word)>=3):
            r1 = 'hsg'
            r2 = 'iej'
            st_new = r1 + word[1:] + word[0] + r2
            n_words.append(st_new)
        else:
            n_words.append(word[::-1])
    print(" ".join(n_words))
else:
    n_words = []
    for word in words:
        if (len(word)>=3):
            st_new = word[3:-3]
            st_new = st_new[-1] + st_new[:-1]
            n_words.append(st_new)
        else:
            n_words.append(word[::-1])
    print(" ".join(n_words))
        