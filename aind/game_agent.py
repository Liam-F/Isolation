#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Udacity: Finish all TODO items in this file to complete the isolation project,
then test your agent's strength against a set of known agents using
tournament.py and include the results in your report.

@author: ucaiado
Created on 07/29/2017
"""

import random


'''
Begin help functions
'''


class SearchTimeout(Exception):
    ''' Subclass base exception for code clarity. '''
    pass


def custom_score(game, player):
    ''' Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    '''
    # TODO: finish this function!
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    f_in_center = (center_score(game, player) == 0) * 10.
    return float(own_moves - 3. * opp_moves + f_in_center)


def custom_score_2(game, player):
    ''' Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    '''
    # TODO: finish this function!
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float(own_moves - 2 * opp_moves)


def custom_score_3(game, player):
    ''' Calculate the heuristic value of a game state from the point of view
    of the given player. Reward the agent by the number of open moves and give
    and aditional reward by selecting the center of the board

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    '''
    # TODO: finish this function!
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    f_in_center = (center_score(game, player) == 0) * 10.
    f_my_moves = open_move_score(game, player)

    return f_my_moves + f_in_center


def null_score(game, player):
    """This heuristic presumes no knowledge for non-terminal states, and
    returns the same uninformative value for all other states.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : hashable
        One of the objects registered by the game object as a valid player.
        (i.e., `player` should be either game.__player_1__ or
        game.__player_2__).

    Returns
    ----------
    float
        The heuristic value of the current game state.
    """

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    return 0.


def open_move_score(game, player):
    """The basic evaluation function described in lecture that outputs a score
    equal to the number of moves open for your computer player on the board.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : hashable
        One of the objects registered by the game object as a valid player.
        (i.e., `player` should be either game.__player_1__ or
        game.__player_2__).

    Returns
    ----------
    float
        The heuristic value of the current game state
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    return float(len(game.get_legal_moves(player)))


def improved_score(game, player):
    """The "Improved" evaluation function discussed in lecture that outputs a
    score equal to the difference in the number of moves available to the
    two players.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : hashable
        One of the objects registered by the game object as a valid player.
        (i.e., `player` should be either game.__player_1__ or
        game.__player_2__).

    Returns
    ----------
    float
        The heuristic value of the current game state
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float(own_moves - opp_moves)


def center_score(game, player):
    """Outputs a score equal to square of the distance from the center of the
    board to the position of the player.

    This heuristic is only used by the autograder for testing.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : hashable
        One of the objects registered by the game object as a valid player.
        (i.e., `player` should be either game.__player_1__ or
        game.__player_2__).

    Returns
    ----------
    float
        The heuristic value of the current game state
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    w, h = game.width / 2., game.height / 2.
    y, x = game.get_player_location(player)
    return float((h - y)**2 + (w - x)**2)

'''
End help functions
'''


class IsolationPlayer:
    ''' Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    '''
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=15.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    ''' Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    '''

    def get_move(self, game, time_left):
        ''' Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        '''
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        try:
            best_move = (game.get_legal_moves(game.active_player))[0]
        except IndexError:
            best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def minimax(self, game, depth):
        ''' Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        '''
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # The functions MAX-VALUE and MIN-VALUE go through the whole game tree,
        # all the way to the leaves, to determine the backed-up value of state
        # so, we just need to call one of the functions
        best_score = float('-inf')
        l_legal_moves = game.get_legal_moves(game.active_player)
        try:
            best_move = l_legal_moves[0]
        except IndexError:
            return (-1, -1)
        for idx, m in enumerate(l_legal_moves):
            v = self.min_value(game.forecast_move(m), depth)
            if v > best_score:
                best_score = v
                best_move = m
        return best_move

    def score(self, game, player):
        '''
        Calculate the heuristic value of a game state from the point of player
        '''
        return custom_score_3(game, player)

    def terminal_test(self, game, depth):
        '''
        Return True if the game is over for the active player
        and False otherwise.
        '''
        # check if there is still time left
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        # control the depth.
        if depth < 2:
            # Depth one means terminal state
            # print('depth: ', depth)
            return True
        # check if there are still legal moves by Assumption 1
        return not bool(game.get_legal_moves(game.active_player))

    def min_value(self, game, depth):
        '''
        Return the value for a win (+1) if the game is over,
        otherwise return the minimum value over all legal child
        nodes.
        '''
        # check if there is still time left
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        # check
        if self.terminal_test(game, depth):
            # return 1
            return self.score(game, self)  # by Assumption 2
        v = float('inf')
        for m in game.get_legal_moves(game.active_player):
            # implement the proposed function in AIMA, pg 166:
            # \nu \leftarrow MAX(\nu, MIN-VALUE(RESULT(s, a)))
            # also, decrieses he current depth
            v = min(v, self.max_value(game.forecast_move(m), depth - 1))
        return v

    def max_value(self, game, depth):
        '''
        Return the value for a loss (-1) if the game is over,
        otherwise return the maximum value over all legal child
        nodes.
        '''
        # check if there is still time left
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        # check if the game is terminated. Pass the current depth to test
        if self.terminal_test(game, depth):
            # return -1
            return self.score(game, self)  # by assumption 2
        v = float('-inf')
        for m in game.get_legal_moves(game.active_player):
            # implement the proposed function in AIMA, pg 166:
            # \nu \leftarrow MIN(\nu, MAX-VALUE(RESULT(s, a)))
            # also, decrieses he current depth
            v = max(v, self.min_value(game.forecast_move(m), depth - 1))
        return v


