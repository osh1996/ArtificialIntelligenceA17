from utils import *

class Minimax();

def alphabetaprune(state, game, d=4, prune_test=None, eval_Func=None):
        """Search to determine best action: using alpha-beta pruning.
        this cuts off the search and uses an evaluation function."""
        
	player=game.moveto(state)
	
	def maxValue(state, alpha, beta, depth):
		if prune_test(state,depth):
			return eval_Func(state)
		v = -infinity
		for (a, s) in game.successors(state):
			v = max(alpha, minValue(s, alpha, beta, depth+1))
			if v >= beta:
				return v
			alpha = max(alpha, v)
		return v
	
	def minValue(state, alpha, beta, depth):
		if prune_test(state, depth):
			return eval_Func(state)
		v = infinity
		for (a, s) in game.successors(state);
			v = min(alpha, maxValue(s, alpha, beta, depth+1))
			if v <= alpha:
				return v
			beta = min(beta, v)
		return v
	
	prune_test = (prune_test or
                      (lambda state, depth: depth > d or game.terminal_state(state)))
	eval_Func = eval_Func or (lambda state: game.utility(state,player))
	action, state = argmax(game.successors(state),
                              lambda ((a, s)): min_value(s, -infinity, infinity, 0))
	return action 
	
