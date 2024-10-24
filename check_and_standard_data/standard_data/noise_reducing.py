import pandas as pd

df = pd.read_csv('data/diabetes.csv')

columns_with_noise = ['Glucose', 'BMI']

df[columns_with_noise] = df[columns_with_noise].replace(0, pd.NA)

for col in columns_with_noise:
    df[col] = df[col].fillna(df[col].mean())



columns_with_noise = ['BloodPressure', 'SkinThickness', 'Insulin']
df[columns_with_noise] = df[columns_with_noise].replace(0, pd.NA)
for col in columns_with_noise:
    df[col] = df[col].fillna(df[col].median())

df.to_csv('data/diabetes_clean_data.csv',index=False)
print(df)