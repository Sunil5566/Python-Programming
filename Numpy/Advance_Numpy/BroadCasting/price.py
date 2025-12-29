import numpy as np

prices = np.array([100,20,400,5240])

discount = 10

final_prices = prices-(prices * discount/100)

print(final_prices)