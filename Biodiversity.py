import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import os
data = pd.read_csv(r"<File location of the csv to be trained>")
categorical_columns = ['Metric ID', 'Project ID', 'Carbon Reduction (tons/year)', 'Renewable Energy (MWh/year)']
target_column = 'Biodiversity Index'
feature_columns = [col for col in data.columns if col != target_column]
label_encoders = {}
for column in categorical_columns:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le
X = data[feature_columns]
y = data[target_column]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
save_directory = r"<File Destiontion for the .joblib file to be saved>"
if not os.path.exists(save_directory):
    os.makedirs(save_directory)
model_path = os.path.join(save_directory, 'random_forest_model69.joblib')
encoders_path = os.path.join(save_directory, 'label_encoders69.joblib')
joblib.dump(model, model_path)
joblib.dump(label_encoders, encoders_path)
print(f'Model and encoders saved to {save_directory}')