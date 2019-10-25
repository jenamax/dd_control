# Differential drive control Gazebo simulation

## Structure
- config: folder yaml file for platform control
- launch: folder with 3 launch files
   - display.launch - dispaly model in rviz
   - robot.launch - run model in gazebo with control by steering_control node
   - control.launch - example of robot control by python script (include robot.launch file and start control script)
- rviz: folder with rviz config file
- scripts: folder with Python example script for robot rontrol
- urdf: foledr with urdf file with robot structure defenition

## Runnintg:
- build package in catkin workspace
- run launch file robot.launch to start gazebo simulation and input as argument path to catkin workspace where package was built (roslaunch dd_control robot.launch catkin:=/path/to/ws)
- controller subscribed on topic /dd_controller/cmd_vel; when twist published on this topic platform start move
- controller publish odometry (position, orientation and twist) data to topic /dd_controller/odom
- to run the example of ocntrol by Python script launch control.launch file and input as argument path to catkin workspace where package was built (roslaunch dd_control control.launch catkin:=/path/to/ws)
- if you want to control robot by your own script just run robot.launch and make your script publish twist to /dd_controller/cmd_vel
