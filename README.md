# RaspberryPi ＆ PyTorch 深層学習を用いた、霧箱における飛跡のリアルタイム分類

picamera で霧箱内の映像を取得し、背景差分で飛跡を抽出したら、PyTorch で深層学習にかけて α 線と宇宙線の分類を行う

<dl>

## <dt>実行環境</dt>

## <dt>使い方</dt>

### <dd>Step1: 学習データの作成

- RaspberryPi 上で **take_photo.py** を実行し、学習に使う画像を撮影する。
- 飛跡の見えていない状態で背景を撮影したら、飛跡の撮影を行うと飛跡部分を切り取った画像が **image_data/tmp** に保存される。
- グレースケールした後で、背景画像との差分の絶対値を二値化し、マスクをかけたものに対し、Hough 変換によって直線検出されたものが緑の枠に囲まれて表示される。<br><br>

</dd>

### <dd>Step2: データのラベリング

- 撮影した画像データに対して **label_img.py** を実行し、ラベル付けを行う。

- ラベル付けされたデータは  **image_data/all/alpha** (cosmic) に保存される。<br><br>

</dd>

### <dd>Step3: PyTorchで学習

- PCで **train_net.py** を実行し、作ったデータをもとに学習を行う。

- 学習済みのパラメータは  **trained_net.ckpt** に保存され、途中から学習を再開できる。<br><br>

</dd>

### <dd>Step4: リアルタイム分類

- RaspberryPi 上で **realtime_classification.py** を実行し、**trained_net.ckpt** での学習結果に基づいてリアルタイムでの分類を行う。

- フリーズのおそれがあるため、実行に使用するコア数（デフォルト4）の変更を推奨
- バッチサイズ (一度に検出する物体の数) の上限数によってはフリーズするおそれがあるので注意 
<br><br>


</dd>

## <dt>学習モデル</dt>

以下に示されている **畳み込みニューラルネットワーク（CNN）** を使用している

<br><br>

## <dt>参考</dt>

コード作成をするにあたり、以下の文献を参考にした。

- Raspberry 3 B+ ＆ PyTorchの深層学習で、カメラ映像内の複数物体をリアルタイム分類
  
  https://qiita.com/AoChoco/items/a09b446460d95d5c9503

- 霧箱を用いた放射線の測定

  https://osksn2.hep.sci.osaka-u.ac.jp/theses/soturon/sotsuron2021-1.pdf

</dl>
