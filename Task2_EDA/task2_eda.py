import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("charts", exist_ok=True)

# Load the Titanic dataset
df = pd.read_csv("Task1_Data_Cleaning/Titanic.csv")

# Display the first five rows
print("First 5 rows of the Titanic dataset:")
print(df.head())

# Display the number of rows and columns
print("\nDataset shape:")
print(df.shape)
# Calculate descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate records
print("\nDuplicate Rows:")
print(df.duplicated().sum())
# Analyze passenger survival
print("\nSurvival Count:")
print(df["Survived"].value_counts())

print("\nSurvival Percentage:")
print(df["Survived"].value_counts(normalize=True) * 100)
# Analyze survival by gender
print("\nSurvival Count by Gender:")
print(df.groupby("Sex")["Survived"].value_counts())

print("\nSurvival Rate by Gender (%):")
print(df.groupby("Sex")["Survived"].mean() * 100)
# Visualize survival rate by gender
survival_rate = df.groupby("Sex")["Survived"].mean() * 100

survival_rate.plot(kind="bar", color=["orange", "skyblue"])

plt.title("Titanic Survival Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Survival Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/chart1.png", bbox_inches="tight")
plt.show()

# Analyze survival by passenger class
print("\nSurvival Rate by Passenger Class (%):")
print(df.groupby("Pclass")["Survived"].mean() * 100)

# Visualize survival rate by passenger class
class_survival = df.groupby("Pclass")["Survived"].mean() * 100

class_survival.plot(kind="bar")

plt.title("Titanic Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/chart2.png", bbox_inches="tight")
plt.show()

# Analyze survival by age
df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[0, 12, 18, 35, 60, 100],
    labels=["Child", "Teenager", "Young Adult", "Adult", "Senior"]
)

print("\nSurvival Rate by Age Group (%):")
print(df.groupby("AgeGroup", observed=False)["Survived"].mean() * 100)

# Visualize survival rate by age group

age_survival = df.groupby("AgeGroup", observed=False)["Survived"].mean() * 100

age_survival.plot(kind="bar")
plt.title("Titanic Survival Rate by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Survival Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/chart3.png", bbox_inches="tight")
plt.show()