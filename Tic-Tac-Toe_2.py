
def print_board(board):
    for j,line in enumerate(board):
        for i,p in enumerate(line):
            print p,
            if i!=2:
                print '|',
        
        print ''
        if j!=2:
            print '---------'
    print '' 

                
def check_done(board,n):
   
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]!=" ":
            #print board[i][0],'WON-!'
            return True,board[i][0]
        if board[0][i]==board[1][i]==board[2][i]!=" ":
            #print board[0][i],'WON |!'
            return True,board[0][i]
    if board[0][0]==board[1][1]==board[2][2]!=" "or \
       board[0][2]==board[1][1]==board[2][0]!=" ":
            #print board[1][1],'WON!\\'
            return True,board[1][1]
    if n==9:
        #print "------Draw!---------"
        return True,'Draw!'
    return False,None

def choosePlayer():
    
    while True:
        x=raw_input('play X or O? (Note: X moves first) ')
        if x in ['X','x']:
            return 'X'
        elif x in ['O','o']:
            return 'O'
        
def userMove(board,pattern):
    print "Current board:"       
    print_board(board)
    while True:
        print "Player",pattern,
        try:
            pos=input("Your choice(1-9): ")
            if pos<=9 and pos>=0:
                x=(pos-1)/3
                y=(pos-1)%3
            if board[x][y]==" ":
                board[x][y]=pattern
                break
        except:
            print "You need to add a numeric value (1-9)"

def corner_move(board,pattern):
    
    for i in [0,2]:
        for j in [0,2]:
            if board[i][j]==" ":
                board[i][j]=pattern
                return True
    return False

def center_move(board,pattern):
    import random
    if random.choice([0,1]) and board[1][1]==' ':
        board[1][1]=pattern
        return True
    return False
def winOrBlock_move(board,pattern1,pattern2):
    for i in range(3):
        for j in range(3):
            if board[i][j]==" ":
                board[i][j]=pattern1
                done,result=check_done(board,0)
                if done:
                    return True
                board[i][j]=pattern2
                done,result=check_done(board,0)
                if done:
                    board[i][j]=pattern1
                    return True
                board[i][j]=" "
    return False

def random_move(board,pattern):
    import random
    edge=[(0,1),(1,0),(1,2),(2,1)]
    while True:
        i,j=random.choice(edge)
        if board[i][j]==" ":
            board[i][j]=pattern
            break
    
def computerMove(board,pattern1,pattern2):
    if not winOrBlock_move(board,pattern1,pattern2):
        if not center_move(board,pattern1):
            if not corner_move(board,pattern1):
                random_move(board,pattern1)
   
def game():
    
    done=False
    Player=[' ','X','O']
    Turn=1
    num=0
    result=None
    
    
    MapTips=[["1","2","3"],["4","5","6"],["7","8","9"]]
    newboard=[[" " for i in range(3)]for i in range(3)]
    print "New Game!!"
    print "Please select the position by typing in a number between 1 and 9"
    print "Tips:"
    print_board(MapTips)

    New=set([1,2,3,4,5,6,7,8,9])

    User=choosePlayer()
    while not done:
    
        if Player[Turn]==User:
            
            userMove(newboard,User)                             
            
        else:
            move=computerMove(newboard,Player[Turn],User)
                        
        Turn=-Turn
        num+=1
        done,result=check_done(newboard,num)
    
    print '---------------------------'         
    if result==User:       
        print "Congratuation!!! ", result,' WON!'
        
    elif result=='Draw!':
        print result
    else:
        print "Game Over! ", result,' WON!'
    print '---------------------------'       
    print "Final board:"
    print_board(newboard)
    print '---------------------------'               
                  
            
                
        
def run():
    Again=True
    valid=False
    while Again:
        game()
        while not valid:
            x=raw_input("Try again? Y/N: ")
            if x in['y','Y','N','n']:
               if x in['N','n']:
                    Again=False
               valid=True
        

if __name__=='__main__':
    run()
                
    
