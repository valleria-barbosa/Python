#A partir da var word = 'engenharia de software'. Se a indice word == 'e' or 'o', continue

word = 'engenharia de software'
i = 0

while i < len(word):
    if word[i] == 'e' or word[i] == 'o':
        i += 1
        continue
    print(word[i])
    i += 1