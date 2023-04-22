import threading
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def compute_primes(start, end, result):
    primes = []
    for i in range(start, end + 1):
        if is_prime(i):
            primes.append(i)
    result.extend(primes)

result = []

# Define the range of numbers to compute primes for
N = int(1e6)
num_threads = int(input("Enter number of threads : "))
chunk_size = N // num_threads

# Create num_threads threads to compute primes
threads = []
for i in range(num_threads):
    start = i * chunk_size + 1
    end = (i + 1) * chunk_size
    t = threading.Thread(target=compute_primes, args=(start, end, result))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

# Print the results
print(len(result))