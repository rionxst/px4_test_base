#!/usr/bin/env python3
import rospy
import tf
from nav_msgs.msg import Odometry

def odom_callback(msg):
    br = tf.TransformBroadcaster()
    # MAVROS의 Odometry 토픽 데이터를 TF 트리(odom -> base_link)로 변환
    br.sendTransform(
        (msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.position.z),
        (msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w),
        msg.header.stamp, # Gazebo 시뮬레이션 시간 동기화
        "base_link",      # 자식 프레임
        "odom"            # 부모 프레임
    )

if __name__ == '__main__':
    rospy.init_node('odom_tf_broadcaster')
    # 실제 드론의 Odometry 토픽을 구독 (PX4 기본값)
    rospy.Subscriber('/mavros/local_position/odom', Odometry, odom_callback)
    rospy.spin()
