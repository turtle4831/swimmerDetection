import cv2
import numpy as np


class ArucoHelper:
   def __init__(self):
      self.aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_100)


      self.parameters = cv2.aruco.DetectorParameters()
      self.detector = cv2.aruco.ArucoDetector(self.aruco_dict, self.parameters)

   def generate_aruco_marker(self, id = 42, marker_size = 200):
      """

      :param id:
      :param marker_size: size in pixels
      :return:
      """
      marker_image = cv2.aruco.generateImageMarker(self.aruco_dict, id, marker_size)
      cv2.imwrite(f'generated_aruco_{id}.png', marker_image)

   def get_aruco_info(self, wanted_id, camera_stream: cv2.VideoCapture):
      """

      :param wanted_id: the id you want to get info from
      :param camera_stream: cv2.VideoCapture
      :return:
      """
      ret,frame = camera_stream.read()
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      corners, ids, rejected = self.detector.detectMarkers(gray)
      if ids is not None:
         print(f"corners: {corners}; ids: {ids};")







