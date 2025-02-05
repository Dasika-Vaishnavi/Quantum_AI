import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import feather
from sklearn.utils import shuffle


train_data = feather.read_dataframe('data5_lumAB_train_normalized.feather')
test_data = feather.read_dataframe('data5_lumAB_test_normalized.feather')

lum_data = train_data.append(test_data, ignore_index=True)

data = shuffle(lum_data).reset_index(drop=True)
data.to_feather('Lum Data')