import os
import shutil
import threading
import cv2


picture_path='video'


def video2frame(video_src,save_path):
    cap = cv2.VideoCapture(video_src)
    count=cap.get(cv2.CAP_PROP_FRAME_COUNT)

    interval=int(count/20)+1

    for i in range(0,int(count),interval):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        a, b = cap.read()
        cv2.imwrite(save_path+os.sep+'%d.jpg' % int(i/interval), b)


def delete_dirs(video_src_path):
    dirs = os.listdir(video_src_path)
    for dir in dirs:
        try:
            dir_path=video_src_path+os.sep+dir
            files=os.listdir(dir_path)

            video_path=''
            for file in files:
                suffix_name=os.path.splitext(file)[1] # 获取文件后缀名
                is_delete=True
                if suffix_name in video_formats:
                    is_delete=False
                    video_path=file
                    break
            if is_delete:
                print('deleted:',dir_path)
                shutil.rmtree(dir_path)
            else:
                # 处理视频
                pic=dir_path + os.sep + picture_path
                if not os.path.exists(pic):
                    os.makedirs(pic)
                video2frame(dir_path+os.sep+video_path,pic)

            is_delete=True
        except:
            pass


if __name__ == '__main__':
    video_src_path = '/home/yuhao/test'
    video_formats = ['.mp4']

    video_src_paths=os.listdir(video_src_path)
    # 采用多线程处理,每一个菜谱类别采用一个线程进行清洗
    for path in video_src_paths:
        t = threading.Thread(target=delete_dirs, args=(video_src_path+os.sep+path,))
        t.start()








