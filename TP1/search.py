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
from game import Directions

# For typing
from typing import List, Any
from collections.abc import Callable


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


def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]

#### Implementation of search functions

# Type hint for the state of the search
# A tuple of the form (state, parent, direction, accum)
# where 
#   state is the current state
#   parent is the state from which the current state was reached 
#   direction is the direction taken to reach the current state
#   accum is the accumulated cost of the path
GeneralSearchState = tuple[Any, Any, Directions, int]

# An abstract class that represents a data structure used in the
# general search algorithm
class GeneralSearchList:
    def isEmpty(self) -> bool:
        """
        Returns True if the list is empty
        """
        util.raiseNotDefined()
    
    def pop(self) -> GeneralSearchState:
        """
        Returns the first element of the list
        """
        util.raiseNotDefined()

    def push(self, state: GeneralSearchState) -> None:
        """
        Pushes the state to the list
        """
        util.raiseNotDefined()

# Implementation of the general search algorithm
def generalSearch(
    problem: SearchProblem,
    GeneralList: Callable[[], GeneralSearchList]
):
    # Construct the initial list
    l = GeneralList()

    # Push the initial state to the list
    # The initial state is the start state of the problem
    # There is no parent or direction, so we set them to None
    # The cost is calculated using the problem object
    l.push(
        (problem.getStartState(), None, None, problem.getCostOfActions([]))
    )

    # Store the visited node with its predecesor and the direction
    # taken, this is used to check for already visited nodes
    # and to reconstruct the path once we reach the goal
    visited = dict()

    while not l.isEmpty():
        # Take an element from the list
        state, parent, dirp, accum = l.pop()

        if state in visited:
            # Already visited, skip it
            continue

        # Mark the state as visited
        # and store the parent and direction
        visited[state] = (parent, dirp)

        if problem.isGoalState(state):
            # Reached a goal state
            # Reconstruct the directions
            return reconstructDirections(state, visited)

        # Expand the list with the successors of the current state
        for successor, direction, cost in problem.getSuccessors(state):
            l.push((successor, state, direction, accum + cost))

    # If we reach here, it means we have not found a solution
    return []

# Reconstruct the directions from the start state to the end state
# using the visited dictionary
def reconstructDirections(
    end: Any,
    visited_map: dict[Any, tuple[Any, Directions]]
) -> List[Directions]:
    directions = []

    # Start from the end state and climb up in the
    # visited map until we reach the start state
    parent, direction = visited_map[end]
    while parent != None:
        directions.append(direction)
        parent, direction = visited_map[parent]

    # The directions are in reverse order, so we need to reverse them
    directions.reverse()

    return directions


def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    return generalSearch(problem, util.Stack)


def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    return generalSearch(problem, util.Queue)


def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    # Se asume que el costo de ruta sigue la propiedad asocitativa
    # f: funcion de costo de ruta
    # f(a,...,b,...c) = f(a,...b)+f(b,...c)
    
    def UCSPriorityQueue():
        # Priority queue with the cost as the priority
        # The cost is the 4th element of the tuple
        return util.PriorityQueueWithFunction(lambda x: x[3])
    
    return generalSearch(problem, UCSPriorityQueue)


def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

CHECK_HEURISTIC_CONSISTENCY = True

def aStarSearch(
        problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    
    def fun(x):
        # verificar consistencia
        if CHECK_HEURISTIC_CONSISTENCY and x[1] is not None:
            hnprima = heuristic(x[0], problem)
            hn = heuristic(x[1], problem)
            if not (hn <= 1 + hnprima):
                print("Heuristica no consistente!")
                print("Para los estados, ",x[0], " y ", x[1])
                print(hn, ">", "1 +", hnprima)
                #exit(1)
        return x[3] + heuristic(x[0], problem)
    
    def AStarPriorityQueue():
        # Priority queue with the cost + heuristic as the priority
        # The cost is the 4th element of the tuple
        return util.PriorityQueueWithFunction(
            fun
            #lambda x: x[3] + heuristic(x[0], problem)
        )

    return generalSearch(problem, AStarPriorityQueue)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
