import pandas as pd
from sklearn.model_selection import train_test_split

# import file
df = pd.read_csv('../res/tp0/marambio_2007.dat', sep=r'\s+')

# create new data frame
stats = pd.DataFrame(index=['Mean', 'Max', 'Min', 'Median', 'Std', '25%', '50%', '75%'], columns=df.columns)

# fill new df for each model
for col in df:
    stats[col][0] = df[col].mean()
    stats[col][1] = df[col].max()
    stats[col][2] = df[col].min()
    stats[col][3] = df[col].median()
    stats[col][4] = df[col].std()
    stats[col][5] = df[col].quantile(.25)
    stats[col][6] = df[col].quantile(.75)
    stats[col][7] = df[col].quantile(.5)

print(stats)
print("\n\n")

# Split dataframes in test and train dataframes
train, test = train_test_split(df, test_size=0.2)

print("\n\n")
print(train.shape[0])
print(test.shape[0])
