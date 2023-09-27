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
         ## Uppercase action indicates chosen character moves from left to right bank
        ## Lowercase action indicates chosen character moves from right to left bank
        print("Before: ", state)
        print("Action: ", action)
        for elems in action[0]:
            if(elems.lower()):
                state.add(elems.upper())
            if(elems.upper()):
                state.discard(elems)
        return state
    
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
    test_state = {'F', 'W', 'C'}
    test_action = ['FW']
    test_state2 = {'W' , 'C'}
    test_action2 = ['f']
    #test 1
    print(wgc.actions(test_state))
    print("After", wgc.result(test_state, test_action))
    #test 2
    print(wgc.actions(test_state2))
    print("After", wgc.result(test_state2, test_action2))

    """
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
    """