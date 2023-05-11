import pandas as pd
import numpy as np
# create a new DataFrame
data = {'Name': ['John', 'Jane', 'Sam','Raj'],
        'Age': [25, 30, 35,40],
        'City': ['New York', 'Paris', 'London',np.nan]}
df = pd.DataFrame(data)

# print the DataFrame
print(df)
