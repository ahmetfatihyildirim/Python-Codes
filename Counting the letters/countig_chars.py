sentence = input("Please write your sentence to Count the number of each letter in a sentence: ")
output = {}
setof = set(sentence)

for i in setof:
    output[i] = sentence.count(i)
output

