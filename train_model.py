import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
import joblib
from sklearn.preprocessing import StandardScaler

#load and preparing data

df = pd.read_csv("student_data.csv")

df['Result'] = df['Result'].map({'Pass': 1, 'Fail' :0})

x = df.drop('Result', axis=1)
y = df['Result']
print(y)

scaler = StandardScaler()
scaler.fit(x)
scaler.transform(x)
print(x.std(), y.std())
#split into train and test sets

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print(x.shape, X_train.shape, y_test.shape)

#train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

#evaluateing the model

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

#save the trained model in model.pkl

joblib.dump(model, "model.pkl")
print("Model saved as model.pkl")

#checking accuracy quickly

print ("Accuracy:", accuracy_score(y_test, y_pred))

