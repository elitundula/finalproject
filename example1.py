import numpy as np
import time

list_a = [1] * 10**6
list_b = [2] * 10**6

start = time.time()
result_list = [x + y for x, y in zip(list_a, list_b)]
end = time.time()
print(f"Python list addition took {end - start:.4f} seconds")

array_a = np.ones(10**6, dtype=np.int32)
array_b = np.full(10**6, 2, dtype=np.int32)

start = time.time()
result_array = array_a + array_b
end = time.time()
print(f"NumPy array addition took {end - start:.4f} seconds")
