import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/achieng/robotics/robot_four/src/mobile_dd_robot/install/mobile_dd_robot'
