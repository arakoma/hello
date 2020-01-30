# 操作
- 設定画面  
画像のpathを入力  
一番下のボタンクリックで設定完了
- カメラ映像  
カメラ位置、角度の調整をする  
okならキーボードのsキー押すと調整終了
- hello画面  
ここがメイン  
キーボードのqキーで終了  


## 音源
あみたろの声素材工房 様
http://www14.big.or.jp/~amiami/happy/  
使わせていただきますありがとうございます…！  


## haarcascades
検出器はopencvのリポジトリより。
https://github.com/opencv/opencv/tree/master/data/haarcascades  


## pythonモジュール
```python
pip install pygame opencv-python numpy
```

## todo
- 待機画面つくる
- 自作関数をモジュール化する(各関数の説明も書く)

- main.py が悪魔合体って感じなので整理する
- camera の映像は完成品は流さない(?)

- sound.py mp3ファイルにも対応させる

- 音源流す条件増やす
- 条件に合わせた音源を探す

- opencv haar-cascade検出器の原理読む  
https://algorithm.joho.info/machine-learning/haar-like-cascades-face-detection/  