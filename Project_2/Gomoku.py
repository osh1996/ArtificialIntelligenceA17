class Gomoku(Game):
    """play gomoku on an h x v board with first player being 'W' and second player
    being 'B'. The list of moves in form of a list (x,y) and board in form of dict
    {(x,y): player where player is either 'W' or 'B' """
    def _init_(self, h=15, v=15, k=5):
        update(self, h=h, v=v, k=k)
        moves = [(x, y) for x in range(1, h+1)
                 for y in range(1,v+1)]
        self.initial = Struct(to_move='W', utility=0, board={}, moves=moves)

    def legalMoves(self, state):
        #legal moves are any square not yet taken
        return state.moves

    def make_move(self, move, state):
        if move not in state.moves:
            return state #Illegal moves does nothing
        board = state.board.copy(); board[move] = state.to_move
        moves = list(state.moves); moves.remove(move)
        return Struct(to_move=if_(state.to_move == 'W', 'B', 'W'),
                      utility+self.compute_utility(board, move, state.to_move),
                      board=board, moves=moves)
    
    def utility(self, state):
        return state.utility

    def terminal_test(self, state):
        #A state is terminal if it is won or there are no empty squares
        return state.utility !=0 or len(state.moves) == 0

 



