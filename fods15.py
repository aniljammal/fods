import pandas as pd
from collections import Counter
likes = pd.Series([10, 20, 10, 30, 20, 40, 10, 20, 30])
likes_freq = likes.value_counts()
print("Likes frequency distribution:\n", likes_freq)
