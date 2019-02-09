# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


#####################################################
#####################################################
# Please enter the number of hours you spent on this
# assignment here
num_hours_i_spent_on_this_assignment = 30
#####################################################
#####################################################

#####################################################
#####################################################
# Give one short piece of feedback about the course so far. What
# have you found most interesting? Is there a topic that you had trouble
# understanding? Are there any changes that could improve the value of the
# course to you? (We will anonymize these before reading them.)
"""
<Your feedback goes here>

- It would have helped to be given a walk-through of the codebase
- I found it easier to do bfs first, then dfs afterwards.
- It's cool to know the logic behind how some games are designed


"""
#####################################################
#####################################################



"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import heapq

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]

def update(self, item, priority):
        # If item already in priority queue with higher priority, update its priority and rebuild the heap.
        # If item already in priority queue with equal or lower priority, do nothing.
        # If item not in priority queue, do the same thing as self.push.
        for index, (p, c, i) in enumerate(self.heap):
            if i[0] == item[0]:
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)


def depthFirstSearch(problem):
    """
    Questoin 1.1
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print ( problem.getStartState() )
    print (problem.isGoalState(problem.getStartState()) )
    print ( problem.getSuccessors(problem.getStartState()) )

    """
    "*** YOUR CODE HERE ***"
    #print ( problem.getStartState() )
    #print (problem.isGoalState(problem.getStartState()) )
    #boolean
    #print ( problem.getSuccessors(problem.getStartState()) )
    #array to loop through
    #python3 pacman.py -p SearchAgent -a fn=depthFirstSearch

    # array to loop through
    # python3 pacman.py -p SearchAgent -a fn=depthFirstSearch

    F = util.Stack()
    startState = problem.getStartState()
    path = []
    F.push( (startState, path) )
    visitedNodes = list()
    visitedNodes.append(startState)

#exact same as bfs

    while F.isEmpty() == 0:
        prev = F.pop()
        prevSt = prev[0]
        prevAct = prev[1]
        for i in problem.getSuccessors(prevSt):
            curSt = i[0]
            curAct = i[1]

            if curSt not in visitedNodes:
                if problem.isGoalState(curSt) == 1:
                    path = prevAct + [curAct]
                    print(path)
                    return path
                else:
                    F.push((curSt, prevAct + [curAct]))
                    visitedNodes.append(curSt)




def breadthFirstSearch(problem):
    """Questoin 1.2
     Search the shallowest nodes in the search tree first.
     """
    "*** YOUR CODE HERE ***"

    """python3 pacman.py -l mediumMaze -p SearchAgent -a fn=bfs"""

    #get init state
    F = util.Queue()
    startState = problem.getStartState()
    path = []
    visitedNodes = list()
    F.push((startState, path))

    #check if init state is goal, return sol'n
    while F.isEmpty() == 0:
        prev = F.pop()
        st = prev[0]
        act = prev[1]
        for i in problem.getSuccessors(st):
            curSt = i[0]
            curAct = i[1]
            if curSt not in visitedNodes:
                if problem.isGoalState(curSt) == 1:
                    path = act+[curAct]
                    print(path)
                    return path
                path = act + [curAct]
                F.push((curSt, path))
                visitedNodes.append(curSt)


    #loop do
        #if q is empty then return failure
        #pop Q
        #set node to visited
        #for each successor of node
            #get child
            #if child not explored or Q, then
                #if child is goal state then return solution
                #insert child onto Q



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Question 1.3
    Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    # get init state
    F = util.PriorityQueue()
    startCost = heuristic(problem.getStartState(), problem)
    startState = problem.getStartState()
    path = []
    exploredNodes = list()
    F.push((startState, path), startCost)
    exploredNodes.append(startState)

    # use uniform cost search algorhtm

    while F.isEmpty() == 0:
        prev = F.pop()
        st = prev[0]
        act = prev[1]

        if problem.isGoalState(st):
            path = act
            print(path)
            return path
        else:
            exploredNodes.append(st)

        for i in problem.getSuccessors(st):
            curSt = i[0]
            curAct = i[1]
            if curSt not in exploredNodes:
                path = act + [curAct]
                curCost = problem.getCostOfActions(path) + heuristic(curSt, problem)
                F.update((curSt, path), curCost)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
