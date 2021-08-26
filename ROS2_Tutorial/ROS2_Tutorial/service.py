from interfaces.srv import MultiplyTwoFloats

import rclpy
from rclpy.node import Node

class Service(Node):

    def __init__(self):
        super().__init__("stupidService")
        self.srv = self.create_service(MultiplyTwoFloats, "multiply", self.multiply_callback)

    def multiply_callback(self, request, response):
        response.product = request.a * request.b
        self.get_logger().info("Incoming request : " + str(request.a) + " " + str(request.b))
        return response

rclpy.init()
serve = Service()
rclpy.spin(serve)
rclpy.shutdown()
