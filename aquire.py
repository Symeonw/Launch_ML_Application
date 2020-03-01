import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.read_excel("divorce.xlsx")
X = df.drop(columns=["Class"])
y = df.Class
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=123)
clf = RandomForestClassifier(max_depth=30, random_state=123)
clf.fit(X_train, y_train)
clf.score(X_train, y_train)
clf.score(X_test, y_test) #96.49% Accuracy


