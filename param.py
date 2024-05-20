# ================= take_photo.py ==============================

MIN_LEN = 20  # 検出する直線の最小長さ
MAX_GAP = 200  # 直線として認識する最大の間隔
GRAY_THR = 20  # 濃度変化の閾値
CUT_MODE = True  # True:検出物体を切り取って保存, False:画像全体をそのまま保存

# ================= label_img.py ==============================
SRC_DIR = 'image_data/tmp'
DEST_ALPHA = 'image_data/all/alpha'
DEST_COSMIC = 'image_data/all/cosmic'

# ================= train_net.py ==============================
DATA_DIR = 'image_data/all'             # 画像フォルダ名
CKPT_PROCESS = 'train_process.ckpt'     # 学習経過保存ファイル名
CKPT_NET = 'trained_net.ckpt'           # 学習済みパラメータファイル名
NUM_CLASSES = 2                         # クラス数
NUM_EPOCHS = 100                        # 学習回数
LEARNING_RATE = 0.01                    # 学習率

# ================= realtime_classification.py ==============================

CKPT_NET = 'trained_net.ckpt'               # 学習済みパラメータファイル
OBJ_NAMES = ['alpha', 'cosmic']             # 各クラスの表示名
# MIN_LEN = 20
# GRAY_THR = 20
CONTOUR_COUNT_MAX = 3       # バッチサイズ(一度に検出する物体の数)の上限
SHOW_COLOR = (255, 191, 0)  # 枠の色(B,G,R)

NUM_CLASSES = 2  # クラス数
PIXEL_LEN = 112  # Resize後のサイズ(1辺)
CHANNELS = 1     # 色のチャンネル数(BGR:3, グレースケール:1)