class AlphaBetaPlayer(IsolationPlayer):
    ''' Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    '''

    def get_move(self, game, time_left):
        ''' Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        '''
        self.time_left = time_left

        # TODO: finish this function!
        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        try:
            best_move = (game.get_legal_moves(game.active_player))[0]
        except IndexError:
            best_move = (-1, -1)
        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            # implement interative-deepening describeb in AIMA, pg. 89
            # in order to control the loop, I choose the first depth to be 1
            # for depth = 0 to \inf do
            for depth in range(1, 10**6):
                # result \leftarrow DEPTH-LIMITED-SEARCH(problem, depth)
                best_move = self.alphabeta(game, depth)
                # It is implement in various part of the code
        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed
        # Return the best move from the last completed search iteration
        # if result != curoff then return result
        return best_move

    def alphabeta(self, game, depth, alpha=float('-inf'), beta=float('inf')):
        ''' Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        '''
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # TODO: finish this function!
        best_score = float('-inf')
        l_legal_moves = game.get_legal_moves(game.active_player)
        try:
            best_move = l_legal_moves[0]
        except IndexError:
            return (-1, -1)
        for idx, m in enumerate(game.get_legal_moves(game.active_player)):
            v = self.min_value(game.forecast_move(m), alpha, beta, depth-1)
            if v > best_score:
                alpha = v
                best_score = v
                best_move = m
        return best_move

    def score(self, game, player):
        '''
        Calculate the heuristic value of a game state from the point of player
        '''
        return custom_score_3(game, player)

    def cutoff_test(self, game, depth):
        '''
        Return True if the game is over for the active player
        and False otherwise. Also perform the Cutoff-test described in
        AIMA, ps 173
        '''
        # check if there is still time left
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        # control the depth.
        if depth < 1:
            # Depth one means terminal state
            # print('depth: ', depth)
            return True
        # check if there are still legal moves by Assumption 1
        return not bool(game.get_legal_moves(game.active_player))

    def min_value(self, game, alpha, beta, depth):
        '''
        Return the value for a win (+1) if the game is over,
        otherwise return the minimum value over all legal child
        nodes.

        implement the proposed function in AIMA, pg 170
        '''
        # check if there is still time left
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        # if TERMINAL-TEST(state) then return UTILITY(state)
        if self.cutoff_test(game, depth):
            return self.score(game, self)
        v = float('inf')
        # for each a in ACTIONS(state) do
        for m in game.get_legal_moves(game.active_player):
            # \nu \leftarrow MIN(\nu, MAX-VALUE(RESULT(s, a), \alpha, \beta))
            v = min(v, self.max_value(game.forecast_move(m), alpha, beta,
                                      depth - 1))
            # if \nu \leq \alpha then return v
            if v <= alpha:
                return v
            # \beta \leftarrow MIN(\beta, v)
            beta = min(beta, v)
        return v

    def max_value(self, game, alpha, beta, depth):
        '''
        Return the value for a loss (-1) if the game is over,
        otherwise return the maximum value over all legal child
        nodes.

        implement the proposed function in AIMA, pg 170
        '''
        # check if there is still time left
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        # if TERMINAL-TEST(state) then return UTILITY(state)
        if self.cutoff_test(game, depth):
            return self.score(game, self)
        v = float('-inf')
        # for each a in ACTIONS(state) do
        for m in game.get_legal_moves(game.active_player):
            # \nu \leftarrow MIN(\nu, MAX-VALUE(RESULT(s, a)))
            v = max(v, self.min_value(game.forecast_move(m), alpha, beta,
                                      depth - 1))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v
