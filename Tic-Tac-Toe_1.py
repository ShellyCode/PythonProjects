
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
            print board[i][0],'WON-!'
            return True
        if board[0][i]==board[1][i]==board[2][i]!=" ":
            print board[0][i],'WON |!'
            return True
    if board[0][0]==board[1][1]==board[2][2]!=" "or \
       board[0][2]==board[1][1]==board[2][0]!=" ":
            print board[1][1],'WON!\\'
            return True
    if n==8:
        print "------Draw!---------"
        return True
    return False

def run():
    
    done=False
    Player=[' ','X','O']
    Turn=1
    num=0
    
    MapTips=[["1","2","3"],["4","5","6"],["7","8","9"]]
    newboard=[[" " for i in range(3)]for i in range(3)]
    print "New Game!!"
    print "Please select the position by typing in a number between 1 and 9"
    print "Tips:"
    print_board(MapTips)
    
    
    while not done:
        
        print "Your board:"       
        print_board(newboard)
        Move=False
        
        while Move!=True:
            print "Player",Player[Turn],
                   
            try:
                pos=input("Your choice: ")
                if pos<=9 and pos>=0:
                    x=(pos-1)/3 
                    y=(pos-1)%3
                if newboard[x][y]==" ":
                    newboard[x][y]=Player[Turn]
                    Turn=-Turn
                    Move=True
                    num+=1
                done=check_done(newboard,num)
               
               
            except:
                print "You need to add a numeric value (1-9)"
                
        
             
                 
             

##MapTips=[[" "," "," "],[" "," "," "],[" "," "," "]]
#newboard=[[" "]*3]*3        
        
##print_board(MapTips)
##check_done(MapTips)
##        
run()
                
    
