import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
import joblib

rfm = pd.read_csv("data/customer_segments.csv")

print("---  Printing firts 5 enteries ---")
print(rfm.head())

# customer is churned if no purchas in last 90 days
rfm['Churn'] = rfm['Recency'].apply(lambda x: 1 if x > 90 else 0)


print("priting the value counts of churn")
print(rfm['Churn'].value_counts(normalize=True))

# prepare fearutes
X = rfm[['Recency', 'Frequency', 'Monetary']]
y = rfm['Churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

rf = RandomForestClassifier(
    n_estimators=100,
    class_weight='balanced',
    random_state=42
)

rf.fit(X_train, y_train)

print("Making Prediction on test data and Printing the classification report")
y_pred = rf.predict(X_test)

print(classification_report(y_test, y_pred))

print("printing Feature importance from Random Forest feature importance attribute")

feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': rf.feature_importances_
}).sort_values(by='Importance', ascending=False)

print(feature_importance)

joblib.dump(rf, "models/churn_model.pkl")
print("Model saved")



