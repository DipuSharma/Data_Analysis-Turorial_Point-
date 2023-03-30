import pandas as pd
from pandas_profiling import ProfileReport
import numpy as np
import matplotlib.pyplot as plt
import seaborn as snb

# import os

# data = os.listdir()
df = pd.read_csv('supermarket_sales - Sheet1.csv')
print(df.info())
print(df.head())