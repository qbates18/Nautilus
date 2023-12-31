from packages.models.input import Data

CAM_RATE = 1
INPUT_RATE = 500
PROCESS_RATE = 100

THRESHOLD = 0.1

gamepad_flag = True
gamepad2_flag = True
cam_flag = False
socket_flag = True
altitude_lock_flag = False

top_data = Data(["FORWARD", "RIGHT", "BACK", "LEFT", "DOWN", "UP", "ROT_CCW", "ROT_CW", "S_TOG", "L_TOG", "CAM_UP", "CAM_DN"])
sub_data = Data(["ID", "TMPR", "DEPTH", "HEAD", "ALT"])

arm_inputs = Data(["S1_LEFT", "S1_RIGHT", "S2_FORWARD", "S2_BACK", "S3_FORWARD", "S3_BACK", "S4_OPEN", "S4_CLOSE", "S5_CW", "S5_CCW", "theta1", "theta2", "theta3"])

map_dict = None
map2_dict = None
