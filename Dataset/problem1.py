import pandas as pd

inventory_data = pd.read_excel('Dataset\Inventory.xlsx')

df = pd.DataFrame(inventory_data, index = range(0, 3000))

df.drop("Item No. ", axis=1, inplace=True)
print(df.info()) 
print(df.isnull().sum())


#null_data = df[df.isnull().any(axis=1)]
#print(null_data)

numerical_cols = df.select_dtypes(include=['number']).columns
categorical_cols = df.select_dtypes(include=['object', 'category', 'bool']).columns

# Impute missing values
# For numerical columns, use mean
df[numerical_cols] = df[numerical_cols].apply(lambda x: x.fillna(x.mean()))

# For categorical columns, use mode
for col in categorical_cols:
    if df[col].isnull().any():
        mode_val = df[col].mode()
        if not mode_val.empty:
            df[col] = df[col].fillna(mode_val[0])


print(df.isnull().sum())

print(df['State'].value_counts())

dummies = pd.get_dummies(df['State'], prefix='State')
