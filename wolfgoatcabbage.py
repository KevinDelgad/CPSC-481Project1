from search import *
# YOUR CODE GOES HERE

class WolfGoatCabbage(Problem):
    def __init__(self, inital = ('W', 'G', 'F', 'C'), goal = ()):
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
        return returnAction

    def rightBankActions(self, state, validActions):
        tempRightBank = []
        returnActions = validActions
        returnReturnActions= []
        for elems in state:
            pointerval = 0
            while pointerval != len(returnActions):
                if(elems.lower() in returnActions[pointerval]):
                    returnActions.remove(returnActions[pointerval])                    
                    continue
                pointerval += 1

        for action in returnActions:
            for char in action:
                if(char not in tempRightBank):
                    tempRightBank.append(char)

        testingRightBank = list(tempRightBank)

        for action in returnActions:
            for char in action:
                testingRightBank.remove(char)
            if (not all(x in testingRightBank for x in ["w", "g"])):
                if(not all(a in testingRightBank for a in ["g", "c"])):
                    returnReturnActions.append(action)
            testingRightBank = list(tempRightBank)


        return returnReturnActions


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
    print(wgc.goal_test(()))
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
