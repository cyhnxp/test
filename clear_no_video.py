import os
import shutil
import threading


def delete_dirs(video_src_path):
    dirs = os.listdir(video_src_path)
    for dir in dirs:
        try:
            dir_path=video_src_path+os.sep+dir
            files=os.listdir(dir_path)

            for file in files:
                suffix_name=os.path.splitext(file)[1] # 获取文件后缀名
                is_delete=True
                if suffix_name in video_formats:
                    is_delete=False
                    break
            if is_delete:
                print('deleted:',dir_path)
                shutil.rmtree(dir_path)
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








