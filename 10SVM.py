import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score
from sklearn.svm import SVC

data = pd.read_csv("es.csv")

data = data.drop('Email No.', axis=1)

X = data.drop('Prediction', axis=1)  # 'Prediction' is the target (spam/not spam)
y = data['Prediction']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

SVM = SVC(gamma='auto')  # Use 'auto' gamma for simplicity
SVM.fit(X_train, y_train)

y_pred = SVM.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("Accuracy: ", accuracy)
print("Precision: ", precision)
print("Recall: ", recall)

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix: ")
print(cm)

print("Classification Report: ")
print(classification_report(y_test, y_pred))