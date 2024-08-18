#aruco test
import micro_controller_side.CameraStream.camera
from micro_controller_side.CameraStream import aruco_helper

camera = micro_controller_side.CameraStream.camera.Camera("camera1", 1)
helper = aruco_helper.ArucoHelper()

while True:
   helper.get_aruco_info(0,camera.get_camera_stream())