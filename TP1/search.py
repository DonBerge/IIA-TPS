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


# A type hint for a generic search list
GeneralSearchList = Any


def generalSearch(
    problem: SearchProblem,
    ListConstructor: Callable[[Any], GeneralSearchList],
    ListEmpty: Callable[[GeneralSearchList], bool],
    ListTake: Callable[[GeneralSearchList], Any],
    ListExpand: Callable[[GeneralSearchList, Any], GeneralSearchList]
):
    # Construct the list with the start state
    # The list will contain tuples of the form (state, parent, direction)
    # where state is the current state, parent is the state from which
    # the current state was reached and direction is the direction taken
    # to reach the current state
    l = ListConstructor((problem.getStartState(), None, None))

    # Store the visited node with its predecesor and the direction
    # taken, this is used to reconstruct
    # execution path
    visited = dict()

    while not ListEmpty(l):
        # Take an element from the list
        state, parent, dirp = ListTake(l)

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
        l = ListExpand(l, state)

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
    def create(x: Any):
        c = util.Stack()
        c.push(x)
        return c

    def take(x):
        return x.pop()

    def empty(x):
        return x.isEmpty()

    def expand(stack, state):
        for successor, direction, _ in problem.getSuccessors(state):
            stack.push((successor, state, direction))
        return stack
    return generalSearch(problem, create, empty, take, expand)


def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    def create(x) -> util.Queue:
        c = util.Queue()
        c.push(x)
        return c

    def take(x: util.Queue):
        return x.pop()

    def empty(x: util.Queue):
        return x.isEmpty()

    def expand(queue: util.Queue, state):
        for successor, direction, _ in problem.getSuccessors(state):
            queue.push((successor, state, direction))
        return queue
    return generalSearch(problem, create, empty, take, expand)


def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    #def create(x) -> util.PriorityQueue:
    #    c = util.PriorityQueue()
    #    c.push(x, problem.getCostOfActions([x[2]]))
    #    return c
    
    start = problem.getStartState()
    stack = util.PriorityQueue()
    stack.push((start, []), 0)
    visited = set()
    while not stack.isEmpty():
        state, directions = stack.pop()
        if state in visited:
            continue
        visited.add(state)
        if problem.isGoalState(state):
            # Retry to find the rest of the pills
            return directions
        for successor, direction, _ in problem.getSuccessors(state):
            ndirs = directions + [direction]
            cost = problem.getCostOfActions(ndirs)
            stack.push((successor, ndirs), cost)
    return []


def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(
        problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    start = problem.getStartState()
    stack = util.PriorityQueue()
    stack.push((start, []), 0)
    visited = set()
    while not stack.isEmpty():
        state, directions = stack.pop()
        if state in visited:
            continue
        visited.add(state)
        if problem.isGoalState(state):
            # Retry to find the rest of the pills
            return directions
        for successor, direction, _ in problem.getSuccessors(state):
            ndirs = directions + [direction]
            cost = problem.getCostOfActions(
                ndirs) + heuristic(successor, problem)
            stack.push((successor, ndirs), cost)
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
