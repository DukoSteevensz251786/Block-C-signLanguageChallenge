import numpy as np
import pandas as pd

df = pd.read_csv(r'data/processed/hand_signs.csv')

print(df.shape)

print((df['label'] == 'I').sum()
)