import numpy as np
from sklearn.naive_bayes import GaussianNB
X = np.array([[0, 90], [90, 180], [180, 270], [270, 360]])
Y = np.array([1, 2, 3, 4])
clf = GaussianNB()
clf.fit(X, Y)
a = input("enter the angle")
p = clf.predict([[a]])
print '%d is lies in quadrant %d' %(a,p[0])
