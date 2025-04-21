import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("C:\\Users\\mrkir\\Downloads\\archive (5)\\marriage_data_india.csv")
print(df)




sns.set(style="whitegrid")


#1. Age at Marriage vs Marital Satisfaction

plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Marital_Satisfaction', y='Age_at_Marriage', hue='Gender', palette="coolwarm")
plt.title("Age at Marriage vs Marital Satisfaction (by Gender)")
plt.legend(title='Gender')
plt.tight_layout()
plt.show()


#2.Divorce Rate by Marriage Type

plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Marriage_Type', hue='Divorce_Status', palette='Set2')
plt.title("Divorce Rate by Marriage Type (Hue: Divorce Status)")
plt.ylabel("Count")
plt.xlabel("Marriage Type")
plt.tight_layout()
plt.show()


# 3. Education Level vs Income Level (Count Plot with Income Level Hue).
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Education_Level', hue='Income_Level', palette='YlGnBu')
plt.title("Education Level vs Income Level (Hue: Income)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



#4. Urban vs Rural Comparison (Dowry & Parental Approval with Hue).

dowry_ct = pd.crosstab(df['Urban_Rural'], df['Dowry_Exchanged'], normalize='index') * 100
approval_ct = pd.crosstab(df['Urban_Rural'], df['Parental_Approval'], normalize='index') * 100


fig, axes = plt.subplots(1, 2, figsize=(14, 6))


sns.heatmap(dowry_ct, annot=True, fmt=".1f", cmap="Blues", ax=axes[0])
axes[0].set_title("Dowry Exchange by Region (%)")
axes[0].set_ylabel("Region")
sns.heatmap(approval_ct, annot=True, fmt=".1f", cmap="Greens", ax=axes[1])
axes[1].set_title("Parental Approval by Region (%)")
axes[1].set_ylabel("Region")
plt.tight_layout()
plt.show()




#5.Children Count vs Marital Satisfaction (Scatter Plot with Spouse Working Hue).

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x='Marital_Satisfaction',
    y='Children_Count',
    hue='Spouse_Working',
    palette='muted',
    s=100,
    alpha=0.7
)
plt.title("Children Count vs Marital Satisfaction (by Spouse Working)")
plt.xlabel("Marital Satisfaction")
plt.ylabel("Number of Children")
plt.legend(title="Spouse Working")
plt.tight_layout()
plt.show()

