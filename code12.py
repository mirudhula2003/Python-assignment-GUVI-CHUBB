import numpy as np

scores = np.random.randint(0, 101, size=(10, 1000))

mean= np.mean(scores, axis=1)
median = np.median(scores, axis=1)
var = np.var(scores, axis=1)
std = np.std(scores, axis=1)

print("Mean:", mean)
print("Median:", median)
print("Variance:", var)
print("Standard deviation:", std)
