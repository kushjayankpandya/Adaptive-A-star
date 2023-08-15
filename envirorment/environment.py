'''
created by : Kush Jayank Pandya
last updated on : 14 Aug 2023
'''

#importing libraries
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

class Environments:
    '''
    This class contains functions to create multiple environments.
    '''

    def __init__(self,size_of_matrix,no_of_environments):
        '''
        Parameters
        ----------
        size_of_matrix : int
            Size of the maze.
        no_of_environments : int
            Number of environments to be created.
        '''

        self.size_of_matrix = size_of_matrix
        self.no_of_environments = no_of_environments
        self.last_environment = None


    def create_grid(self):
        '''
        Create a matrix of ones with size (n+2 x n+2),
        where first and last rows and columns will be padded with zeros i.e. boundry of the maze.

        Parameters
        ----------
        size_of_matrix : int
            Size of the maze.

        Returns
        -------
        environment : numpy array
            Matrix of ones with size (n+2 x n+2), where first and last rows and columns will 
            be padded
        '''

        environment = np.ones((self.size_of_matrix, self.size_of_matrix))
        environment = np.pad(environment, [(1, 1), (1, 1)], mode='constant')

        return environment


    def create_single_environment(self,environment,i,j):
        '''
        Creation of environment using dfs i.e. maze with 30% of probability marked as blocked and 
        70% of probability marked as unblocked starting from random starting point.

        Parameters
        ----------
        Environment : numpy array
            Matrix of ones with size (n+2 x n+2), where first and last rows and columns will be 
            padded with zeros i.e. boundry of the maze.
        i : int
            Starting point of dfs.
        j : int
            Starting point of dfs.
        size_of_matrix : int
            Size of the maze.

        Returns
        -------
        Environment : numpy array
            Matrix of ones with size (n+2 x n+2), where first and last rows and columns will be 
            padded with zeros i.e. boundry of the maze.
        '''

        first_iter = True
        environment[(i,j)] = 2
        stack = [(i,j)]
        visited = set()

        # DFS to create the maze
        while stack:

            # Pop a cell from the stack and make it a current cell
            vertex = stack.pop()
            if vertex in visited:
                continue

            # Mark the current cell as visited
            a,b = vertex
            if first_iter is False:
                environment[a,b] =  int(np.random.choice([0, 2], size=(1,1), p=[0.3, 0.7]))
            else:
                first_iter = False

            # Add the cell to the stack of visited cells
            visited.add(vertex)
            children = [ (a+1,b) ,(a-1,b) ,(a,b-1) ,(a,b+1) ]
            np.random.shuffle(children)
            children = [(x,y) for (x,y) in children if x > 0 and y> 0 and
                                                    x < self.size_of_matrix + 1 and
                                                    y < self.size_of_matrix + 1]

            # Push the children of the current cell to the stack
            for (a,b) in children:
                stack.append((a,b))

        return environment

    def create_start_end_points(self,environment):
        '''
        Creation of start and end points of the maze.

        Parameters
        ----------
        Environment : numpy array
            Matrix of ones with size (n+2 x n+2), where first and last rows and columns will be 
            padded with zeros i.e. boundry of the maze.
        size_of_matrix : int
            Size of the maze.

        Returns
        -------
        Environment : numpy array
            Matrix of ones with size (n+2 x n+2), where first and last rows and columns will be 
            padded with zeros i.e. boundry of the maze.
        start_point : tuple 
            Starting point of the maze.
        end_point : tuple
            Ending point of the maze.
        '''

        # Creating start points
        i,j = 0,0  #always blocked cell
        while environment[i,j] == 0:
            (i,j) = (random.randint(a = 1, b = self.size_of_matrix),
                    random.randint(a = 1, b = self.size_of_matrix))
        environment[i,j] = 3
        start_point = (i,j)

        # Creating end points
        i,j = 0,0  #always blocked cell
        while environment[i,j] == 0:
            (i,j) = (random.randint(a = 1, b = self.size_of_matrix),
                    random.randint(a = 1, b = self.size_of_matrix))
        environment[i,j] = 4
        end_point = (i,j)

        # setting down right most point of cell as 6 for color scheme
        environment[ self.size_of_matrix +  1, self.size_of_matrix + 1] = 6


        return (environment,start_point,end_point)


    def create_multiple_environments(self):
        '''
        Creation of multiple environments.
        
        Parameters
        ----------
        no_of_environments : int
            Number of environments to be created.
        size_of_matrix : int
            Size of the maze.

        Returns
        -------
        Environment_set : list
            List of environments.
        '''

        environment_set = []

        # Creating multiple environments
        for _ in range(self.no_of_environments):

            # Creating grid
            array = self.create_grid()

            # Creating environment
            (i,j) = (random.randint(a = 1, b = self.size_of_matrix),
                    random.randint(a = 1, b = self.size_of_matrix))
            environment = self.create_single_environment(array,i,j)

            # Creating start and end points
            environment_plus = self.create_start_end_points(environment)

            # Appending to the list
            environment_set.append(environment_plus)

        # getting the last enviorment for visualization purpose
        self.last_environment = environment_set[-1]

        return environment_set

    def visulize_random_enviroment(self):
        '''
        Visulization of the last environment created.

        Parameters
        ----------
        self.last_environment : numpy array
            Matrix of ones with size (n+2 x n+2), where first and last rows and columns will be
            padded with zeros i.e. boundry of the maze.

        Returns
        -------
        None.
        '''

        plt.figure(figsize = (10,10))
        plt.title('Maze')

        # add legend
        plt.legend(handles=[mpatches.Patch(color='blue', label='Blocked'),
                            mpatches.Patch(color='cyan', label='Unblocked'),
                            mpatches.Patch(color='yellow', label='Start point'),
                            mpatches.Patch(color='green', label='End point')],
                            bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.
                           )

        # plot the maze
        plt.imshow(self.last_environment[0], cmap='jet', interpolation='none') # type: ignore
