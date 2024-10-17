import rclpy   #ros2 python接口库
from rclpy.node import Node  #ros 节点类

import time

def main(args=None):
    rclpy.init(args=args)                    # ros接口初始化
    node = Node("ros_demo_hello")            # 创建ros节点对象且初始化
                                                                
    while rclpy.ok():                        # 判断ros系统是否正常运行   
        node.get_logger().info("傻狗")       # ros日志输出
        time.sleep(0.5)                        

    node.destroy_node()                     # 销毁节点对象
    rclpy.shutdown()                        # 关闭ros python接口
