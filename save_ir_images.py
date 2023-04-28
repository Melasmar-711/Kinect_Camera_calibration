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

global img
def depth_call(image):

    print(image)
    #img = bridge.imgmsg_to_cv2(image.data, desired_encoding='passthrough')
    #cv2.imshow("ffgh", img)
    #cv2.waitKey('10')
    #print(img)




if __name__ == "__main__":
    global img_try
    rospy.init_node("ir_saver")

    raate=rospy.Rate(30)
    i=29
    ir_publisher = rospy.Publisher("ir_processed", Image, queue_size=30)
    while True:
        pTime = 0

        cap = rospy.wait_for_message("/camera/ir/image_raw", Image)
        #print(cap.encoding)
        cv_bridge = CvBridge()
        try:
            depth_image = cv_bridge.imgmsg_to_cv2(cap, desired_encoding='passthrough')
        except CvBridgeError:
            print('e')
        depth_array = np.array(depth_image, dtype=np.float32)
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=5), cv2.COLORMAP_JET)

        image_ir_calibrate = cv2.cvtColor(depth_colormap, cv2.COLOR_RGBA2GRAY)
        (thresh, w_h) = cv2.threshold(image_ir_calibrate, 40, 200, cv2.THRESH_BINARY_INV)


        cv2.imshow("Image", w_h)
        k=cv2.waitKey(1)
        w_h_depth_array=np.array(w_h, dtype=np.float32)
        
        depth_w_h = cv2.applyColorMap(cv2.convertScaleAbs(w_h, alpha=1), cv2.COLORMAP_JET)
        image_ir_calibrate = cv_bridge.cv2_to_imgmsg(depth_w_h, encoding="rgb8")


        #ir_publisher.publish(image_ir_calibrate)
        #raate.sleep()


        if k & 0xFF == ord('q'):
            break
        elif k & 0xFF == ord('s'):
            #cv2.imwrite(f"/home/asmar/projects_pycharm/calibration_demo/python_stereo_camera_calibrate-main/calib intrinsic/depth/ir_{i}.png",w_h)
            cv2.imwrite(f"/home/asmar/projects_pycharm/calibration_demo/python_stereo_camera_calibrate-main/frames_pair/ir/ir_8.png",w_h)
            i=i+1
            
            
    cv2.destroyAllWindows()

