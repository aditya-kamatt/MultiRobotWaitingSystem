#!/usr/bin/python3

"""
This is the main entry point for the particle filter exercise node. It
subscribes to laser, map, and odometry and creates an instance of
pf.PFLocaliser() to do the localisation.
"""

import rospy
import random
import numpy as np

from robot import Robot




class WaiterRobotsNode(object):

    def __init__(self):
        # declare attributes
        self.map = []
        self.robots = []
        self.tableLocations = []
        self.activePaths = []

        # path planning mdp model parameters
    
        
        
        
        
        self.initialiseMapAndRobots(2)
        self.printMap()

        print(self.robots)

        # self.orderModel(6)
    
    def printMap(self):
        print("printing map...")
        map = self.map
        for i in range(len(map)-1,-1, -1):
            for j in range(0,len(map[i])):
                print(map[i][j], end = '')
                print('|', end = '')
            print()

        

    def initialiseMapAndRobots(self, numberOfRobot):
        print("initialising map and robots...")
        # initialise n*m map with the tables locations T and the kitchen location K 
        # TODO this map is flipped such that it matches our designs and grid, not sure if that was the best call
        self.map = np.array([ 
                    ['x','x','x','x','x','x','x','x','x','x','x','x'],
                    ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
                    ['x',' ','T',' ',' ',' ','T',' ',' ',' ','T','x'],
                    ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
                    ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
                    ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
                    ['x',' ','T',' ',' ',' ','T',' ',' ',' ',' ','x'],
                    ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
                    ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
                    ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
                    ['x',' ','T',' ',' ',' ',' ',' ',' ','K','K','x'],
                    ['x','x','x','x','x','x','x','x','x','x','x','x'] ])
        self.map = self.map[::-1]
                     
        # set list of starting locations on the map <x,y> -> each robot will be assignned their assignment point at the start of the simulation - filling from the left
        startingLocations = [(4,1),(5,1),(6,1),(7,1) , (10,3),(10,4),(10,5),(10,6),(10,7)]
        
        # list table locations for convinience -> done manually can do automatically using the map
        tableLocations = [(2,1),(2,5),(2,9),(6,5), (6,9), (10,9)]

        # initialise robots with their robot id and their pose (x,y,theta) and their state (), their positional state location <x,y> assignment point <x,y>
        for i in range (0, numberOfRobot):
            robotId = i+1
            pose = startingLocations[i]
            state = 'idle'
            location = startingLocations[i]
            assignmentPoint = tableLocations[i]
            robot =  Robot(robotId, pose, state, location, assignmentPoint)
            self.robots.append(robot)









    # order simulation model #TODO this is probably a different node
    # will need to listen to the frequency model and add them to a queue
    def orderModel (self, numberOfTable):
        # defined demand phases high medium and low
        HIGH = 1 # every factor of 1
        MEDIUM = 2 # every factor of 2
        LOW = 3 # every factor of 3

        while True:

            orderFrequency = random.randint(1,3)
            if orderFrequency == 1:
                orderFrequency = HIGH
            elif orderFrequency == 2:
                orderFrequency = MEDIUM
            elif orderFrequency == 3:
                orderFrequency = LOW
            
            print("switching to demand phade: ", orderFrequency)
            x = 10 # suggested number of orders for each phase
            # randomly change order frequency every x orders with noise
            numberOfOrders = np.random.normal(x, 0.5*x)

            for i in range (0, int(numberOfOrders)):
                # randomly generate order
                table = random.randint(1, numberOfTable)
                order = 'T' + str(table)
                # publish order

                print("Order for table " + str(table) + " is " + str(order))
                #distribution centered around centered around the frequency  
                rospy.sleep(np.random.normal(orderFrequency, 0.5 * orderFrequency))

            
        # send order message to waiter robot system



    def pathPlanning(self, a, b):
        # a = (x,y) b = (x,y)
        # calculate the best path between the two points 
        
        # define states - we can 
        self.states = self.map
        # define actions
        # define rewards
        # define transition model
        # calculate optimal policy
        # return optimal policy
        pass



# main method
if __name__ == '__main__':
    # --- Main Program ---
    rospy.init_node('waiter_robots_node')
    node = WaiterRobotsNode()
    rospy.spin()
    # print("hello world")
  