from search import *
# YOUR CODE GOES HERE

class WolfGoatCabbage(Problem):
    def __init__(self, inital = {'F', 'W', 'G', 'C'}, goal = {}):
        super().__init__(inital, goal)

    def goal_test(self, state):
        return state == self.goal

    def result(self, state, action):
        pass

    def actions(self, state):
        pass

 
if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    print(wgc.goal_test({}))

    """
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
    """