from search import *
# YOUR CODE GOES HERE

class WolfGoatCabbage(Problem):
    def __init__(self, inital = {'F', 'W', 'G', 'C'}, goal = {}):
        super().__init__(inital, goal)

    def leftBankActions(self, state, validActions):
        returnActions = validActions
        for elems in state:
            pointerval = 0
            if(elems == "F"):
                continue
            while pointerval != len(returnActions):
                if(elems not in returnActions[pointerval] and len(returnActions[pointerval]) != 1):
                    returnActions.remove(returnActions[pointerval])
                    continue
                pointerval += 1

        return returnActions

    def rightBankActions(self, state, validActions):
        returnActions = validActions
        for elems in state:
            pointerval = 0
            while pointerval != len(returnActions):
                if(elems.lower() in returnActions[pointerval]):
                    returnActions.remove(returnActions[pointerval])
                    continue
                pointerval += 1

        return returnActions


    def goal_test(self, state):
        return state == self.goal

    def result(self, state, action):
        pass

    def actions(self, state):
        ## Uppercase values indicate entities are on the left bank
        ## Lowercase values indicate entities are on the right bank
        validActions = ["F", "FW", "FG", "FC", "f", "fw", "fg", "fc"]
        bankSide = [4, 8, True]

        if("F" not in state):
            bankSide = [0, 4, False]

        del validActions[bankSide[0]:bankSide[1]]

        print(bankSide[2])

        if(bankSide[2] == False):
            return self.rightBankActions(state, validActions)
            
        return self.leftBankActions(state, validActions)
        




 
if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    print(wgc.actions("C"))

    """
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
    """