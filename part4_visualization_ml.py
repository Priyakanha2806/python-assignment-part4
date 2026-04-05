import pandas as pd

df = pd.read_csv("students.csv")

print(df.head())
print(df.shape)
print(df.dtypes)
print(df.describe())

print(df['passed'].value_counts())

subject_cols = ['math','science','english','history','pe']

print("Pass avg:\n", df[df['passed']==1][subject_cols].mean())
print("Fail avg:\n", df[df['passed']==0][subject_cols].mean())

df['avg'] = df[subject_cols].mean(axis=1)
top_student = df.loc[df['avg'].idxmax()]
print("Top student:", top_student['name'], top_student['avg'])
import matplotlib.pyplot as plt

# 1. Pass vs Fail count
df['passed'].value_counts().plot(kind='bar')
plt.title("Pass vs Fail")
plt.xlabel("Result (0=Fail, 1=Pass)")
plt.ylabel("Number of Students")
plt.show()

# 2. Average marks per subject
subject_cols = ['math', 'science', 'english', 'history', 'pe']
df[subject_cols].mean().plot(kind='bar')
plt.title("Average Marks per Subject")
plt.ylabel("Marks")
plt.show()

# 3. Study hours vs Average marks
plt.scatter(df['study_hours_per_day'], df['avg'])
plt.title("Study Hours vs Average Marks")
plt.xlabel("Study Hours")
plt.ylabel("Average Marks")
plt.show()
df[['math','science','english','history','pe']].mean().plot(kind='bar')
plt.title("Average Marks per Subject")
plt.show()
plt.scatter(df['study_hours_per_day'], df['avg'])
plt.title("Study Hours vs Average Marks")
plt.show()