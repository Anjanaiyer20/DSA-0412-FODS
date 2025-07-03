# 📦 1. Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from math import pi
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# 📥 2. Load Dataset
df = pd.read_csv("C:\\Users\\user\\OneDrive\\Documents\\Fundamentals of data science\\student-performance.csv")  # Full path to your file
# ✅ Create a new binary target based on test_score threshold
df['pass_fail'] = (df['test_score'] >= 50).astype(int)

# ✅ Show how many passed vs failed
print("🔍 New class distribution (after fixing):")
print(df['pass_fail'].value_counts())


# 🧼 3. Preprocessing: Encode Categorical Columns
df = df.apply(lambda col: col.astype('category').cat.codes if col.dtypes == 'object' else col)

# 🧾 4. Display Data Table and Column Names
print("🔍 Preprocessed Data Preview:")
print(df.head(10))
print("📑 Column Names:", df.columns.tolist())

# ✅ 5. Use 'pass_fail' as Target
target_col = 'pass_fail'
X = df.drop(target_col, axis=1)
y = df[target_col]

# 📊 6. Correlation Heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Feature Correlation Heatmap", fontsize=16)
plt.show()
print("✔ Full class distribution in pass_fail:")
print(df['pass_fail'].value_counts())


# ✂️ 7. Train-Test Split
# ✂️ 7. Train-Test Split (Stratified to preserve 0/1 balance)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# 🤖 8. Train Models
# Linear Regression
lin_model = LinearRegression()
lin_model.fit(X_train, y_train)
lin_preds = (lin_model.predict(X_test) >= 0.5).astype(int)

# Logistic Regression
log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train, y_train)
log_preds = log_model.predict(X_test)

# 🧪 9. Evaluation Function
def evaluate_model(y_true, y_pred):
    return {
        "Accuracy": accuracy_score(y_true, y_pred),
        "Precision": precision_score(y_true, y_pred),
        "Recall": recall_score(y_true, y_pred),
        "F1 Score": f1_score(y_true, y_pred)
    }

# 📊 10. Model Performance
lin_scores = evaluate_model(y_test, lin_preds)
log_scores = evaluate_model(y_test, log_preds)
results_df = pd.DataFrame([lin_scores, log_scores], index=['Linear Regression', 'Logistic Regression'])

print("\n📊 Model Performance Comparison:")
print(results_df)

# 🌐 11. Radar Chart
def plot_radar(data, title):
    labels = list(data.columns)
    num_vars = len(labels)
    angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))

    for i, row in data.iterrows():
        values = row.tolist()
        values += values[:1]
        ax.plot(angles, values, label=i, linewidth=2)
        ax.fill(angles, values, alpha=0.25)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=12)
    ax.set_yticklabels([])
    ax.set_title(title, size=16, pad=20)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    plt.tight_layout()
    plt.show()

# 📈 12. Show Radar Chart
plot_radar(results_df, "Linear vs Logistic Regression - Model Performance")
