import numpy as np

def get_list_list_of_factors_slow(N):
    numbers = np.linspace(1, N, N)
    factors = numbers[N%numbers == 0]
    return factors

def get_list_list_of_factors_fast(N):
    root = np.power(N,.5)
    factors = []
    print(f"checking numbers up to {np.floor(root)}")
    for i in range(1,int(np.floor(root))+1):
        if np.remainder(N,i) == 0:
            factors.append(i)
            factors.append(N/i)
    return factors


if __name__ == "__main__":
    N=199
    factors = get_list_list_of_factors_slow(N)
    print(factors)
    N=292
    factors = get_list_list_of_factors_slow(N)
    print(np.sort(factors))

