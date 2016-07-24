## 1_submission: always 1
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
df_sample = pd.read_csv("./data/sample_submission.csv")
# df_sample
df_train = pd.read_csv("./data/train.csv")
# df_train
df_test = pd.read_csv("./data/test.csv")
# df_test
for i in range(113844):
    df_sample['Last'][i] = 1
df_sample.to_csv("1_submission.csv", index=False)

## 2_submission: 等差数列
L = df_test['Sequence'].tolist()

Id = df_test['Id'].tolist()
n = len(L)
M = [map(int, L[i].strip().split(',')) for i in range(n)]
Last = [(2*M[i][-1] - M[i][-2]) if len(M[i]) >= 2 else M[i][-1] for i in range(n)]

df_result = DataFrame(np.array([Id, Last]).T, columns=['Id', 'Last'])
df_result.to_csv("2_submission.csv", index=False)
