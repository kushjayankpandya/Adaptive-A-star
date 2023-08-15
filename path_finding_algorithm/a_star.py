'''
A star algorithm with different g value priority 
created by : Kush Jayank Pandya
last updated on : 14 Aug 2023
'''
from heapq import heappush, heappop
from a_star_utils.functions import AStarUtils
from a_star_utils.heuristic_functions import HeuristicFunctions



class A_star:
    
    def __init__(self):
        pass


    def a_star(agent_maze,start_point,end_point,H,G,F,G_closed_list):

        came_from = {}
        openlist = []
        closelist = []

        path_found = False
        F[start_point] = H[start_point]
        G[start_point] = 0
        heappush(openlist, (F[start_point],H[start_point], start_point))

        while(openlist):

            _ , _1 , current_point = heappop(openlist)
            F[current_point] = G[current_point] + H[current_point]
            

            if H[current_point] == 0:
                path_found = True
                G_closed_list[end_point] = G[end_point]
                break

            successors = get_neighbours(agent_maze,current_point, closelist)

            for successor_point in successors:


                successor_point_current_cost = G[current_point] + cost


                open_set = [val3 for val1,val2,val3 in openlist]
                if successor_point in open_set:

                    if G[successor_point] <= successor_point_current_cost:
                        continue
                    else:
                        G[successor_point] = successor_point_current_cost
                        index = openlist.index((F[successor_point], H[successor_point],successor_point))
                        F[successor_point] =  G[successor_point] + H[successor_point]
                        openlist[index] = (F[successor_point], H[successor_point], successor_point)
                        heapify(openlist)
                        came_from[successor_point] = current_point

                elif successor_point in closelist:
                    continue

                else:
                    G[successor_point] = successor_point_current_cost
                    F[successor_point] =  G[successor_point] + H[successor_point]
                    heappush(openlist, (F[successor_point], H[successor_point], successor_point))
                    came_from[successor_point] = current_point

            

            closelist.append(current_point)
            G_closed_list[current_point] = G[current_point]


        if path_found == False:
            return False

        else:
            return came_from
