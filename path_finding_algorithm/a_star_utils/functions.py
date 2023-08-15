'''
This file contains all the functions used in the A* algorithm
created by : Kush Jayank Pandya
last updated on : 14 Aug 2023
'''

import matplotlib.pyplot as plt

class AStarUtils:
    '''
    This class contains all the functions used in the A* algorithm
    '''

    def get_neighbours(self,agent_maze,current_point,closelist):
        '''
        This function returns the neighbours of the current point in the maze.

        Parameters
        ----------
        agent_maze : numpy array
            Matrix of ones with size (n+2 x n+2), where first and last rows and columns will be
            padded with zeros i.e. boundry of the maze.
        current_point : tuple
            Current point in the maze.
        closelist : list
            List of points that are already visited.

        Returns
        -------
        real_neighbours : list
            List of neighbours of the current point in the maze.
        '''
        current_point_i,current_point_j = current_point
        potential_neighbours = [(current_point_i + 1,current_point_j),
                                (current_point_i - 1,current_point_j),
                                (current_point_i,current_point_j + 1),
                                (current_point_i,current_point_j - 1)]
        real_neighbours = []

        for neighbour in potential_neighbours:

            if agent_maze[neighbour] != 0 and neighbour not in closelist:
                real_neighbours.append(neighbour)

        return real_neighbours


    def step_plot(self,agent_maze,g_value,start_point,current_point,came_from):
        '''
        This function plots the maze with the path found by the A* algorithm for each step.

        Parameters
        ----------
        agent_maze : numpy array
            Matrix of ones with size (n+2 x n+2), where first and last rows and columns will be
            padded with zeros i.e. boundry of the maze.
        G : numpy array
            Matrix of ones with size (n+2 x n+2), where first and last rows and columns will be
            padded with zeros i.e. boundry of the maze.
        start_point : tuple
            Start point in the maze.
        current_point : tuple
            Current point in the maze.
        came_from : dict
            Dictionary containing the path from the start point to the current point.

        Returns
        -------
        None.
        '''

        temp_agent_maze = agent_maze.copy()
        point = current_point

        while point != start_point:
            point = came_from[point]
            temp_agent_maze[point] = 5

        temp_agent_maze[current_point] = 5

        plt.figure(figsize = (20,20))
        fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(30,10))
        fig.suptitle('A* path',fontsize= 30, fontweight='bold')
        ax1.imshow(temp_agent_maze, cmap='jet', interpolation='none')
        ax2.imshow(g_value, cmap='jet', interpolation='none')
        ax1.set_title('Agent Maze(Knowledge about the real maze as per agent)',
                      fontsize= 15, fontweight='bold')
        ax2.set_title('Expanded cells by A* algorithm',fontsize= 15, fontweight='bold')
        plt.show()
