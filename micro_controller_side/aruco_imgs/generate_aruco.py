from micro_controller_side.CameraStream.aruco_helper import ArucoHelper

hp = ArucoHelper()
for i in range(100):
   hp.generate_aruco_marker(i)