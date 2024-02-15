import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
import cv2
import numpy as np


class ViewCompressedImage(Node):
    def __init__(self):
        super().__init__('pi_image_compressed_viewer')
        self.create_subscription(
            CompressedImage,
            'camera/image/compressed',
            self.image_callback,
            1
        )

    def image_callback(self, msg):
        np_arr = np.frombuffer(msg.data, np.uint8)
        image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        cv2.imshow('PI Camera View', image_np)
        cv2.waitKey(1)


def main(args=None):
    rclpy.init(args=args)
    viewer = ViewCompressedImage()
    rclpy.spin(viewer)
    viewer.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
