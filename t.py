import string
import csv

with open("data/SMSSpamCollection", encoding="utf-8") as f:
    data = list(csv.reader(f, delimiter="\t"))

def clean(s):
    translator = str.maketrans("", "", string.punctuation)
    return s.translate(translator)

X, y = [], []
for target, msg in data:
    X.append(msg)
    y.append(target)
X = [clean(x).lower() for x in X]

print(X[:3])

