import cv2
import numpy as np
"""
ty to this guy https://www.youtube.com/watch?v=YOpJrB6bQxo

"""

class ArucoHelper:
   def __init__(self):
      calib_data_path = "../calib_data/MultiMatrix.npz"

      self.calib_data = np.load(calib_data_path)
      self.aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_100)

      self.parameters = cv2.aruco.DetectorParameters()
      self.detector = cv2.aruco.ArucoDetector(self.aruco_dict, self.parameters)

      self.cam_mat = self.calib_data["camMatrix"]
      self.dist_coef = self.calib_data["distCoef"]
      self.r_vectors = self.calib_data["rVector"]
      self.t_vectors = self.calib_data["tVector"]

      self.MARKER_SIZE = 6  # centimeters (measure your printed marker size)

   def generate_aruco_marker(self, id=42, marker_size=200):
      """

      :param id:
      :param marker_size: size in pixels
      :return:
      """
      marker_image = cv2.aruco.generateImageMarker(self.aruco_dict, id, marker_size)
      cv2.imwrite(f'generated_aruco_{id}.png', marker_image)

   def get_aruco_info(self,camera_stream: cv2.VideoCapture):
      """
      :param camera_stream: cv2.VideoCapture
      :return:distance from a tag in cm and a tuple full of corners objects incase you wanna use that for some reason
      """
      ret, frame = camera_stream.read()
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      marker_corners, marker_IDs, reject = self.detector.detectMarkers(gray)

      if marker_corners:
         rVec, tVec, _ = self.my_estimatePoseSingleMarkers(
            marker_corners, self.MARKER_SIZE, self.cam_mat, self.dist_coef
         )
         total_markers = range(0, marker_IDs.size)
         for ids, corners, i in zip(marker_IDs, marker_corners, total_markers):

            corners = corners.reshape(4, 2)
            corners = corners.astype(int)
            top_right = corners[0].ravel()
            top_left = corners[1].ravel()
            bottom_right = corners[2].ravel()
            bottom_left = corners[3].ravel()

            # Calculating the distance in cm
            return  np.sqrt(
               tVec[i][0][2] ** 2 + tVec[i][0][0] ** 2 + tVec[i][0][1] ** 2
            ), (top_left,top_right,bottom_left,bottom_right)

   def my_estimatePoseSingleMarkers(self,corners, marker_size, mtx, distortion):
      '''
      This will estimate the rvec and tvec for each of the marker corners detected by:
         corners, ids, rejectedImgPoints = detector.detectMarkers(image)
      corners - is an array of detected corners for each detected marker in the image
      marker_size - is the size of the detected markers
      mtx - is the camera matrix
      distortion - is the camera distortion matrix
      RETURN list of rvecs, tvecs, and trash (so that it corresponds to the old estimatePoseSingleMarkers())
      '''
      marker_points = np.array([[-marker_size / 2, marker_size / 2, 0],
                                [marker_size / 2, marker_size / 2, 0],
                                [marker_size / 2, -marker_size / 2, 0],
                                [-marker_size / 2, -marker_size / 2, 0]], dtype=np.float32)
      trash = []
      rvecs = []
      tvecs = []
      for c in corners:
         nada, R, t = cv2.solvePnP(marker_points, c, mtx, distortion, False, cv2.SOLVEPNP_IPPE_SQUARE)
         rvecs.append(R)
         tvecs.append(t)
         trash.append(nada)
      return rvecs, tvecs, trash