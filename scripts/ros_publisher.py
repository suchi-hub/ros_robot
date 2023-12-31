import rospy
from std_msgs.msg import String

class Publisher:
    def __init__(self):
        rospy.init_node('command_publisher', anonymous=True)
        self.pub = rospy.Publisher('command', String, queue_size=10)
        self.rate = rospy.Rate(1)
        while not rospy.is_shutdown():
            command = f"Time is {rospy.get_time()}"
            # command = input("Enter command: ")
            rospy.loginfo(command)
            self.pub.publish(command)
            self.rate.sleep()

if __name__ == '__main__':
    try:
        Publisher()
    except rospy.ROSInterruptException:
        pass