import numpy as np
# import matplotlib.pyplot as plt

# import mnist


def PCA(data, test, r, row=False):
    print("PCA", flush=True)
    sample_num = 42000
    test_num = 28000
    # d=784
    if row:
        data = data.T  # データを縦ベクトルに
    # 共分散行列:分散（bias=0）
    Sigma = np.cov(data, rowvar=1, bias=0)
    eigen_values, eigen_vectors = np.linalg.eig(Sigma)
    # r=2;#写像する空間の次元
    U = eigen_vectors[:, 0:r]  # 固有値の大きい上位r個の固有ベクトル
    m = np.mean(data, axis=1)
    # 2次元空間X_に射影
    data_ = np.zeros((r, sample_num))
    for i in range(1, sample_num):
        data_[:, i] = U.T@(data[:, i]-m)
    if row:
        data_ = data_.T

    if row:
        test = test.T
    test_ = np.zeros((r, test_num))
    for i in range(1, test_num):
        test_[:, i] = U.T@(test[:, i]-m)
    if row:
        test_ = test_.T
    return data_, test_


# digit_data,label,digit_test=mnist.data_load()

# digit_data_,digit_test_=PCA(digit_data,digit_test,2)

# digit_color = {
#     0: "black",
#     1: "red",
#     2: "orange",
#     3: "gold",
#     4: "lime",
#     5: "blue",
#     6: "green",
#     7: "cyan",
#     8: "blue",
#     9: "magenta"
# }

# plt.title("PCA")
# for i in range(0,3000):
#     print(i)
#     print(label[i])
#     color=digit_color[label[i]]
#     digit="$"+str(label[i])+"$"
#     plt.scatter(digit_data_[i,0],digit_data_[i,1],color=color,marker=digit)

# plt.show()

# with open("train_PCA.csv", mode='w') as f:
#     # New file
#     f.write("label")
#     for i in range(0,d):
#         f.write(",pixel{}".format(i))
#     f.write("\n")
#     for i in range(0,sample_num):
#         f.write("{},{},{}\n".format(label[i],digit_data_[i,0],digit_data_[i,1],))

# #テストデータ
# test_num=28000
# digit_test=np.loadtxt("test.csv",dtype=int,delimiter=",",skiprows=1,max_rows=test_num,usecols=np.arange(0,d))

# digit_test=digit_test.T#データを縦ベクトルに

# digit_test_=np.zeros((r,test_num))#変換後のデータ

# for i in range(1,test_num):
#     digit_test_[:,i]=U.T@(digit_test[:,i]-m)

# digit_test_=digit__.T

# with open("test_PCA.csv", mode='w') as f:
#     # New file

#     for i in range(0,d):
#         f.write("pixel{},".format(i))
#     f.write("\n")
#     for i in range(0,test_num):
#         f.write("{},{}\n".format(digit_test_[i,0],digit_test_[i,1],))
