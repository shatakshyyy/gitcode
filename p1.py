import numpy as np
import time
list_size = 100000
py_list1 = list(range(list_size))
py_list2 = list(range(list_size))

np1 = np.arange(list_size)
np2 = np.arange(list_size)

start_time = time.time()
result_list = [py_list1[i] + py_list2[i] for i in range(list_size)]
end_time = time.time()
print(f"time taken with lists:{end_time - start_time:.6f} seconds")
start_time = time.time()
result_np = np1 + np2
end_time = time.time()
print(f"Time taken with NumPy: {end_time - start_time:.6f} seconds")