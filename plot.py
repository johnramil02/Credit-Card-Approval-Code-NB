import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()

np.random.seed(1234)
df = pd.DataFrame(np.random.randn(10, 4), columns=['Col1', 'Col2', 'Col3', 'Col4'])
ax1 = df.boxplot(column=['Col1', 'Col2', 'Col3'], figsize=(15,5), grid=True)
ax1.set_title('test title')
ax1.set_xlabel('x data')
ax1.set_ylabel('y data')

plt.show()