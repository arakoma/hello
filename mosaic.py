import cv2
import numpy as np


# s*s個に分割する
# sは画像のサイズ以下にしてね
# 画像サイズをsで割り切れない場合、端はモザイクっぽくする
# 処理内容はほぼ mean pooling 
def mosaic(img, s=1, d=0):
    if len(img.shape) == 3:
        out = img.copy().astype(np.float32)
    if len(img.shape) == 2:
        out = img.copy().astype(np.float32)
        out = np.expand_dims(out, -1)

    H, W, C = out.shape
    
    dy = H // s
    dx = W // s
    for i in range(s):
        for j in range(s):
            for c in range(C):
                out[dy*i:dy*(i+1), dx*j:dx*(j+1), c] \
                    = np.mean(out[dy*i:dy*(i+1), dx*j:dx*(j+1), c])
    
    # 端を処理
    for i in range(H):
        for j in range(dx*s, W):
            out[i, j] = out[i, j-1]
    for i in range(dy*s, H):
        for j in range(W):
            out[i, j] = out[i-1, j]
    
    out += d
    
    #下限上限
    out = np.clip(out, 0, 255)

    out = out.astype(np.uint8)

    return out


img = cv2.imread("image.png")
img2 = img.copy()
H, W, C = img.shape
x = min(H, W)

for s in range(1, 30)[::-1]:
    img2 = mosaic(img2, s)
    cv2.imshow("", img2)
    cv2.waitKey(50)

for s in range(1, 30):
    img2 = mosaic(img, s)
    cv2.imshow("", img2)
    cv2.waitKey(50)
else:
    cv2.imshow("", img)

cv2.waitKey(0)
cv2.destroyAllWindows()