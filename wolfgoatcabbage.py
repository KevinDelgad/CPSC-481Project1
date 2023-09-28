from search import *
# YOUR CODE GOES HERE

class WolfGoatCabbage(Problem):
    def __init__(self, inital = ('F', 'W', 'G', 'C'), goal = ()):
        super().__init__(inital, goal)

    def leftBankActions(self, state, validActions):
        initialActions = []
        returnAction = []
        tempState = list(state)
        for elems in state:
            if(elems == "F"):
                initialActions.append("F")
                continue
            initialActions.append("F" + elems)

        for action in initialActions:
            for char in action:
                tempState.remove(char)

            if (not all(x in tempState for x in ["W", "G"])):
                if(not all(a in tempState for a in ["G", "C"])):
                    returnAction.append(action)
            tempState = list(state)

        print("State", state)
        print("Returned Actions", returnAction)
        return returnAction

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
        curState = list(state)
        for elems in action:
            if(elems.islower()):
                curState.append(elems.upper())
            elif(elems.isupper()):
                curState.remove(elems)
        return tuple(curState)
    
    def actions(self, state):
        ## Uppercase values indicate entities are on the left bank
        ## Lowercase values indicate entities are on the right bank
        validActions = ["F", "FW", "FG", "FC", "f", "fw", "fg", "fc"]
        bankSide = [4, 8, True]

        if("F" not in state):
            bankSide = [0, 4, False]

        del validActions[bankSide[0]:bankSide[1]]


        if(bankSide[2] == False):
            return self.rightBankActions(state, validActions)
            
        return self.leftBankActions(state, validActions)
        




 
if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
