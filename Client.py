import socket
import os
import struct
from PIL import Image
import io
import cv2
import numpy as np

server_ip = '192.168.1.27'
server_port = 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((server_ip, server_port))
connection = sock.makefile('rb')
try:
    while True:
        # image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]        
        # if not image_len:
        #     break 
        # image_stream = io.BytesIO()
        # image_stream.write(connection.read(image_len))
        # image_stream.seek(0)
        # image = Image.open(image_stream)

        # print('Image is %dx%d' % image.size)
        # image.verify()
        # print('Image is verified')

        stream_bytes = connection.read(4) 
        leng = struct.unpack('<L', stream_bytes[:4])
        jpg = connection.read(leng[0])
        image = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
        cv2.imshow('stream', image)
        cv2.waitKey(1)


finally:
    connection.close()
    sock.close()