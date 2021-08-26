from setuptools import setup

package_name = 'ROS2_Tutorial'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Rounak',
    maintainer_email='raks@todo.todo',
    description='ROS2 Tutorial in Ubuntu 20.04',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = ROS2_Tutorial.publisher_member_function',
            'listener = ROS2_Tutorial.subscriber_member_function',
            'service = ROS2_Tutorial.service',
            'client = ROS2_Tutorial.client:main',
            'param = ROS2_Tutorial.parameter:main',
            'action_server = ROS2_Tutorial.action_server:main',
            'action_client = ROS2_Tutorial.action_client:main'
        ],
    },
)
