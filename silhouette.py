import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from log_kmedoid import k_medoid


def k_calassters(data, k_min=2, k_max=10):
    res = {i: 0 for i in range(k_min, k_max)}
    for i in range(k_min, k_max):
        res_km = k_medoid(data, iteration_constraint=300, k_amount=i, metrics_type=False, ret_table=False)
        medoids = []
        len_class = []
        for k in range(i):
            temp = 0
            for j in res_km:
                if j.k_class == k:
                    temp += 1
            len_class.append(temp)

        for k in res_km:
            if k.medoid:
                medoids.append(k)
        for k in res_km:
            temp = {}
            for j in res_km:
                if j.medoid and j.k_class != k.k_class:
                    temp.update({j.k_class: j + k})
            nearest = list(temp.keys())[list(temp.values()).index(min(list(temp.values())))]
            sum_nearest = 0
            for j in res_km:
                if j.k_class == nearest:
                    sum_nearest += k + j
            sum_nearest /= len_class[nearest]
            sum_same_k = 0
            for j in res_km:
                if j.k_class == k.k_class and j != k:
                    sum_same_k += k + j
            sum_same_k /= len_class[k.k_class]
            res[i] += (sum_nearest - sum_same_k) / max((sum_nearest, sum_same_k))
    return {i: res[i] / len(data) for i in res}


if __name__ == '__main__':
    data = np.array(pd.read_csv('irisDataNoHeadDotComma.csv', header=None))
    colors = ['red', 'green', 'blue', 'black', 'orange', 'yellow']
    ax = plt.subplots()[1]
    result = k_calassters(data)

    print(result)
