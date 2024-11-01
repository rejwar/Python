import timeit

execution_time = timeit.timeit(stmt='[x**2 for x in range(100)]', number=10000)
print(f"Execution time : {execution_time}")
