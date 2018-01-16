
# coding: utf-8

# In[1]:


#import display
from IPython.display import clear_output

# global/static variables
board = [' '] * 10
game_state = True
announce = ''


# In[2]:


'''
allow players to start a new game 
discard zero index so player may use 3 x 3 grid of number pad as game board
'''
def reset_board():
    global board,game_state
    board = [' '] * 10
    game_state = True


# In[3]:


#just using functions, create game board
def display_board():
    #to ensure starting afresh with each new game
    clear_output()
    #display the game board
    print "  "+board[7]+" || "+board[8]+" || "+board[9]+" "
    print "=============="
    print "  "+board[4]+" || "+board[5]+" || "+board[6]+" "
    print "=============="
    print "  "+board[1]+" || "+board[2]+" || "+board[3]+" "


# In[4]:


def win_check(board, player):
    ''' Check for 3 in succession on Horizontal, Vertical, and Diagonal cells  '''
    if (board[7]  ==  board[8] ==  board[9] == player) or         (board[4] ==  board[5] ==  board[6] == player) or         (board[1] ==  board[2] ==  board[3] == player) or         (board[7] ==  board[4] ==  board[1] == player) or         (board[8] ==  board[5] ==  board[2] == player) or         (board[9] ==  board[6] ==  board[3] == player) or         (board[1] ==  board[5] ==  board[9] == player) or         (board[3] ==  board[5] ==  board[7] == player):
        return True
    else:
        return False


# In[5]:


def full_board_check(board):
    #check for any remaining blanks 
    if " " in board[1:]:
        #reminder - zero remains empty in this case
        return False
    else:
        return True


# In[6]:


def ask_player(mark):
    ''' Asks player where to place X or O mark, checks validity '''
    global board
    req = 'Choose where to place your: ' + mark
    while True:
        try:
            choice = int(raw_input(req))
        except ValueError:
            print("Sorry, please input a number between 1-9.")
            continue

        if choice not in range(1,10):
            print("Sorry, please input a number between 1-9.")
            continue

        if board[choice] == " ":
            board[choice] = mark
            break
        else:
            print "That space isn't available!"
            continue


# In[7]:


def player_choice(mark):
    global board,game_state,announce
    #Set game - blank game announcement
    announce = ''
    #Get Player Input/Mark
    mark = str(mark)
    # Validate input
    ask_player(mark)
    
    #Check for winning mark/player
    if win_check(board,mark):
        clear_output()
        display_board()
        announce = mark +" wins! Congratulations!"
        game_state = False
        
    #Show the board
    clear_output()
    display_board()

    #Check for a tie 
    if full_board_check(board):
        announce = "Tie!"
        game_state = False
        
    return game_state,announce


# In[ ]:


def play_game():
    reset_board()
    global announce
    
    # Establish marks
    X='X'
    O='O'
    while True:
        # Show the board
        clear_output()
        display_board()
        
        # Player X turn
        game_state,announce = player_choice(X)
        print announce
        if game_state == False:
            break
            
        # Player O turn
        game_state,announce = player_choice(O)
        print announce
        if game_state == False:
            break
            
    # Ask player for a rematch
    rematch = raw_input('Would you like to play again? y/n')
    if rematch == 'y':
        play_game()
    else:
        print "Thanks for playing!"


# In[ ]:


play_game()

