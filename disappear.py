import cv2
import numpy as np


# s*s個に分割する
def mean_pooling(img, s=1, d=0):
    if len(img.shape) == 3:
        out = img.copy().astype(np.float32)
    if len(img.shape) == 2:
        out = img.copy().astype(np.float32)
        out = np.expand_dims(out, -1)

    h, w, c = out.shape

    dy = h // s
    dx = w // s
    for i in range(s):
        for j in range(s):
            for k in range(c):
                out[dy*i:dy*(i+1), dx*j:dx*(j+1), k] \
                    = np.mean(out[dy*i:dy*(i+1), dx*j:dx*(j+1), k])
    out += d
    
    #下限上限
    out = np.clip(out, 0, 255)

    out = out.astype(np.uint8)

    return out


img = cv2.imread("image.png")
img2 = img.copy()
H, W, C = img.shape
x = min(H, W)

for s in range(1, x//30)[::-1]:
    img2 = mean_pooling(img2, s, d=-5)
    cv2.imshow("", img2)
    cv2.waitKey(100)

cv2.waitKey(0)
cv2.destroyAllWindows()