import os

class CFG():

    data_path='./'
    output_path='.'

    debug=True

    seed=0

    device=None

    def __init__(self,competition_name='') -> None:

        self.competition_name=competition_name

        is_kaggle=os.getenv('KAGGLE_KERNEL_RUN_TYPE', '')

        if is_kaggle:
            self.is_kaggle=True
            self.data_path='/kaggle/input/'
            self.weights_path='/kaggle/input/'
            self.output_path='/kaggle/working/'

        else:
            self.is_kaggle=False
            self.data_path='../data/'
            self.weights_path='../output/'
            self.output_path='../output/'

        return

    # def torch():

    #     #高速化関連
    #     #https://qiita.com/sugulu_Ogawa_ISID/items/62f5f7adee083d96a587

    #     #GPU 遅くなるらしい↓
    #     torch.backends.cudnn.deterministic = True

    #     #イテレーションごとのnnの順伝搬および誤差関数の 計算手法がある程度一定であれば、torch.backends.cudnn.benchmark = Trueで GPU での計算が高速化
    #     torch.backends.cudnn.benchmark = False

    #     self.device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')



def set_seed(seed=0):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    #tf.random.set_seed(seed)
#     torch.manual_seed(seed)
#     torch.cuda.manual_seed(seed)
#     torch.cuda.manual_seed_all(seed)

# set_seed(CFG.seed)

