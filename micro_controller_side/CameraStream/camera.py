import threading
import cv2


class Camera(threading.Thread):
   def __init__(self,camName,camId):
      threading.Thread.__init__(self)
      self.camName = camName
      self.camId = camId
      self.cam = cv2.VideoCapture(self.camId)


   def cam_preview(self):
      cv2.namedWindow(self.camName)
      if self.cam.isOpened():  # try to get the first frame
         rval, frame = self.cam.read()
      else:
         rval = False

      while rval:
         cv2.imshow(self.camName, frame)
         rval, frame = self.cam.read()
         key = cv2.waitKey(20)
         if key == 27:  # exit on ESC
            break
      cv2.destroyWindow(self.camName)

   def get_camera_stream(self):
      return self.cam




