from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression


X, y = load_iris(return_x_y=True)
clf = LogisticRegression(random_stat=0).fit(X, y)
clf.predict(X[:2, :])


# code after the bug correction:

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression


X, y = load_iris(return_X_y=True)
clf = LogisticRegression(random_state=0).fit(X, y)
clf.predict(X[:2, :])
