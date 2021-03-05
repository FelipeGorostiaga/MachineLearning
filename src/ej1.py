import pandas as pd
import math
from sklearn.model_selection import train_test_split

# import file
df = pd.read_csv("marambio_2007.dat", sep="\s+")

# create new data frame
stats = pd.DataFrame(index=['Mean', 'Max', 'Min', 'Median'], columns=df.columns)

# fill new df for each model
for col in df:
    stats[col][0] = df[col].mean()
    stats[col][1] = df[col].max()
    stats[col][2] = df[col].min()
    stats[col][3] = df[col].median()

print(stats)

# Split dataframes in test and train dataframes
train, test = train_test_split(df, test_size=0.2)

print(train.shape[0])
print(test.shape[0])
