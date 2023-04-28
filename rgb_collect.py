import freenect
import cv2
import numpy as np
import rospy
import mediapipe as mp
import time
import stereo_msgs
import sensor_msgs
from sensor_msgs.msg import Image
from stereo_msgs.msg import DisparityImage
import openni_camera as oc

1
from cv_bridge import CvBridge, CvBridgeError

#global bridge
bridge = CvBridge()
#import calibkinect


def depth_call(image):

    print(image)
    #img = bridge.imgmsg_to_cv2(image.data, desired_encoding='passthrough')
    #cv2.imshow("ffgh", img)
    #cv2.waitKey('10')
    #print(img)




if __name__ == "__main__":

    i=11
    rospy.init_node("rgb_saver")
    #raate=rospy.Rate(30)

    while True:
        pTime = 0

        cap = rospy.wait_for_message("/camera/rgb/image_raw", Image)
        cap_1 = rospy.wait_for_message("/camera/rgb/image_rect_color", Image)
        
        #print(cap.encoding)
        cv_bridge = CvBridge()
        cv_bridge1 = CvBridge()
        try:
            rgb_image = cv_bridge.imgmsg_to_cv2(cap, desired_encoding='passthrough')
            rgb_rect=  cv_bridge1.imgmsg_to_cv2(cap, desired_encoding='passthrough')
        except CvBridgeError:
            print('e')

        cv2.imshow("Image", rgb_image)
        #cv2.imshow("image_rect",rgb_rect)
        k=cv2.waitKey(1)
        if k & 0xFF == ord('q'):
            break
        elif k & 0xFF == ord('s'):
            
            #cv2.imwrite(f"/home/asmar/projects_pycharm/calibration_demo/python_stereo_camera_calibrate-main/calib intrinsic/rgb/rgb_images/rgb_{i}.png",rgb_image)
            cv2.imwrite(f"/home/asmar/projects_pycharm/calibration_demo/python_stereo_camera_calibrate-main/frames_pair/rgb/rgb_8.png",rgb_image)
            i=i+1   


    cv2.destroyAllWindows()

