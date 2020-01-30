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
- main.py を整理する

- sound.py mp3ファイルにも対応させる
- 画像指定無い場合のデフォルト画面作る

- 音源流す条件増やす
- 条件に合わせた音源を探す

- opencv haar-cascade検出器の原理読む  
https://algorithm.joho.info/machine-learning/haar-like-cascades-face-detection/  