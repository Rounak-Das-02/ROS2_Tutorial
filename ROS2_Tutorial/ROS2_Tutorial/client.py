from interfaces.srv import MultiplyTwoFloats
import rclpy
from rclpy.node import Node

class Client(Node):
	def __init__(self):
		super().__init__("stupidClient")
		self.client = self.create_client(MultiplyTwoFloats, "multiply")
		while not self.client.wait_for_service(timeout_sec=2.0):
			self.get_logger().info("Service not available, waiting again")
		self.req = MultiplyTwoFloats.Request()
		
	def send_request(self):
		self.req.a = float(input("Enter one Float Value : "))
		self.req.b = float(input("Enter second value : "))
		self.future = self.client.call_async(self.req)


def main():
	rclpy.init()
	client = Client()
	client.send_request()

	while rclpy.ok():
		rclpy.spin_once(client)
		if client.future.done():
			try:
				response = client.future.result()
			except Exception as e:
				client.get_logger().info('Service call failed %r' % (e,))
			else:
				client.get_logger().info("Result of %f * %f is %f" %(client.req.a , client.req.b , response.product))
			break


	client.destroy_node()
	rclpy.shutdown()

if __name__ == " __main__":
	main()