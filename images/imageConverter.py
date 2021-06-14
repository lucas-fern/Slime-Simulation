import cv2
import numpy as np

img_name = 'LF3'
img_path = img_name + '.png'
img = cv2.imread(img_path, 0)

with open(img_name + '.txt', 'w') as f:
    rows, cols = img.shape
    print(f'static int gridWidth = {cols};', file=f)
    print(f'static int gridHeight = {rows};', file=f)
    print(f'static int blocked[{rows}][{cols}] = {{', file=f)
    for idx, row in enumerate(img):
        str_row = [str(i) for i in row]
        string = ', '.join(str_row)
        print(f'    {{{string}}}', end='', file=f)
        if idx != rows - 1:
            print(',', file=f)
    print('};', file=f)

