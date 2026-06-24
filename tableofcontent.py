import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import sklearn.metrics as metrics
data = pd.read_csv('../input/mobile-price-classification/')
data.head()