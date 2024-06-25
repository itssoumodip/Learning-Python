import random

# Predefined list of random words
random_words_list = ["apple", "banana", "cherry", "date", "fig", "grape", "honeydew", "kiwi", "lemon", "mango"]

# Function to get three random words
def get_random_words(n):
    return random.sample(random_words_list, n)

# Get user input for the message and coding/decoding choice
st = input("Enter the Message: ")
words = st.split(" ")
coding = int(input("1 for Coding, 0 for Decoding: "))

# Initialize the list for new words
n_words = []

# Process the message for coding
if coding:
    for word in words:
        if len(word) >= 3:
            r1 = 'hsg'
            r2 = 'iej'
            st_new = r1 + word[1:] + word[0] + r2
            n_words.append(st_new)
        else:
            n_words.append(word[::-1])
else:
    # Process the message for decoding
    for word in words:
        if len(word) >= 3:
            st_new = word[3:-3]
            st_new = st_new[-1] + st_new[:-1]
            n_words.append(st_new)
        else:
            n_words.append(word[::-1])

# Get three random words before and after the message
prefix_random_words = get_random_words(3)
suffix_random_words = get_random_words(3)

# Combine random words and the coded/decoded message
final_message = " ".join(prefix_random_words) + " " + " ".join(n_words) + " " + " ".join(suffix_random_words)

print(final_message)
