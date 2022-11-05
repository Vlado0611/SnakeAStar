
class Node:

    def __init__(self, state, position, parent=None, action=None, cost=0):
        self.state = state   # state je tijelo zmije - lista
        self.position = position  # pozicija glave zmije
        self.parent = parent
        self.action = action
        self.cost = cost

    def expand(self, game):
        actions = game.actions(self.state, self.position)  # uzimamo sve moguce akcije iz trenutnog stanja
        
        child_nodes = []

        for action in actions:
            pseudo_state = self.state.copy()
            pseudo_position = self.position.copy()
            successor_state, new_pos = game.result(pseudo_state, pseudo_position, action)
            cost = self.cost + 1 + game.ManhattanDistance(new_pos)  # f + h = g, f = 1, h je manhattan distanca
            child_nodes.append(Node(successor_state, new_pos, self, action, cost))  # dodajemo cvor u child_nodes
        
        return child_nodes

    def stuck(self, game):
        if len(game.actions(self.state, self.position)) == 0:
            return True
        
        return False
    
    def __lt__(self, node):
        return self.cost < node.cost
