import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from interfaces.action import Fibonacci

class FibonacciActionClient(Node):
    def __init__(self):
        super().__init__("fibonacci_action_client")
        self.actionClient = ActionClient(self, Fibonacci, "fibonacci")

    def send_goal(self, order):
        goal_msg = Fibonacci.Goal()
        goal_msg.order = order
        self.actionClient.wait_for_server()
        self._send_goal_future = self.actionClient.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)
        self._send_goal_future.add_done_callback(self.goal_response_callback)
    
    def goal_response_callback(self, future):
        goal_handle = future.result()

        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')

        self._get_result_future = goal_handle.get_result_async()

        self._get_result_future.add_done_callback(self.get_result_callback)


    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Result: {0}'.format(result.sequence))
        rclpy.shutdown()

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info('Received feedback: {0}'.format(feedback.partial_sequence))


    
def main():
    rclpy.init()
    fib = FibonacciActionClient()
    fib.send_goal(10)
    rclpy.spin(fib)

if __name__ == "__main__":
    main()
