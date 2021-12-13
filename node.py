from vector import *



class Node():
    def __init__(self, x, y):
        self.mPos = Vector2(x, y)

    def neighbors(self, node, all_nodes):
        """
        finds the neighbors that can be gone to from the given node
        :param node: node to be looked at
        :return: the avaliable nodes
        """
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        avaliable = []
        for dir in dirs:
            neighbor = [node.x + dir[0], node.y + dir[1]]
            if neighbor in all_nodes:
                avaliable.append(neighbor)
        return avaliable