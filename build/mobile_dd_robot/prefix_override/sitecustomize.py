import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/achieng/robotics/robot_four/install/mobile_dd_robot'
