#
#   EXERCICIO PROGRAMA 1 - BUSCAS
#
#   IVO DE ANDRADE DE DEUS
#
#   No USP 8075238
#

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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

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
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    stack = util.Stack()
    stack.push((problem.getStartState(), [problem.getStartState()], []))
    while stack:
            (vertex, path, directions)= stack.pop()
            """
            print "Vertex:", vertex
            print "Is the vertex a goal?", problem.isGoalState(vertex)
            print "Vertex's successors:", problem.getSuccessors(vertex)
            print "Path so far:", path
            print "Directions so far:", directions
            """
            if problem.isGoalState(vertex) ==  True:
                return directions
            for next in problem.getSuccessors(vertex):
                if next[0] not in path:
                    if problem.isGoalState(next) ==  True:
                        break
                    else:
                        stack.push((next[0], path + [next[0]], directions + [next[1]]))

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    visited = set()
    queue.push((problem.getStartState(), []))
    while queue:
            (vertex, directions)= queue.pop()
            if problem.isGoalState(vertex) ==  True:
                return directions
            elif vertex not in visited:
                visited.add(vertex)
                for next in problem.getSuccessors(vertex):
                        queue.push((next[0], directions + [next[1]]))


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    queue = util.PriorityQueue()
    visited = set()
    queue.push((problem.getStartState(), [], 0), 0)
    
    while not queue.isEmpty():
            (vertex, directions, cost) = queue.pop()
            
            if problem.isGoalState(vertex) ==  True:
                return directions
            
            elif vertex not in visited:
                visited.add(vertex)
                for next in problem.getSuccessors(vertex):
                    queue.push((next[0], directions + [next[1]], cost + next[2]), cost + next[2])

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    queue = util.PriorityQueue()
    visited = set()
    queue.push((problem.getStartState(), [], 0), 0)
    
    while not queue.isEmpty():
        (vertex, directions, cost) = queue.pop()
            
        if problem.isGoalState(vertex) ==  True:
            return directions
            
        elif vertex not in visited:
            visited.add(vertex)
            for next in problem.getSuccessors(vertex):
                queue.push((next[0], directions + [next[1]], cost + next[2]), cost + next[2] + heuristic(next[0], problem))
    """
    queue = util.PriorityQueue()
    queue.push((problem.getStartState(), [problem.getStartState()], [], 0), heuristic(problem.getStartState(), problem) + 0)

    while not queue.isEmpty():
        (vertex, path, directions, cost) = queue.pop()
        
        if problem.isGoalState(vertex):
            return directions

        for next in problem.getSuccessors(vertex):
            if next[0] not in path:
                queue.update((next[0], path + [next[0]], directions + [next[1]], cost + next[2]), cost + heuristic(next[0], problem))

    """
def learningRealTimeAStar(problem, heuristic=nullHeuristic):
    """Execute a number of trials of LRTA* and return the best plan found."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

    # MAXTRIALS = ...
    

# Abbreviations 
# *** DO NOT CHANGE THESE ***
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
lrta = learningRealTimeAStar
