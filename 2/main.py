import matplotlib.pyplot as plt
import numpy as np

from perceptron import Perceptron as P
import dataImport as di



ppn = P(eta=0.1, n_iter=10)


ppn.fit(di.X, di.y)
plt.plot(range(1, len(ppn.errors_) +1),
ppn.errors_, marker='o')

plt.xlabel('Epochs')
plt.ylabel('Number of Updates')
plt.show()
