import numpy as np
import matplotlib.pyplot as plt

sample_num = 42000
test_num = 28000
d = 784


def data_load():
    print("train data loading...", flush=True, end="")
    digit_data = np.loadtxt(
        "train.csv",
        dtype=int,
        delimiter=",",
        skiprows=1,
        max_rows=sample_num,
        usecols=np.arange(1, d+1)
    )
    label = np.loadtxt(
        "train.csv",
        dtype=int,
        delimiter=",",
        skiprows=1,
        max_rows=sample_num,
        usecols=(0)
    )
    print("loaded", flush=True)
    print("test data loading...", flush=True, end="")
    digit_test = np.loadtxt("test.csv", dtype=int, delimiter=",", skiprows=1)
    print("loaded", flush=True)

    return digit_data, label, digit_test


# https://stackoverflow.com/questions/37228371/visualize-mnist-dataset-using-opencv-or-matplotlib-pyplot
def digit_visualize(digit_data, height=28, width=28, label=None):
    plt.title('digit:{}'.format(label))
    plt.imshow(
        np.array(digit_data, dtype='uint8').reshape((height, width)),
        cmap='gray'
    )
    plt.show()


def write_prediction(file_name, predictions):
    with open(file_name, mode='w') as f:
        f.write("ImageId,Label\n")
        for i in range(0, test_num):
            print("{}".format(i), flush=True)
            f.write("{},{}\n".format(i+1, predictions[i]))


def visualize_2d(data, label, plot_name="digit", num=1000):
    digit_color = {
        0: "black",
        1: "red",
        2: "orange",
        3: "gold",
        4: "lime",
        5: "blue",
        6: "green",
        7: "cyan",
        8: "blue",
        9: "magenta"
    }
    plt.title(plot_name)
    for i in range(0, num):
        print(i)
        print(label[i])
        plt.scatter(
            data[i, 0],
            data[i, 1],
            color=digit_color[label[i]],
            marker="$"+str(label[i])+"$"
        )
    plt.show()
