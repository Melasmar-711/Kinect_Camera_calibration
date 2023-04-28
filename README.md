# Kinect_Camera_calibration
this is a package to help you do intrinstic calibration for both rgb and ir cameras of the kinect camera and also do extrinsic calibration between them


this package is built using with some modifications to the following repo https://github.com/TemugeB/python_stereo_camera_calibrate
to make it suitable for a kinect camera.

# steps
1) you will need to install openni ros packages 
2) install the requirments using `pip install -r requirments.txt`
3) run the rgb_collect.py 
4) run the save_ir_images.py
5) check the path passed to the functions in the calib.py
6) run the calib.py
