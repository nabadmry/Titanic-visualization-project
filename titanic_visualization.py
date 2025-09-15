# Titanic Dataset Visualization Project
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os

# ✅ Make sure images folder exists
os.makedirs("images", exist_ok=True)

# ✅ Load dataset (adjust path if needed)
df = pd.read_csv("dataset/train.csv")
print("First 5 rows of the dataset:")
print(df.head())

# 1. Survival count
plt.figure(figsize=(6,4))
sns.countplot(x='Survived', data=df, palette='Set2')
plt.title('Survival Count')
plt.savefig('images/survival_count.png')
plt.show()

# 2. Survival by Gender
plt.figure(figsize=(6,4))
sns.countplot(x='Sex', hue='Survived', data=df, palette='Set1')
plt.title('Survival by Gender')
plt.savefig('images/survival_by_gender.png')
plt.show()

# 3. Survival by Class
plt.figure(figsize=(6,4))
sns.countplot(x='Pclass', hue='Survived', data=df, palette='Set3')
plt.title('Survival by Passenger Class')
plt.savefig('images/survival_by_class.png')
plt.show()

# 4. Age distribution
plt.figure(figsize=(6,4))
sns.boxplot(x='Survived', y='Age', data=df, palette='coolwarm')
plt.title('Age Distribution by Survival')
plt.savefig('images/age_distribution.png')
plt.show()

# 5. Fare distribution
plt.figure(figsize=(6,4))
sns.kdeplot(data=df, x='Fare', hue='Survived', fill=True)
plt.title('Fare Distribution by Survival')
plt.savefig('images/fare_distribution.png')
plt.show()

print("\n✅ All plots saved in the 'images/' folder!")
