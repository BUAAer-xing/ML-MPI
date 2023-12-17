import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import randint
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('data.csv')

X = df.drop('best_process', axis=1)
y = df['best_process']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X = scaler.fit_transform(X)
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

rfc = RandomForestClassifier(max_depth=28, min_samples_leaf=7, min_samples_split=12, n_estimators=300)
rfc.fit(X_train, y_train)
y_pred = rfc.predict(X_test)
print("RFC_Accuracy:", accuracy_score(y_test, y_pred))

lr = LogisticRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)
print("LR_Accuracy:", accuracy_score(y_test, y_pred))

svc = SVC()
svc.fit(X_train, y_train)
y_pred = svc.predict(X_test)
print("SVC_Accuracy:", accuracy_score(y_test, y_pred))

DTC = DecisionTreeClassifier()
DTC.fit(X_train, y_train)
y_pred = DTC.predict(X_test)
print("DTC_Accuracy:", accuracy_score(y_test, y_pred))

GBC = GradientBoostingClassifier()
GBC.fit(X_train, y_train)
y_pred = GBC.predict(X_test)
print("GBC_Accuracy:", accuracy_score(y_test, y_pred))

KNC = KNeighborsClassifier(n_neighbors=5)
KNC.fit(X_train, y_train)
y_pred = KNC.predict(X_test)
print("KNC_Accuracy:", accuracy_score(y_test, y_pred))

MLP = MLPClassifier(hidden_layer_sizes=(100, 100), max_iter=1000)
MLP.fit(X_train, y_train)
y_pred = MLP.predict(X_test)
print("MLP_Accuracy:", accuracy_score(y_test, y_pred))

GNB = GaussianNB()
GNB.fit(X_train, y_train)
y_pred = GNB.predict(X_test)
print("GNB_Accuracy:", accuracy_score(y_test, y_pred))

print('=================================================================')

rfc = RandomForestClassifier(max_depth=28, min_samples_leaf=7, min_samples_split=12, n_estimators=300)
rfc.fit(X, y)
y_pred = rfc.predict(X)
print("RFC_Accuracy:", accuracy_score(y, y_pred))

lr = LogisticRegression()
lr.fit(X, y)
y_pred = lr.predict(X)
print("LR_Accuracy:", accuracy_score(y, y_pred))

svc = SVC()
svc.fit(X, y)
y_pred = svc.predict(X)
print("SVC_Accuracy:", accuracy_score(y, y_pred))

DTC = DecisionTreeClassifier()
DTC.fit(X, y)
y_pred = DTC.predict(X)
print("DTC_Accuracy:", accuracy_score(y, y_pred))

GBC = GradientBoostingClassifier()
GBC.fit(X, y)
y_pred = GBC.predict(X)
print("GBC_Accuracy:", accuracy_score(y, y_pred))

KNC = KNeighborsClassifier(n_neighbors=5)
KNC.fit(X, y)
y_pred = KNC.predict(X)
print("KNC_Accuracy:", accuracy_score(y, y_pred))

MLP = MLPClassifier(hidden_layer_sizes=(100, 100), max_iter=1000)
MLP.fit(X, y)
y_pred = MLP.predict(X)
print("MLP_Accuracy:", accuracy_score(y, y_pred))

GNB = GaussianNB()
GNB.fit(X, y)
y_pred = GNB.predict(X)
print("GNB_Accuracy:", accuracy_score(y, y_pred))

param_dist = {
    "max_depth": [3, None],
    "min_samples_split": np.arange(2, 11),
    "min_samples_leaf": np.arange(1, 11),
    "criterion": ["gini", "entropy"]
}
random_search = RandomizedSearchCV(
    DecisionTreeClassifier(),
    param_distributions=param_dist,
    n_iter=500,
    cv=2,
    verbose=1,
    n_jobs=-1,
    random_state=42,
    scoring='accuracy'
)
random_search.fit(X, y)
print("Best Parameters: ", random_search.best_params_)
print('Best score: ', random_search.best_score_)



