# Step 0: Import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score
import plotly.graph_objects as go

# Step 1: Load the saved CSV and fix the formatting
df = pd.read_csv("winequality-red.csv")

# If only one column exists, it's a malformed CSV – fix it
if df.shape[1] == 1:
    df = df.iloc[:, 0].str.split(",", expand=True)

    # Assign proper column names manually
    df.columns = [
        'fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides',
        'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates',
        'alcohol', 'quality'
    ]

# Convert all values to numeric
df = df.apply(pd.to_numeric)

# Step 2: Visualize correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("📊 Correlation Heatmap - Wine Quality Features")
plt.show()

# Step 3: Basic statistics
stats = df.describe().T[['mean', 'std']]
stats['median'] = df.median()
stats['variance'] = df.var()

print("\n📈 Preprocessed Statistics (Top 5 features):")
print(stats[['mean', 'median', 'variance', 'std']].head())

# Step 4: Prepare for classification
df['quality_label'] = df['quality'].apply(lambda x: 1 if x >= 7 else 0)
df.drop('quality', axis=1, inplace=True)
print("\n📋 Preprocessed Data Table (first 10 rows):")
print(df.head(10))
import plotly.express as px

# Step 4.1: Innovative input data visualization - Parallel Coordinates Plot
fig = px.parallel_coordinates(
    df,
    color="quality_label",
    dimensions=[
        'fixed acidity', 'volatile acidity', 'citric acid',
        'residual sugar', 'chlorides', 'free sulfur dioxide',
        'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol'
    ],
    color_continuous_scale=px.colors.diverging.Tealrose,
    labels={"quality_label": "Quality Label"},
    title="🍷 Parallel Coordinates Plot - Input Feature Distributions by Wine Quality"
)

fig.show()



X = df.drop('quality_label', axis=1)
y = df['quality_label']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Step 5: Train models
svm = SVC()
svm.fit(X_train, y_train)
svm_preds = svm.predict(X_test)

rf = RandomForestClassifier()
rf.fit(X_train, y_train)
rf_preds = rf.predict(X_test)

# Step 6: Evaluation function
def evaluate(y_true, y_pred):
    return {
        'Accuracy': accuracy_score(y_true, y_pred),
        'F1 Score': f1_score(y_true, y_pred),
        'Recall': recall_score(y_true, y_pred),
        'Precision': precision_score(y_true, y_pred)
    }

svm_scores = evaluate(y_test, svm_preds)
rf_scores = evaluate(y_test, rf_preds)

print("\n🔍 SVM Performance:")
for metric, val in svm_scores.items():
    print(f"{metric}: {val:.2f}")

print("\n🔍 Random Forest Performance:")
for metric, val in rf_scores.items():
    print(f"{metric}: {val:.2f}")

# Step 7: Radial Performance Graph
metrics = list(svm_scores.keys())
svm_values = list(svm_scores.values())
rf_values = list(rf_scores.values())

fig = go.Figure()

fig.add_trace(go.Barpolar(
    r=svm_values,
    theta=metrics,
    name='SVM',
    marker_color='navy',
    opacity=0.7
))

fig.add_trace(go.Barpolar(
    r=rf_values,
    theta=metrics,
    name='Random Forest',
    marker_color='darkred',
    opacity=0.7
))

fig.update_layout(
    title="🍷 Radial Comparison - SVM vs Random Forest on Wine Quality",
    polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
    showlegend=True
)

fig.show()
