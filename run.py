from game import Game

if __name__ == "__main__":
    game = Game(grid_size=3)
    print("Player1 name: ")
    game.player1_name = input()
    print("Player2 name: ")
    game.player2_name = input()
    while game.winner == None:
        game.print()
        if game.turn == 'x':
            print("Player " + str(game.player1_name) + "'s turn: ")
        else:
            print("Player " + str(game.player2_name) + "'s turn: ")
        print("row [Y direction]: ")
        x_input = input().strip()
        if x_input == "":
            continue
        x = int(x_input)-1
        print("column [X direction]: ")
        y_input = input().strip()
        if y_input == "":
            continue
        y = int(y_input)-1
        move_result = game.play([x,y])
        game.total_moves_made += 1
        if move_result['status'] == 'fail':
            print("Invalid move: " + move_result['message'])
            continue
        game_result = game.gameStatus(game.turn)
        if game_result['status'] == 'won':
            game.winner = game.turn
            if game.turn == 'o':
                game.print()
                print("Player " + str(game.player1_name) + " won the game!")        
                break
            else:
                game.print()
                print("Player " + str(game.player2_name) + " won the game!")
                break
        if game.total_moves_made == game.total_allowed_moves:
            game.print()
            print("game ended without any result")
            break