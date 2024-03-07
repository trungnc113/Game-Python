from ast import List, Tuple
import heapq
import math
from os import path
import threading
from typing import Callable
from setting import *

class  node:
	
	def __init__(self , parent ,position):
		self.parent = parent
		self.position = position

		self.g = 0
		self.h = 0
		self.f = 0
	def __lt__(self, other):
		return self.f < other.f
def heuristics(a, b):
		return math.sqrt((a.position[0] - b.position[0])**2 + abs(a.position[1] - b.position[1])**2)

def a_star(maze,start, end):			
        start_node = node(None, start)
        end_node = node(None, end)
        open_list = []
        closed_list = set()
	
        heapq.heappush(open_list, (0, start_node))
        
        while open_list:
            _, current_node = heapq.heappop(open_list)
            
            if current_node.position == end_node.position:
                path = []
                while current_node.parent is not None:
                    path.append(current_node.position)
                    current_node = current_node.parent
                path.reverse()
                return path

            closed_list.add(current_node.position)

            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
                
                if node_position[0] < 0 or node_position[0] >= len(maze) or node_position[1] < 0 or node_position[1] >= len(maze[0]):
                    continue

                if maze[node_position[0]][node_position[1]] == '1':
                    continue
                
                if node_position in closed_list:
                    continue
                
                new_node = node(current_node, node_position)
                
                if (new_node.g, new_node) in open_list:
                    continue
                
                new_node.h = heuristics(new_node, end_node)
                new_node.f = new_node.g + new_node.h
                heapq.heappush(open_list, (new_node.f, new_node))