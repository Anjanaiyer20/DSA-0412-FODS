import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)
n = 500

# Create sample data
data = {
    'hours_studied': np.random.randint(0, 10, size=n),
    'attendance_rate': np.random.uniform(50, 100, size=n),
    'extracurricular': np.random.choice(['yes', 'no'], size=n),
    'sleep_hours': np.random.uniform(4, 10, size=n),
    'internet_access': np.random.choice(['yes', 'no'], size=n),
    'parental_education': np.random.choice(['none', 'high_school', 'bachelor', 'master'], size=n),
    'test_score': np.random.randint(0, 101, size=n)
}

# Create DataFrame
df = pd.DataFrame(data)

# Add binary target: 1 = pass, 0 = fail
df['pass_fail'] = (df['test_score'] >= 50).astype(int)

# Save to CSV
df.to_csv("student-performance.csv", index=False)
print("✅ Dataset saved as 'student-performance.csv'")
