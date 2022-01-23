from PIL import Image
import os
import math

GIF_directory = "dataset/gif/"
write_directory = "dataset/gif_frames/"
with os.scandir(GIF_directory) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            print(entry.name)
        gif_path = GIF_directory + entry.name
        gif_name = entry.name.split('.')[0]
        dirname = write_directory + gif_name + "/"
        if len(gif_name) > 0:
            print(dirname)
            print(gif_name)
            os.mkdir(dirname)
            im = Image.open(gif_path)
            num_frames = im.n_frames
            num_iters = math.floor(num_frames/10)
            for i in range(num_iters):
                im.seek(i*10)
                im.save("frame%d.png" % i*10)
            
            