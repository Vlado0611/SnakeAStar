import math

class Snake:

    def __init__(self, position, body, food_pos):
        self.position = position
        self.body = body
        self.food_pos = food_pos

    def goal_test(self, position):
        if position[0] == self.food_pos[0] and position[1] == self.food_pos[1]:
            return True
        else:
            return False 

    def actions(self, state, position):
        possible_actions = ["UP", "DOWN", "LEFT", "RIGHT"]

        for pos in state:
            if (position[0] - 10 == pos[0] and position[1] == pos[1]) or position[0] - 10 <= 0:
                if possible_actions.count("LEFT") > 0:
                    possible_actions.remove("LEFT")
            if (position[0] + 10 == pos[0] and position[1] == pos[1]) or position[0] + 10 >= 720:
                if possible_actions.count("RIGHT") > 0:
                    possible_actions.remove("RIGHT")
            if (position[1] - 10 == pos[1] and position[0] == pos[0]) or position[1] - 10 <= 0:
                if possible_actions.count("UP") > 0:
                    possible_actions.remove("UP")
            if (position[1] + 10 == pos[1] and position[0] == pos[0])or position[1] + 10 >= 480:
                if possible_actions.count("DOWN") > 0:
                    possible_actions.remove("DOWN")
        
        return possible_actions

    def result(self, state, curr_pos, action):

        if action == "UP":
            curr_pos[1] -= 10
        if action == "DOWN":
            curr_pos[1] += 10
        if action == "LEFT":
            curr_pos[0] -= 10
        if action == "RIGHT":
            curr_pos[0] += 10

        state.insert(0,list(curr_pos))

        if curr_pos[0] == self.food_pos[0] and curr_pos[1] == self.food_pos[1]:
            pass
        else:
            state.pop() 

        return [state, curr_pos]

    def ManhattanDistance(self, position):
        return abs(position[0] - self.food_pos[0]) + abs(position[1] - self.food_pos[1])
        #return math.sqrt((position[0] - self.food_pos[0])**2 + (position[1] - self.food_pos[1])**2)
    


