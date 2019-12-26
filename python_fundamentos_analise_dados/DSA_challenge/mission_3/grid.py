from Node import Node

adjacent_squares = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]

def a_star(maze, start, end):
    """ Returns a list of tuples as a path from the given start to the given end in the given maze """

    if not maze:
        return None

    if len(maze[0]) == 0:
        return None
    
    # Create start and end node
    start_node = Node(None, start)
    end_node = Node(None, end)
    
    # Initialize both open and closed list
    open_list = [start_node]
    closed_list = []
    
    # Loop until you find the end
    while len(open_list) > 0:
        # Get the current node
        current_index = 0
        current_node = open_list[current_index]
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
        
        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)
        
        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path
        
        # Generate children
        children = []
        for new_position in adjacent_squares:
            
            # Get node position
            node_position = (current_node.position[0] + new_position[0]
                             , current_node.position[1] + new_position[1])
            
            # Make sure within range
            if node_position[0] > (len(maze) - 1) \
            or node_position[0] < 0 \
            or node_position[1] > (len(maze[-1]) - 1) \
            or node_position[1] < 0:
                continue
            
            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] == 0:
                continue
            
            # Create new node
            new_node = Node(current_node, node_position)
            
            # Append
            children.append(new_node)
        
        # Loop through children
        for child in children:
            
            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue
            
            # Create the f, g, and g values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) \
                    + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h
            
            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue
            
            # Add the child to the open list
            open_list.append(child)

class Grid(object):

    def find_path(self, matrix):
        if not matrix:
            return None
        
        # Get end coordinates
        x = len(matrix) - 1
        y = len(matrix[-1]) - 1
        
        return a_star(matrix, [0, 0], [x, y])