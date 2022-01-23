import cv2
import os
video_directory = "dataset/video/"
write_directory = "dataset/video_frames/"
with os.scandir(video_directory) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            print(entry.name)
        video_path = video_directory + entry.name
        video_name = entry.name.split('.')[0]
        dirname = write_directory + video_name + "/"
        if len(video_name) > 0:
            print(dirname)
            print(video_name)
            os.mkdir(dirname)
            vidcap = cv2.VideoCapture(video_path)
            success,image = vidcap.read()
            count = 0
            while success:
                success,image = vidcap.read()
                # print('Read a new frame: ', success)
                count += 1
                if count % 30 == 0 and image is not None:
                    cv2.imwrite(dirname + "frame%d.png" % count, image)     # save frame as PNG file      
                    print(count)
        
