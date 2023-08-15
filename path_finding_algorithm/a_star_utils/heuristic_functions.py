'''
this file contains all the heuristic functions used in a star algorithm
created by :kush jayank pandya
last updated : 14 Aug 2023
'''
import numpy as np
import matplotlib.pyplot as plt

def heuristic_func(heuristic_grid,current_point,end_point):
    '''
    This function calculates the heuristic value for a given point in the maze.
    Heuristic value is calculated as the manhattan distance between the current 
    point and the end point.

    Parameters
    ----------
    heuristic_grid : numpy array
        Heuristic matrix of size (n+2 x n+2), where first and last rows and columns will be 
        padded with zeros i.e. boundry of the maze.
    current_point : tuple
        Current point in the maze.
    end_point : tuple
        End point in the maze.  

    Returns
    -------
    None.

    '''

    end_point_i, end_point_j = end_point
    current_point_i, current_point_j = current_point
    heuristic_grid[current_point_i, current_point_j] = ( abs( end_point_i - current_point_i ) +
                                                         abs( end_point_j - current_point_j ))


def heuristic_maze(size_of_matrix,end_point):
    '''
    This function creates a heuristic matrix of size (n+2 x n+2), where first and last rows and 
    columns will be padded with zeros i.e. boundry of the maze.

    Parameters  
    ----------
    size_of_matrix : int
        Size of the maze.
    end_point : tuple
        End point in the maze.

    Returns
    -------
    heuristic_maze : numpy array
        Heuristic matrix of size (n+2 x n+2), where first and last rows and columns will
        be padded with zeros i.e. boundry of the maze.

    '''


    heuristic_grid = np.full((size_of_matrix+2, size_of_matrix+2),np.inf)
    y_temp = [y_point for y_point in range(1,size_of_matrix + 1 )]
    x_temp = [x_point for x_point in range(1,size_of_matrix + 1)]


    for x_point in x_temp:
        for y_point in y_temp:
            heuristic_grid(heuristic_grid,(x_point,y_point),end_point)

    return heuristic_grid


def visulize_heuristic(heuristic_grid):
    '''
    This function visulizes the heuristic matrix.

    Parameters
    ----------
    heuristic_grid : numpy array
        Heuristic matrix of size (n+2 x n+2), where first and last rows and columns will be 
        padded with zeros i.e. boundry of the maze.

    Returns
    -------
    None.

    '''

    plt.imshow(heuristic_grid, cmap='jet', interpolation='none')
    plt.show()
