# Multi-Robot Waiting System

This project implements a Markov Decision Process (MDP) based solution for a simulated system of waiter robots. It uses ROS (Robot Operating System) to simulate the behavior of multiple robots waiting on tables in a restaurant.

## Features
- Simulates multiple waiter robots using MDP.
- ROS-based simulation environment.
- Includes configuration for map, RViz, and Stage simulator.

## Prerequisites
- ROS (Melodic/Noetic)
- Python 3.x

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/aditya-kamatt/MultiRobotWaitingSystem.git
2. Copy the package folder to your catkin_ws/src directory.
3. Rename the folder to waiter_robots.

## Build the workspace:
```bash
catkin_make
```
Run the following commands in separate terminals:
```bash
roscore
rosrun stage_ros stageros <path to map world file>
rosrun map_server map_server <path to map yaml file>
rosrun rviz rviz
rosrun waiter_robots node.py
```

## Running the Simulation
Make the `node.py` script executable:
```bash
chmod +x scripts/node.py
```
