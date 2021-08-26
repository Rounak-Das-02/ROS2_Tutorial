import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Publisher(Node):
    def __init__(self):
        super().__init__("stupid_publisher")
        self.publisher = self.create_publisher(String, "stupidTopic", 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        msg = String()
        msg.data = "HELLO "+ str(self.count)
        self.count+=1
        self.publisher.publish(msg)
        self.get_logger().info("Publishing : " + msg.data)
    
rclpy.init(args = None)
pub = Publisher()
rclpy.spin(pub)

pub.destroy_node()
rclpy.shutdown()


