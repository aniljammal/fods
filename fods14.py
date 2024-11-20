import pandas as pd
from collections import Counter
customer_ages = pd.Series([25, 30, 35, 40, 25, 30, 35, 25, 40, 30])
age_freq = customer_ages.value_counts()import pandas as pd
from collections import Counter
likes = pd.Series([10, 20, 10, 30, 20, 40, 10, 20, 30])
likes_freq = likes.value_counts()
print("Likes frequency distribution:\n", likes_freq)
print("Age frequency distribution:\n", age_freq)
