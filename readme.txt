각 패널에 필요한 것(최소 2개의 패널이 필요합니다.)
1. source ~/catkin_ws/devel/setup.bash

gazebo를 실행시킬 터미널에서만 실행하면 될 것
2. source ~/catkin_ws/src/drone_practice/launch/setup_env.sh
3. roslaunch drone_practice practice.launch

gmapping 기반으로 slam 생성
4. roslaunch drone_2d_lidar gmapping.launch

rviz에서 확인할 때 add -> topic -> map을 선택하면 slam으로 생성되는 map을 topic 기반으로 볼 수 있습니다.

추가사항
---------------------2026/06/06----------------------------
1. source ~/catkin_ws/devel/setup.bash
2. source ~/catkin_ws/src/drone_practice/launch/setup_env.sh
3. roslaunch drone_practice master.launch
후에 drone_practice/launch의 master.launch를 실행하는 것으로 여러 launch 파일을 동시에 실행할 수 있습니다.
추후에 launch 파일이 추가되면 해당 파일의 코드를 참고하여 추가해주시면 되겠습니다.
