word = input("Enter a word")
word2 = ''
for letter in word:
    if letter != 'a' and letter != 'e' and letter != 'i' and letter != 'o' and letter != 'u':
        word2 = word2+letter

print(word2)
