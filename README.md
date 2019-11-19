# Move Servo with Sensor via Ros

Please note: there is a delay between publishing and the servo moving.
Kind of a major delay.

# Dependencies
1. rpi sensors:https://github.com/altosz/rpisensors
3. and its dependencies: https://github.com/bivab/smbus-cffi/blob/master/README.rst
2. servo_control: https://github.com/NoelleTemple/servo_control

Use
```
sudo pip install -e .
```
inside the folder with the setup.py file to properly install python packages

If you get a locked error
```
cd /var/lib/dpkg/
sudo rm lock
sudo rm lock-frontend
```

# Pinouts
Raspberry Pi Pinout:

![Raspberry Pi Pinout](https://github.com/NoelleTemple/roscore_move/blob/master/Resources/Raspberry-Pi-GPIO-Layout-Model-B-Plus-rotated.png)


The servo I use: Tower Pro Micro Servo 9g SG90
* Note that this servo takes duty cycle inputs between 2 and 13 with a frequency of 50 Hz.  

![Servo Motor Pinout](https://github.com/NoelleTemple/roscore_move/blob/master/Resources/Servo-Motor-Wires.png)

Pinout:
* Vin -> pin 2
* Ground -> pin 39
* Control -> pin 33

Sensor used: VL6180X

![Sensor Pinout](https://github.com/NoelleTemple/roscore_move/blob/master/Resources/Sensor%20Pinout.jpg)

Pinout:
* Vin -> pin 1
* Ground -> pin 9
* SDA -> pin 3
* SCL -> pin 5

# Setup Roscore

```
sudo apt install ros-desktop-full ros-desktop-full-dev
sudo apt install build-essential dpkg-dev git 
sudo apt install libopencv-dev liborocos-kdl-dev libompl-dev
```

```
mkdir ~/ros-underlay
cd ~/ros-underlay
rosinstall_generator ros_comm --rosdistro kinetic --exclude RPP --exclude-path /usr/share --deps --wet-only > kinetic_debian_ros_comm.rosinstall
wstool init -j8 src kinetic_debian_ros_comm.rosinstall
cd ~/ros-underlay
catkin_make
```

If having issues, check to see if roscore is already available:
```
roscore
```
If this works, you should get an output like this:
```
SUMMARY
========

PARAMETERS
 * /rosdistro: melodic
 * /rosversion: 1.14.3

NODES

auto-starting new master
process[master]: started with pid [29233]
ROS_MASTER_URI=http://ubuntu:11311/
```

No need to install ros if you already have it.

# Create Workspace

```
cd ~/
source ros-underlay/devel/setup.bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws
catkin_make
```

# Create Package

```
cd ~/catkin_ws/src
catkin_create_pkg move std_msgs rospy 
cd move/src
```

# Create Subscriber and Listener
``` 
cd ~/
git clone https://github.com/NoelleTemple/roscore_move.git
cd roscore_move
cp talker.py ~/catkin_ws/src/move/src/
cp listener.py ~/catkin_ws/src/move/src/
cd ~/catkin_ws/src/move/src/
chmod +x listener.py
chmod +x talker.py
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```
Where "move" is the name of the package.

# Running the Scripts
Each of these commands will need to be run in 3 different windows:
```
roscore
```

```
rosrun move listener.py
```

```
rosrun move talker.py
```

Where "move" is the name of the package.

The servo has a delay, but will move based on the distance an object is from the sensor.  

