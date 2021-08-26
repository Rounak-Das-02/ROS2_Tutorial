import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter
from rclpy.exceptions import ParameterNotDeclaredException
from interfaces.msg import Yomsg
# from interfaces.srv import MultiplyTwoFloats
from rcl_interfaces.msg import ParameterDescriptor

class parameter(Node):
    def __init__(self):
        super().__init__("param_node" , allow_undeclared_parameters=True, automatically_declare_parameters_from_overrides=True)
        period = 2 #seconds
        self.timer = self.create_timer(period, self.callback)
        # self.req = MultiplyTwoFloats.Request()
        self.req = Yomsg()
        self.req.a = 20.0
        self.req.b = 10.0
        my_parameter_descriptor = ParameterDescriptor(description='This parameter is mine!')
        # self.declare_parameter("parameter",
        #     [self.req.a, self.req.b], 
        #     my_parameter_descriptor)

        self.declare_parameter("parameter",
            [self.req.a, self.req.b],
            my_parameter_descriptor)
        
        self.publisher_ = self.create_publisher(Yomsg, 'topic', 10)

    def callback(self):
        param = self.get_parameter("parameter").get_parameter_value()._double_array_value
        # print(param[0])
        self.get_logger().info("Hello %s" %param)
        
        new_param = Parameter(
            'parameter',
            rclpy.Parameter.Type.DOUBLE_ARRAY,
            [param[0], param[1]]
        )
        self.req.a = param[0]
        self.req.b = param[1]

        all_new_parameter = [new_param]
        self.set_parameters(all_new_parameter)
        self.publisher_.publish(self.req)

def main():
    rclpy.init()
    P = parameter()
    rclpy.spin(P)

if __name__ == "__main__":
    main()


