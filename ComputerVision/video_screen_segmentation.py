import cv2
import numpy as np


class Between(object):
    def __init__(self, pathA, pathB):
        self.VideoA = cv2.VideoCapture(pathA)
        self.VideoB = cv2.VideoCapture(pathB)

    def VideoInfoRead(self):
        self.widthA = int(self.VideoA.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.heightA = int(self.VideoA.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.widthB = int(self.VideoB.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.heightB = int(self.VideoB.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fpsA = int(self.VideoA.get(cv2.CAP_PROP_FPS))
        self.fpsB = int(self.VideoB.get(cv2.CAP_PROP_FPS))
        self.width = max(self.widthA, self.widthB)
        self.height = max(self.heightA, self.heightB)
        self.fps = max(self.fpsA, self.fpsB)

    def VideoMake(self):
        self.VideoInfoRead()
        print(self.width)
        print(self.height)
        print(self.fps)
        videowriter = cv2.VideoWriter('out.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), self.fps, (self.width, self.height))
        successA, frameA = self.VideoA.read()
        successB, frameB = self.VideoB.read()
        while successA and successB:
            frameA = cv2.resize(frameA, (int(self.width / 2), int(self.height)), interpolation=cv2.INTER_CUBIC)
            frameB = cv2.resize(frameB, (int(self.width / 2), int(self.height)), interpolation=cv2.INTER_CUBIC)
            decollateFrame = np.hstack((frameA, frameB))
            videowriter.write(decollateFrame)
            successA, frameA = self.VideoA.read()
            successB, frameB = self.VideoB.read()
        videowriter.release()


tomake = Between('/Users/lingchen/PycharmProjects/like/interesting/test1.mp4', '/Users/lingchen/PycharmProjects/like/interesting/test2.mp4')
# tomake.VideoInfoRead()
tomake.VideoMake()