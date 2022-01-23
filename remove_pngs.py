import os
for file in os.listdir('dataset/video/'):
    if file.endswith('.png'):
        os.remove(file) 
