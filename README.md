dist フォルダにある.exe ファイルを開くと起動します。  


# 操作
1. 設定画面  
画像のpathを入力  
一番下のボタンクリックで設定完了  

2. カメラ映像  
カメラ位置、角度の調整をする  
okならキーボードのsキー押すと調整終了  

3. hello画面  
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

## memo
- main.py を整理する

- sound.py mp3ファイルにも対応させる
- 画像指定無い場合のデフォルト画面作る
- opencv haar-cascade検出器の原理読む  
https://algorithm.joho.info/machine-learning/haar-like-cascades-face-detection/  

- 画像指定しないと設定画面終えられないようにする  
- 設定で音声フラグ管理  
- 設定で入力しない場合の処理  

# 音声条件
- "おはよー"　起動時最初
  
#### 未実装
- "おつかれ"　時間経過  
- "n時間たちました"　時間経過  
- "n時です"　0,6,12,18,時にコール  
- "今日はm月d日x曜日です"　その日の初回起動時  
