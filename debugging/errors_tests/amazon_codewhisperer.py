import pandas as pd

data = {0: [1, 2, 3, 4], 1: [2, 3], 2: [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)


# fix the bug in the code above


print(df.iloc[0, 1])
print(df.iloc[1, :])
print(df.iloc[2, 2:])