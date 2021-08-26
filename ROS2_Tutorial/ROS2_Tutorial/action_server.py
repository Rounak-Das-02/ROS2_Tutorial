import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
import time

from interfaces.action import Fibonacci

class FibonacciActionServer(Node):
    def __init__(self):
        super().__init__("fibonacci_action_server")
        self.actionServer = ActionServer(
            self, 
            Fibonacci,
            'fibonacci',
            self.callback
        )
    
    def callback(self, goal_handle):
        self.get_logger().info("Executing Goal ... ")
        sequence = [0, 1]
        feedback_msg = Fibonacci.Feedback()
        feedback_msg.partial_sequence = [0, 1]

        for i in range(1, goal_handle.request.order):
            feedback_msg.partial_sequence.append(
                feedback_msg.partial_sequence[i] + feedback_msg.partial_sequence[i-1])
            self.get_logger().info('Feedback: {0}'.format(feedback_msg.partial_sequence))
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1)

        goal_handle.succeed()
        result = Fibonacci.Result()
        result.sequence = feedback_msg.partial_sequence
        return result

def main():
    rclpy.init()
    fib = FibonacciActionServer()
    rclpy.spin(fib)

if __name__ == "__main__":
    main()