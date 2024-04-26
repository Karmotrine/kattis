word1 = list(input())
word2 = list(input())
diff = len([word1[x] for x in range(len(word1)) if word1[x] != word2[x]])
print(diff + 1)