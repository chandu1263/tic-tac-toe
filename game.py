from player import Player

class Game:
    
    def __init__(self, grid_size=3):
        self.grid_size = grid_size
        self.player1 = Player(piece='x', grid_size=self.grid_size)
        self.player2 = Player(piece='o', grid_size=self.grid_size)
        self.grid = [['_' for __ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.turn = 'x'
        self.winner = None
        self.player1_name = ""
        self.player2_name = ""
        self.total_moves_made = 0
        self.total_allowed_moves = self.grid_size * self.grid_size 
        
    def play(self, position):
        if position[0] < 0 or position[0] >= self.grid_size or position[1] < 0 or position[1] >= self.grid_size:
            return {'status':'fail', 'message': 'Not a valid move'}
        if self.grid[position[0]][position[1]] != '_':
            return {'status':'fail', 'message': 'cell already taken'}
        else:
            self.grid[position[0]][position[1]] = self.turn
            if self.turn == 'x':
                self.player1.grid_positions.append(position)
                self.turn = 'o'
            elif self.turn == 'o':
                self.player2.grid_positions.append(position)
                self.turn = 'x'
            return {'status':'success'}
            
    def gameStatus(self, turn):
        if turn == 'x':
            turn = 'o'
        else:
            turn = 'x'
        # each row
        for i in range(self.grid_size):
            wincheck = True
            for j in range(self.grid_size):
                if self.grid[i][j] != turn:
                    wincheck = False
            if wincheck:
                return {'status': 'won'}
        #each column
        for j in range(self.grid_size):
            wincheck = True
            for i in range(self.grid_size):
                if self.grid[i][j] != turn:
                    wincheck = False
            if wincheck:
                return {'status': 'won'}
        # diagonal 1 (negative slope)
        i = 0
        j = 0
        wincheck = True
        while i < self.grid_size and j < self.grid_size:
            if self.grid[i][j] != turn:
                wincheck = False
                break
            i += 1
            j += 1
        if wincheck:
            return {'status': 'won'}
        # diagonal 2 (positive slope)
        i = self.grid_size-1
        j = 0
        while i >= 0 and j < self.grid_size:
            if self.grid[i][j] != turn:
                wincheck = False
                break
            i -= 1
            j += 1
        if wincheck:
            return {'status': 'won'}
        return {'status':'not decided'}
    
    def print(self):
        for row in range(self.grid_size):
            for column in range(self.grid_size):
                print(self.grid[row][column], end=" ")
            print("\n")