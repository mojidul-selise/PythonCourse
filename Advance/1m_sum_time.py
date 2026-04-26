from time import time
def timer(func):
    def wrapper(n):
        start_time = time()
        result = func(n)
        end_time = time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

@timer
def sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

sum = sum(1000000)
print(sum)