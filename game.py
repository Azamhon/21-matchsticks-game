def main():
    print('Hello user and welcome to the 21 matchsticks game! \nThe objective of the game is to take matchsticks from a pile of 21. \nEach turn player must take at least 1 and at most 3 matchsicks \nEach player competes with one anoher and the one to take the final match wins.')
    playmode = input('First tell me if you want to play a \'bot\' or another \'player\': ')
    global sticks
    sticks = 21
    if playmode != 'player' and playmode != 'bot':
        print('inproper input! Lets start all over again.')
        return main()
    elif playmode == 'player':
        turn = 'player1'
        
        while True:
            player_turn(turn)
            
            if sticks <=0 :
                break

            if turn == 'player1':
                turn = 'player2'
            else:
                turn = 'player1'
    elif playmode == 'bot':
        turn = 'bot'
        while True:
            if turn == 'player':
                player_turn(turn)
            else:
                bot_turn()

            if sticks <=0 :
                break

            if turn == 'player':
                turn = 'bot'
            else:
                turn = 'player'
    print(turn, 'Won')


def player_turn(turn):
    global sticks
    print('It is turn for', turn, 'to take matches.')
    print(f'there are {sticks} matchsticks left: ', '|'*sticks)
    
    try:
        curr_input = int(input('Give me a number of stick between 1 and 3 you want to take: '))
        if curr_input < 3 or curr_input > 1:
            sticks -= curr_input
            print('='*20)
    except:
        print('invalid input, try again please!')
        player_turn(turn)

def bot_turn():
    global sticks
    print(f'there are {sticks} matchsticks left: ', '|'*sticks)
    print('bot took ', sticks%4, 'matchsticks.')
    sticks -= sticks%4

main()