from collections import Counter

string = "conversation n"
instance = Counter(string)
print(instance.most_common(2)[1][0])
