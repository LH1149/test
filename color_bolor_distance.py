# Untitled - By:

import sensor, image, time, math
from pyb import UART
import json
import ustruct

#
#white_threshold_01 = ((95, 100, -18, 3, -8, 4));  #白色阈值
red_threshold_01 = [(5, 37, 122, 34, -47, 31),(34, 54, 46, 15, 18, 57),(20, 48, -124, -10, -45, 127),(0, 30, 0, 64, -128, 0)];
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False) # must be turned off for color tracking
sensor.set_auto_whitebal(False) # must be turned off for color tracking
clock = time.clock()

uart = UART(3,115200)   #定义串口3变量
uart.init(115200, bits=8, parity=None, stop=1) # init with given parameters

def find_max(blobs):    #定义寻找色块面积最大的函数
    max_size=0
    for blob in blobs:
        if blob.pixels() > max_size:
            max_blob=blob
            max_size = blob.pixels()
    return max_blob

def sending_data(cx,cy):
    global uart;
    #frame=[0x2C,18,cx%0xff,int(cx/0xff),cy%0xff,int(cy/0xff),0x5B];
    #data = bytearray(frame)
    data = ustruct.pack("<bbhhb",              #格式为俩个字符俩个短整型(2字节)
                   0x2C,                       #帧头1
                   0x12,                       #帧头2
                   int(cx), # up sample by 4    #数据1
                   int(cy), # up sample by 4    #数据2

                   0x5B)
    uart.write(data);   #必须要传入一个字节数组

def recive_data():
    global uart
    if uart.any():
        tmp_data = uart.readline();
        print(tmp_data)


#mainloop
while(True):
    clock.tick() # Track elapsed milliseconds between snapshots().
    img = sensor.snapshot() # Take a picture and return the image.
    #  pixels_threshold=100, area_threshold=100
    blobs = img.find_blobs(red_threshold_01, area_threshold=150);
    cx=0;cy=0;a=0;
    if blobs:
        #如果找到了目标颜色
        max_b = find_max(blobs);
        # Draw a rect around the blob.
        img.draw_rectangle(max_b[0:4]) # rect
        #用矩形标记出目标颜色区域
        img.draw_cross(max_b[5], max_b[6]) # cx, cy
        img.draw_cross(160, 120) # 在中心点画标记
        #在目标颜色区域的中心画十字形标记
        cx=max_b[5];
        cy=max_b[8];

        img.draw_line((160,120,cx,cy), color=(127));
        #img.draw_string(160,120, "(%d, %d)"%(160,120), color=(127));
        img.draw_string(cx, cy, "(%d, %d)"%(cx,cy), color=(127));

    sending_data(cx,cy); #发送点位坐标
    recive_data();
    print(cx,cy);
    #time.sleep(1000)

#pack各字母对应类型
#x   pad byte        no value            1
#c   char            string of length 1  1
#b   signed char     integer             1
#B   unsigned char   integer             1
#?   _Bool           bool                1
#h   short           integer             2
#H   unsigned short  integer             2
#i   int             integer             4
#I   unsigned int    integer or long     4
#l   long            integer             4
#L   unsigned long   long                4
#q   long long       long                8
#Q   unsilong long   long                8
#f   float           float               4
#d   double          float               8
#s   char[]          string              1
#p   char[]          string              1
#P   void *          long
#  该程序只能输送x轴坐标，与需要的颜色坐标，如果输出x、y、颜色
#的话 单片机显示屏特别慢
