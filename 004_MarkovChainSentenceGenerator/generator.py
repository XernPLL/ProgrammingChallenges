import random

#speeches.txt from https://github.com/ryanmcdermott/trump-speeches

dict = {}
with open("speeches.txt","r",encoding="utf8") as file:
    text = file.read().split()
    for i in range(len(text)-1):
        word1 = text[i]
        word2 = text[i+1]
        if word1 in dict.keys():
            dict[word1].append(word2)
        else:
            dict[word1] = [word2]
            
n = int(input("How long sentence do u need?(Bigger than 0)"))
while(n < 1):
    n = int(input("How long sentence do u need?(Bigger than 0)"))
first = random.choice(list(dict.keys()))
while first.islower():
    first = random.choice(list(dict.keys()))
sentence = [first]
i = 0
while i<n-1:
    next = random.choice(list(dict[sentence[i]]))
    sentence.append(next)
    i = i + 1
print(" ".join(sentence))
