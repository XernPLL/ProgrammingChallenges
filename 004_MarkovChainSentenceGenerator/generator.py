import random

###########   TODO: MAKE IT BETTER

#copypasta.txt from https://github.com/louisabraham/copypasta-data
#sampletext.txt from https://github.com/lachlanpage/Markov-Chain-Sentence-Generator/blob/master/sampletext.txt
licznik = 0
dict = {}
with open("copypasta.txt","r") as file:
    for i in file:
        sentence = i.rstrip("\n")
        sentence = sentence.split()
        try:
            for n, j in enumerate(sentence):
                if j+" "+ sentence[n+1] in dict.keys():
                    dict[j + " " + sentence[n + 1]].add(sentence[n + 2])

                else:
                    dict[j + " " + sentence[n + 1]] = set()
                    dict[j + " " + sentence[n + 1]].add(sentence[n + 2])
        except IndexError:
            pass

with open("sampletext.txt","r") as file:
    for i in file:
        sentence = i.rstrip("\n")
        sentence = sentence.split()
        try:
            for n, j in enumerate(sentence):
                if j+" "+ sentence[n+1] in dict.keys():
                    dict[j + " " + sentence[n + 1]].add(sentence[n + 2])

                else:
                    dict[j + " " + sentence[n + 1]] = set()
                    dict[j + " " + sentence[n + 1]].add(sentence[n + 2])
        except IndexError:
            pass

creator = []
key, value = random.choice(list(dict.items()))
key = key.split()
creator.append(key[0])
creator.append(key[1])
wybor = random.choice(list(value))
creator.append(wybor)

try:
    while licznik < 10:
        value = random.choice(list(dict[key[1]+" "+ wybor]))
        creator.append(value)
        key[1] = wybor
        wybor = value
        licznik = licznik +1


except:
    print(" ".join(creator))

print(" ".join(creator))
