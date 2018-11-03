import cv2
import os


def video2frame(video_src,save_path):
    cap = cv2.VideoCapture(video_src)
    count=cap.get(cv2.CAP_PROP_FRAME_COUNT)

    interval=int(count/20)+1

    for i in range(0,int(count),interval):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        a, b = cap.read()
        cv2.imwrite(save_path+os.sep+'%d.jpg' % int(i/interval), b)


if __name__ == '__main__':
    video2frame('0.mp4','pic')