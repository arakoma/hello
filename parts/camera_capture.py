import cv2


def camera_capture():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return
    
    while True:
        ret, frame = cap.read()

        frame_flip = cv2.flip(frame, 1)
        #frame表示
        cv2.namedWindow("", cv2.WINDOW_NORMAL)
        cv2.imshow("", frame_flip)

        #key入力で終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows


camera_capture()