# coding=utf-8

import os
import cv2

videos_src_path = "/home/yuhao/test/asian"
video_formats = [".mp4"]
frames_save_path = "/home/yuhao/test/asian"


def video2frame(video_src_path, formats, frame_save_path):
    """
    将视频按固定间隔读取写入图片
    :param video_src_path: 视频存放路径
    :param formats:　包含的所有视频格式
    :param frame_save_path:　保存路径
    :return:　帧图片
    """

    files = os.listdir(video_src_path)
    print(files)
    for file in files:
        path_file = video_src_path + '/' + file
        if os.path.isfile(path_file + '/' + 'video' + '/' + '19.jpg'):
            continue
        videos = os.listdir(path_file)
        print(videos)

        def filter_format(x, all_formats):
            if x[-4:] in all_formats:
                return True
            else:
                return False

        videos = filter(lambda x: filter_format(x, formats), videos)
        if videos is None:
            print(videos)
            continue

        for each_video in videos:
            print('正在读取视频：', each_video)

            each_video_name = each_video[:-4]
            frame_save_path_1 = os.path.join(frame_save_path, each_video_name)
            frame_save_path_2 = os.path.join(frame_save_path_1, 'video')
            if not os.path.isdir(frame_save_path_2):
                os.mkdir(frame_save_path_2)
            each_video_save_full_path = os.path.join(frame_save_path_2) + "/"

            each_video_full_path = os.path.join(video_src_path+'/'+each_video_name, each_video)
            print(each_video_full_path)

            cap_init = cv2.VideoCapture(each_video_full_path)
            frame_index = 1
            if cap_init.isOpened():
                success = True
            else:
                success = False
                # os.chdir(frame_save_path_1)
                # os.system('del /Q *.mp4')
                print("读取失败!")
            frame_sum = 0
            while (success):
                success, frame = cap_init.read()
                print('---> 正在读取第%d帧:' % frame_index, success)
                frame_sum += 1
                frame_index += 1
            print('视频总%d帧：' % (frame_sum))
            cap = cv2.VideoCapture(each_video_full_path)
            count = 0  # 统计帧数
            frame_gap = int(frame_sum / 20)
            success = True
            i = 0
            # 每隔10帧读取一帧
            while (success):
                success, frame = cap.read()
                i = i + 1
                if (i == frame_gap):
                    print('######## 取到第%d帧:' % int(count+1), success)
                    # print 'Read a new frame:' , success
                    params = []
                    params.append(int(cv2.IMWRITE_JPEG_QUALITY))
                    params.append(95)
                    cv2.imwrite(each_video_save_full_path + '%d.jpg' % count, frame, params)
                    count = count + 1
                    frame_index = frame_index + 1
                    i = 0
            cap.release()


if __name__ == '__main__':
    video2frame(videos_src_path, video_formats, frames_save_path)
