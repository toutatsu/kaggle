import numpy as np
import matplotlib.pyplot as plt

sample_num=42000
test_num=28000
d=784

def data_load():
    print("train data loading...",flush=True,end="")
    digit_data=np.loadtxt("train.csv",dtype=int,delimiter=",",skiprows=1,max_rows=sample_num,usecols=np.arange(1,d+1))
    label=np.loadtxt("train.csv",dtype=int,delimiter=",",skiprows=1,max_rows=sample_num,usecols=(0))
    print("loaded",flush=True)

    print("test data loading...",flush=True,end="")
    digit_test=np.loadtxt("test.csv",dtype=int,delimiter=",",skiprows=1)
    print("loaded",flush=True)

    return digit_data,label,digit_test

#https://stackoverflow.com/questions/37228371/visualize-mnist-dataset-using-opencv-or-matplotlib-pyplot
def digit_visualize(digit_data,label=None):
    plt.title('digit:{}'.format(label))
    plt.imshow(np.array(digit_data, dtype='uint8').reshape((28, 28)), cmap='gray')
    plt.show()

def write_prediction(file_name,predictions):
    with open(file_name, mode='w') as f:
        f.write("ImageId,Label\n")
        for i in range(0,test_num):
            print("{}".format(i),flush=True)
            f.write("{},{}\n".format(i+1,predictions[i]))
