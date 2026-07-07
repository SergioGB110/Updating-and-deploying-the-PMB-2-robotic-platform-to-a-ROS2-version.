#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class ScanFix(Node):

    def __init__(self):
        super().__init__('scan_fix')

        self.sub = self.create_subscription(
            LaserScan,
            '/scan',
            self.cb,
            10)

        self.pub = self.create_publisher(
            LaserScan,
            '/scan_fixed',
            10)

    def cb(self, msg):
        msg.header.frame_id = msg.header.frame_id.lstrip('/')
        self.pub.publish(msg)

def main():
    rclpy.init()
    node = ScanFix()
    rclpy.spin(node)

if __name__ == '__main__':
    main()