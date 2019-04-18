#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import pickle

model = pickle.load(open('Voting', 'rb'))
X_test11 = np.array([100,20,13,35,12,20], dtype=float)
X_test111 = np.reshape(X_test11, (1, 6))
predictions = model.predict(X_test111)
print(predictions)

