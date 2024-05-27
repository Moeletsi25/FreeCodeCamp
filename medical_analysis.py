import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Reading medical data visualization
df = pd.read_csv("medical_examination.csv")

# Creating the overweight column in the df variable
df["overweight"] = (df["weight"] / (df["height"] / 100) ** 2 > 25).astype(int)

# Normalizing data by making 0 always good and 1 always bad
df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
df["gluc"] = (df["gluc"] > 1).astype(int)

#Convert the data into long format and create a chart using seaborn

df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])
df_cat = df_cat.rename(columns={"variable": "variable", "value": "value"})
fig = sns.catplot(data=df_cat, x="variable", hue="value", kind="count", col="cardio")
# Drawing a heat map

# Cleaning data
df_heat = df[
    (df["ap_lo"] <= df["ap_hi"]) &
    (df["height"] >= df["height"].quantile(0.025)) &
    (df["height"] <= df["height"].quantile(0.975)) &
    (df["weight"] >= df["weight"].quantile(0.025)) &
    (df["weight"] <= df["weight"].quantile(0.975))
]

# Calculating correlation matrix
corr = df_heat.corr()
print(corr)

# Generating mask for upper triangle
mask = np.triu(corr)
print(mask)

# Set up matplotlib figure
fig, ax = plt.subplots(figsize=(10, 8))
plt.show()

# Plot heatmap
sns.heatmap(corr, annot=True, fmt=".1f", cmap="coolwarm", mask=mask, square=True, linewidths=0.5, cbar_kws={"shrink": 0.8})
plt.show()