import time
import  cv2
import os

str(time.strftime('%Y-%m-%d-%H-%M',time.localtime(time.time())))
class Camera(object):
    def __init__(self):
        self.video = cv2.VideoCapture('http://172.20.10.4:8080/video')
        self.width = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
        self.height = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
        self.fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.videowrite = None
        self.init = False #get video image, when save save many images, no need to initial always.
        # if self.user_name is not None and self.save_status:
        #     if not os.path.exists(self.user_name):
        #         os.mkdir(self.user_name)
        #
        #     self.videowrite= cv2.VideoWriter(self.user_name + os.sep + '%s.mp4'%str(time.strftime('%Y-%m-%d-%H-%M',
        #                                                                 time.localtime(time.time()))),fourcc,20.0, (width, height))

    def __del__(self):
        self.video.release()

    def get_frame(self, user_name, save_status):
        success, image = self.video.read() #opencv3 get image.

        if user_name is not None and user_name != "" and save_status:
            if self.init is False: #while circle, when in 'used' status save data, in 'not used' status, release.
                # init
                if not os.path.exists(user_name):
                    os.mkdir(user_name)

                self.videowrite= cv2.VideoWriter(user_name + os.sep + '%s.mp4'%str(time.strftime('%Y-%m-%d-%H-%M',
                                                                            time.localtime(time.time()))),
                                                 self.fourcc,20.0, (self.width, self.height))
                self.init = True
            else:
                self.videowrite.write(image)#Saving image to PC
        else:
            if self.init:
                self.videowrite.release()
                self.init = False
                self.videowrite = None

        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tostring()

