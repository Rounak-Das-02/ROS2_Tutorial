import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class Subscriber(Node):
    def __init__(self):
        super().__init__("stupid_subscriber")
        self.subscriber = self.create_subscription(String, "stupidTopic", self.listener_callback, 10)

    def listener_callback(self, msg):
        self.get_logger().info("I Heard : " + str(msg.data))

rclpy.init()
sub = Subscriber()
rclpy.spin(sub)
sub.destroy_node()
rclpy.shutdown()

