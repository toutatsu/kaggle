import mnist
import numpy as np


def knn(k, data, test):
    sample_num = 42000
    test_num = 28000
    ans = np.zeros(test_num)
    for i in range(0, test_num):
        euclid_distance = np.zeros(sample_num)
        for j in range(0, sample_num):
            a = data[j, :]-test[i, :]
            a = a*a
            euclid_distance[j] = np.sum(a)
        print(i, flush=True)
        cnt = np.zeros(10)
        for K in range(0, k):
            cnt[int(label[np.argmin(euclid_distance)])] += 1
            euclid_distance[np.argmin(euclid_distance)] = 10000000
        print(cnt)
        ans[i] = np.argmax(cnt)
    return ans


digit_data, label, digit_test = mnist.data_load()
mnist.write_prediction("knn.csv", knn(7, digit_data, digit_test))
