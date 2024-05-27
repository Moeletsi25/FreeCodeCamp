import pandas as pd

# let  'df' be  the DataFrame containing  dataset.
df = pd.read_csv("adult.data.csv")
# How many people of each race are represented in this dataset?
race_counts = df['race'].value_counts()
print(race_counts)
# What is the average age of men?
average_age_men = df[df['sex'] == 'Male']['age'].mean()
print("Avarage of age of men:", average_age_men)

# What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100

# What percentage of people with advanced education make more than 50K?
advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
percentage_advanced_education_more_than_50K = (df[advanced_education]['salary'] == '>50K').mean() * 100

# What percentage of people without advanced education make more than 50K?
percentage_no_advanced_education_more_than_50K = (df[~advanced_education]['salary'] == '>50K').mean() * 100

# What is the minimum number of hours a person works per week?
min_work_hours = df['hours-per-week'].min()

# What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
num_min_workers = df[df['hours-per-week'] == min_work_hours]
rich_percentage = (num_min_workers['salary'] == '>50K').mean() * 100

# What country has the highest percentage of people that earn >50K?
country_salary_df = df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()
highest_earning_country = country_salary_df.idxmax()
highest_earning_country_percentage = country_salary_df.max() * 100

# Identify the most popular occupation for those who earn >50K in India.
top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()
