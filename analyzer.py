# 2022 - Rafael Urben

import time
import random
import matplotlib.pyplot as plt
from tqdm import tqdm

def random_list(n):
    l = list(range(n))
    random.shuffle(l)
    return l

def generate_graph(algorithm, lengths=1000, samples=100, runs_per_sample=10):
    print("Generating graph...")

    results = []
    for listlength in tqdm(range(1, lengths)):
        wholetime = 0
        for _ in range(samples):
            unsortedlist = random_list(listlength)
            start = time.time()
            for _ in range(runs_per_sample):
                sortedlist = algorithm(unsortedlist)
            end = time.time()
            wholetime += (end-start)
        results.append(wholetime/samples)

    plt.plot(results, "b.")
    plt.show()

if __name__ == '__main__':
    print("Don't run this file directly!")
