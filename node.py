import rclpy
import math
from rclpy.node import Node
from std_msgs.msg import Float64
from sensor_msgs.msg import WheelSpeed
# Part 1 of New Member Project for driverless teaching
class AvgWheelSpeedNode(Node):
    def __init__(self):
        super().__init__('avg_wheel_speed_node')
        self.subscription = self.create_subscription(
            WheelSpeed,
            '/ros_can/wheel_speeds',
            self.wheel_speed_callback,
            10
        )
        self.publisher_ = self.create_publisher(Float64, '/avg_wheel_speeds', 10)
        self.avg_speed = 0.0
        self.wheel_radius = 0.515  # Set the wheel radius in meters

    def wheel_speed_callback(self, msg):
        lb_speed = msg.lb_speed
        rb_speed = msg.rb_speed
        # Calculate the average wheel speed in m/s
        self.avg_speed = ((lb_speed + rb_speed) / 2.0) * 2 * math.pi * self.wheel_radius

        self.publish_speed()

    def publish_speed(self):
        msg = Float64()
        msg.data = self.avg_speed
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = AvgWheelSpeedNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
