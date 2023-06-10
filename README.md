# 21-matchsticks-game
 The game consists of 21 matchsticks. 2 players or a player against a bot pick sticks one by one. The one to take the last stick wins. it is a simple version of a NIM-game


In this repository you can find a python code for playing a game in terminal.

There are 2 playmodes: PvP and PvC.

This game is an introduction to Nim game, which uses the same logic for finding best moves bot but is more difficult to understand without good math foundation.

The code consists of several functions:

<h2>Main Function</h2>
This function controls the flow of the game for different playmodes. The current condittion of the game is controled by the global list variable 'board_state' It can be optimised.

```
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
```

<h2>Player turn Function</h2>
This funciton is used to get the proper input from the user/player. it controls whether inputt makes sense in the current condition of the board and uses remove matches function to change it.

```
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
```

<h2>Bot turn function</h2>
Here is a logic for making correct move to get the board to the nim state: by leaving an opponent with 4 matchsticks one can guarantee a win, as whatever opponent chooses, one can take the remaining of matches. to guarante that one can leave an opponent with 4 matches, one needs to make leave 8/12/16/20 matches on the board. 

Bot cannot lose when taking matches second, as computer finds a combination that returns board_state to a nim state(4/8/12/16/20). More on what is nim state in wiki.

```
def bot_turn():
    global board_state
    nim=0
    for i in board_state:
        nim=nim^i
    print_board()
    counter=0
    for i in board_state:
        if (nim^i) < i:
            print("Bot took {} matche(s) from Pile {}".format(board_state[counter]-(nim^i),counter+1))
            removing_matches(board_state,[str(counter+1),str(board_state[counter]-(nim^i))])
            print('='*20)
            
            break
        counter=counter+1  
```