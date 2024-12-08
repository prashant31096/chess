# Importing Module
from tkinter import *
from PIL import Image, ImageTk
from copy import *

# Define Class : Piece
class Piece:

    def __init__(self,name,category,color,sight,coord,value, cid=0):
        self.name = name
        self.category = category
        self.color = color
        self.sight = sight
        self.coord = coord
        self.value = value
        self.cid = cid

# Define Class : Moves
class Moves:
    
    def __init__(self, name):
        self.name = name
        self.category = name[0]
        self.available = []

    def drive(self, coord):

        if self.category == 'r' or self.category == 'R':
            Moves.Rook(self, coord)
        elif self.category == 'b' or self.category == 'B':
            Moves.Bishop(self, coord)
        elif self.category == 'q' or self.category == 'Q':
            Moves.Rook(self, coord)
            Moves.Bishop(self, coord)
            self.available.remove(coord)
        elif self.category == "p":
            Moves.WhitePawn(self, coord)
        elif self.category == "P":
            Moves.BlackPawn(self, coord)
        elif self.category == "K" or self.category == "k":
            Moves.King(self, coord)
        elif self.category == 'N' or self.category == 'n':
            Moves.Knight(self, coord)

    def valid(self, coord, fcoord):
        available = self.available
        if fcoord in available:
            return fcoord
        else:
            return coord

    def Rook(self,coord):
        
        available = self.available
        available.append(coord)
        for [x,y] in [[1,0],[-1,0],[0,1],[0,-1]]:
            if (coord[0] <= 7 and coord[0] >= 0 and coord[1] <= 7 and coord[1] >= 0):
                i = coord[0]
                j = coord[1]
                while (i + x <= 7 and i + x >= 0 and j + y <= 7 and j + y >= 0):
                
                    if state[i+x][j+y]!=0:
                        if self.category.islower() ^ state[i +x][j+y][0].islower():
                            available.append([i +x, j+y])
                        break
                    else:
                        available.append([i + x, j+y])
                    i += x
                    j+=y
        return available

    def Bishop(self,coord):
        
        available = self.available
        available.append(coord)
        for [x,y] in [[1,1],[-1,-1],[1,-1],[-1,1]]:
            if (coord[0] <= 7 and coord[0] >= 0 and coord[1] <= 7 and coord[1] >= 0):
                i = coord[0]
                j = coord[1]
                while (i + x <= 7 and i + x >= 0 and j + y <= 7 and j + y >= 0):
                
                    if state[i+x][j+y]!=0:
                        if self.category.islower() ^ state[i +x][j+y][0].islower():
                            available.append([i +x, j+y])
                        break
                    else:
                        available.append([i + x, j+y])
                    i += x
                    j+=y            
        return available

    def WhitePawn(self, coord):
        
        name = self.name
        available = self.available
        available.append(coord)
        i = coord[0]
        j = coord[1]
        dflag = 0
        startstate = [[6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7]]

        if coord in startstate:
            dflag = 1

        if i >= 1 and state[i - 1][j] == 0:
            available.append([i - 1, j])
            if dflag == 1 and state[i - 2][j] == 0:
                available.append([i - 2, j])
               
        if coord[1]!=0:
            if i >= 1 and state[i - 1][j - 1] != 0 and state[i - 1][j - 1][0].isupper():
                available.append([i - 1, j - 1])
        if coord[1]!=7:
            if i >= 1 and state[i - 1][j + 1] != 0 and state[i - 1][j + 1][0].isupper():
                available.append([i - 1, j + 1])
                     
        global candidates, white_flag
        if white_flag!=0 and name in candidates:
                if coord[1]!=0:
                    if state[i][j - 1] != 0 and state[i][j - 1]==f"P{white_flag}" :
                        available.append([i - 1, j - 1])
                if coord[1]!=7:
                    if state[i ][j + 1] != 0 and state[i ][j + 1]==f"P{white_flag}":
                        available.append([i - 1, j + 1])
                        
        return  available

                        
    def BlackPawn(self, coord):
        
        name = self.name
        available = self.available
        available.append(coord)
        i = coord[0]
        j = coord[1]
        dflag = 0
        startstate = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]]

        if coord in startstate:
            dflag = 1

        if i <= 6 and state[i + 1][j] == 0:
            available.append([i + 1, j])
            if dflag == 1 and state[i + 2][j] == 0:
                available.append([i + 2, j])
                
        if coord[1]!=0:
            if i <= 6 and state[i + 1][j - 1] != 0 and state[i + 1][j - 1][0].islower():
                available.append([i + 1, j - 1])
        if coord[1]!=7:
            if i <= 6 and state[i + 1][j + 1] != 0 and state[i + 1][j + 1][0].islower():
                available.append([i + 1, j + 1])
       
        global candidates, black_flag
        if black_flag!=0 and name in candidates:
                if coord[1]!=0:
                    if state[i][j - 1] != 0 and state[i][j - 1]==f"p{black_flag}" :
                        available.append([i + 1, j - 1])
                if coord[1]!=7:
                    if state[i ][j + 1] != 0 and state[i ][j + 1]==f"p{black_flag}" :
                        available.append([i +1, j + 1])
    
        return  available

                        
    def King(self, coord):
        available = self.available
        available.append(coord)

        i = coord[0]
        j = coord[1]
        for [x, y] in [[0, 1], [1, 1], [-1, 1], [1, 0], [-1, 0], [0, -1], [1, -1], [-1, -1]]:
            if (i + x <= 7 and i + x >= 0 and j + y <= 7 and j + y >= 0):
                if (state[i + x][j + y] != 0):
                    if self.category.islower() ^ state[i + x][j + y][0].islower():
                        available.append([i + x, j + y])
                else:
                    available.append([i + x, j + y])

        if turn == 0:
            if castle[0][0]:
                available.append([7,6])
            if castle[0][1]:
                available.append([7,2])
        else:
            if castle[1][0]:
                available.append([0,6])
            if castle[1][1]:
                available.append([0,2])
                
        return available

    def Knight(self, coord):
        available = self.available
        available.append(coord)
        i = coord[0]
        j = coord[1]
        for [x, y] in [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]:
            if (i + x <= 7 and i + x >= 0 and j + y <= 7 and j + y >= 0):
                if (state[i + x][j + y] != 0):
                    if self.category.islower() ^ state[i + x][j + y][0].islower():
                        available.append([i + x, j + y])
    
                else:
                    available.append([i + x, j + y])
        return  available
            
# Displaying Board State
def display(state,bsize,gap,redc,bar):
    
    for i in range(bsize):
        for j in range(bsize):
            if state[i][j]!=0:
                print(state[i][j], end = " "*(gap-redc*len(state[i][j])))
            else:
                print(0, end = " "*(gap-redc))  
        print()
        print()
    print("#"*bar)
    print()

# Building Board
def build(bsize):
    global canvas,squares
    for i in range(bsize):
        for j in range(bsize):
            if (i+j)%2:
                squares[i][j] = ImageTk.PhotoImage(file = f"C:\\Users\\prashant kumar\\Desktop\\chess\\images\\BS.jpeg")
            else:
                squares[i][j] = ImageTk.PhotoImage(file = f"C:\\Users\\prashant kumar\\Desktop\\chess\\images\\WS.jpeg")
            canvas.create_image(i*scale, j*scale, image=squares[i][j], anchor='nw')

# Deploying Piece Images
def deploy(bsize,state):
    global canvas, pimages,alive
    for i in range(bsize):
        for j in range(bsize):
            if state[i][j]==0:
                continue
            elif state[i][j].isupper():
                pimages[i][j] = ImageTk.PhotoImage(file = f"C:\\Users\\prashant kumar\\Desktop\\chess\\images\\{state[i][j][0]}{state[i][j][0]}.png")
            else:
                pimages[i][j] = ImageTk.PhotoImage(file = f"C:\\Users\\prashant kumar\\Desktop\\chess\\images\\{state[i][j][0]}.png") 
            cid = canvas.create_image(j*scale, i*scale, image=pimages[i][j], anchor='nw', tag='draggable')
            alive[state[i][j]].cid = cid
            
# Creating Random Piece
def create(name,coord):
    
    global value
    category = name[0]
    if category.islower():
        color = 0
    else:
        color = 1

    category = category.upper()
    if category == "B":
        if (coord[0]+coord[1])%2:
            sight = -1
        else:
            sight = 1
    else:
        sight = 0
        
        
    return Piece(name,category,color,sight,coord.copy(),value[category])

# Making Piece Alive
def make(bsize,state):
    live = {}
    for i in range(bsize):
        for j in range(bsize):
            if state[i][j]!=0:
                live[state[i][j]] = create(state[i][j],[i,j])
    return live


# Coord Adjustment

def normalize(coord):
    global scale, bsize
    norm_coord = [(coord[0]//scale)*scale, (coord[1]//scale)*scale]
    return tuple(norm_coord)

def quantize(coord):
    global bsize
    norm_coord = normalize(coord)
    q_coord = int(norm_coord[0]/scale),int(norm_coord[1]/scale)
    return q_coord
    
def norm_shift(coord):
    norm_coord = normalize(coord)
    shift = norm_coord[0]-coord[0], norm_coord[1]-coord[1]
    return shift

def centralize(coord):
    global scale
    coord = coord[0]+scale/2, coord[1]+scale/2
    return coord

def adjust(coord):
    coord = centralize(norm_shift(coord))
    return coord

# Unrestricted Movement
def pick(event):
    global current_coord, dragged_item, old_square
    result = canvas.find_withtag('current')
    print(result)
    if result:
        dragged_item = result[0]
        current_coord = canvas.canvasx(event.x), canvas.canvasy(event.y)
        old_square = quantize(current_coord)
        pickup = adjust(current_coord)
        canvas.move(dragged_item, -pickup[0], -pickup[1])
    else:
        dragged_item = None

def drag(event):
    global current_coord
    user_coord = canvas.canvasx(event.x), canvas.canvasy(event.y)
    shift = user_coord[0] - current_coord[0], user_coord[1] - current_coord[1]
    current_coord = user_coord
    canvas.move(dragged_item, shift[0], shift[1])
        
def release(event):
    global current_coord, dragged_item,old_square
    user_square = quantize(current_coord)
    shift = adjust(current_coord)
    canvas.move(dragged_item, shift[0], shift[1])
    old_square = [old_square[1],old_square[0]]
    user_square = [user_square[1],user_square[0]]
    GameFunction(list(old_square),list(user_square))
    dragged_item = None

# Implementing Rules of Game

def GameFunction(old_square,user_square):
    
    global state, scale, turn, white_flag, black_flag, candidates, new_square, capture_flag

    [old_row,old_col] = old_square
    [user_row,user_col] = user_square

    name = state[old_row][old_col]
    piece = alive[name]
    obj = Moves(name)
    obj.drive(old_square)
    new_square = obj.valid(old_square,user_square)

    if turn!=piece.color:
        new_square = old_square
    elif turn==piece.color:
        if piece.category=="K":
            alive[piece.name].coord=new_square
        
    [new_row,new_col] = new_square
    if new_col == old_col+2 or new_col == old_col-2:
        if piece.name == "k" and (castle[0][0]==1 or castle[0][1]==1):
            new_square = castle_detect(old_row,old_col,new_row,new_col)
        elif piece.name == "K" and (castle[1][0]==1 or castle[1][1]==1):
            new_square = castle_detect(old_row,old_col,new_row,new_col)
        
    [new_row,new_col] = new_square
    new_square = calid(old_row,old_col,new_row,new_col)
    [new_row,new_col] = new_square
    
    shift = (new_col-user_col)*scale, (new_row-user_row)*scale
    canvas.move(dragged_item, shift[0], shift[1])
        
    capture_flag = 0
    if state[new_row][new_col]!=0 and old_square!=new_square:
        capture_flag = 1
        cid = alive[state[new_row][new_col]].cid
        canvas.delete(cid)
        alive.pop(state[new_row][new_col])
        if state[new_row][new_col] ==  "r2":
            castle[0][0] = 0
        elif state[new_row][new_col] ==  "r1":
            castle[0][1] = 0
        elif state[new_row][new_col] ==  "R1":
            castle[1][0] = 0
        elif state[new_row][new_col] ==  "R2":
            castle[1][1] = 0
        
    if piece.category == "P" and new_square!=old_square:
        enp_capture(old_row,old_col,new_col,obj)
        enp_det(old_row,old_col,new_row,new_col,obj)
            
    state[new_row][new_col] = state[old_row][old_col]
    if new_square!=old_square:
        state[old_row][old_col] = 0
    piece.coord = [new_row,new_col]

    if piece.name[0]=='p' and new_row==0:
        wpromotion()
    elif piece.name[0]=='P' and new_row==7:
        bpromotion()

    if turn!= -1:
        if new_square!=old_square:
            flag_reset(piece)
        terminate(piece)
        
    global bsize,gap,redc,bar
    display(state,bsize,gap,redc,bar)
        
    return None

def flag_reset(piece):
    global turn, white_flag, black_flag, check_flag, castle,n_moves, capture_flag, fmrule, freq
    
    if turn==0 and piece.color==0:
        n_moves+=1
        turn=1
        white_flag = 0
        fmrule +=1
        check_flag = -1
        if piece.name == "k":
            castle[0] = [0,0]
        elif piece.name == "r2":
            castle[0][0] = 0
        elif piece.name == "r1":
            castle[0][1] = 0
        if capture_flag==1 or piece.category == "P":
            fmrule = 0
        dumstate = deepcopy(state)
        dumstate = tuple(map(tuple,dumstate))
        if freq.get(dumstate):
            freq[dumstate] +=1
        else:
            freq[dumstate] = 1
        
    elif turn==1 and piece.color==1:
        n_moves+=1
        turn=0
        black_flag = 0
        check_flag = -1
        fmrule +=1
        if piece.name == "K":
            castle[1]=[0,0]
        elif piece.name == "R2":
            castle[1][0] = 0
        elif piece.name == "R1":
            castle[1][1] = 0
        if capture_flag==1 or piece.category == "P":
            fmrule = 0
        dumstate = deepcopy(state)
        dumstate = tuple(map(tuple,dumstate))
        if freq.get(dumstate):
            freq[dumstate] +=1
        else:
            freq[dumstate] = 1
            
def terminate(piece): 
    global turn,state, freq
    
    if fmrule==100:
        turn=-1
        print("# Draw By Fifty Move Rule")
        
    dumstate = deepcopy(state)
    dumstate = tuple(map(tuple,dumstate))
    if freq.get(dumstate) and freq[dumstate]==3:
        turn = -1
        print("# Draw By Three Fold Repitition")

    if turn==0:
        checkmate(alive["k"].coord)
        stalemate(alive["k"].coord)
        
    elif turn==1:
        checkmate(alive["K"].coord)
        stalemate(alive["K"].coord)

    insuff_mater()

def enp_det(oldrow,oldcol,newrow,newcol,obj):
    global candidates,white_flag,black_flag
    
    candidates = []
    if obj.category =="P" and newrow==oldrow+2:
        
        if oldcol!=0:
            if state[newrow][newcol-1]!=0 and state[newrow][newcol-1][0]=="p":
                white_flag = oldcol+1
                candidates.append(f"p{white_flag-1}")
        if oldcol!=7:
            if state[newrow][newcol+1]!=0 and state[newrow][newcol+1][0]=="p":
                white_flag = oldcol+1
                candidates.append(f"p{white_flag+1}")
            
    elif obj.category =="p" and newrow==oldrow-2:
        if oldcol!=0:
            if state[newrow][newcol-1]!=0 and state[newrow][newcol-1][0]=="P":
                black_flag = oldcol+1
                candidates.append(f"P{black_flag-1}")
        if oldcol!=7:
            if state[newrow][newcol+1]!=0 and state[newrow][newcol+1][0]=="P":
                black_flag = oldcol+1
                candidates.append(f"P{black_flag+1}")
    
def enp_capture(oldrow,oldcolumn,newcol,obj):
    global candidates, white_flag,black_flag
    
    if white_flag!=0 and obj.name in candidates:
        if white_flag!=1 and oldcolumn==newcol-1:
            cid = alive[state[oldrow][newcol]].cid
            canvas.delete(cid)
            alive.pop(state[oldrow][newcol])
            state[oldrow][newcol] = 0
        if white_flag!=8 and oldcolumn==newcol+1:
            cid = alive[state[oldrow][newcol]].cid
            canvas.delete(cid)
            alive.pop(state[oldrow][newcol])
            state[oldrow][newcol] = 0
    elif black_flag!=0 and obj.name in candidates:
        if black_flag!=1 and oldcolumn==newcol-1:
            cid = alive[state[oldrow][newcol]].cid
            canvas.delete(cid)
            alive.pop(state[oldrow][newcol])
            state[oldrow][newcol] = 0
        if black_flag!=8 and oldcolumn==newcol+1:
            cid = alive[state[oldrow][newcol]].cid
            canvas.delete(cid)
            alive.pop(state[oldrow][newcol])
            state[oldrow][newcol] = 0
            
def wpromotion():
    pq.grid(row=0,column=8)
    pr.grid(row=1, column=8)
    pb.grid(row=2, column=8)
    pn.grid(row=3, column=8)

def bpromotion():
    PQ.grid(row=0,column=8)
    PR.grid(row=1, column=8)
    PB.grid(row=2, column=8)
    PN.grid(row=3, column=8)


def promo(category):
    category = str(category)
    global promoted, new_square
    
    p_count = len(promoted)
    [new_row,new_col] = new_square
    cid = alive[state[new_row][new_col]].cid
    canvas.delete(cid)
    alive.pop(state[new_row][new_col])
    
    var = category+"&"+f"{p_count}"
    state[new_row][new_col] = var
    alive[var]  = create(var,new_square.copy())
    
    if category.isupper():
            promoted.append(ImageTk.PhotoImage(file = f"C:\\Users\\prashant kumar\\Desktop\\chess\\images\\{category}{category}.png"))
    else:
            promoted.append(ImageTk.PhotoImage(file = f"C:\\Users\\prashant kumar\\Desktop\\chess\\images\\{category}.png") )
    cid = canvas.create_image(new_col*scale, new_row*scale, image=promoted[-1], anchor='nw', tag='draggable')
    alive[var].cid = cid
    
    if category[0].islower():
        pq.grid_forget()
        pb.grid_forget()
        pr.grid_forget()
        pn.grid_forget()
    if category[0].isupper():
        PQ.grid_forget()
        PB.grid_forget()
        PR.grid_forget()
        PN.grid_forget()
        
def check_detect(koord):
    global turn, pawn_block, castle
    if turn==0:
        Dummy = Moves("k")
        X = "K"
    else:
        Dummy = Moves("K")
        X = "k"
        
    c_flag=-1
    checkers = []
    Dummy.available = []
    rook_available = Dummy.Rook(koord)
    rook_available.remove(koord)
    for [i,j] in rook_available:
        if state[i][j]:
            if alive[state[i][j]].category in ["Q","R"]:
                checkers.append(state[i][j])
                c_flag = turn
        
    Dummy.available = []
    bish_available = Dummy.Bishop(koord)
    bish_available.remove(koord)
    for [i,j] in bish_available:
            if state[i][j]:
                if alive[state[i][j]].category in ["Q","B"]:
                    checkers.append(state[i][j])
                    c_flag = turn
                    
    Dummy.available = []
    knight_available = Dummy.Knight(koord)
    knight_available.remove(koord)
    for [i, j] in knight_available:
            if state[i][j]:
                if alive[state[i][j]].category == "N":
                    checkers.append(state[i][j])
                    c_flag = turn
        
    Dummy.available = []
    king_available = Dummy.King(koord)
    king_available.remove(koord)
    for [i, j] in king_available:
            if state[i][j]:
                if alive[state[i][j]].name == X:
                    c_flag = turn

    [i,j]=koord
    if turn==0:
        if pawn_block == 0:
            if (i>=1 and j>=1 and state[i-1][j-1]):
                if state[i-1][j-1][0] == "P":
                    checkers.append(state[i-1][j-1])
                    c_flag = 0
            if (i >= 1 and j <=6 and state[i-1][j+1]):
                if state[i-1][j+1][0] == "P":
                    checkers.append(state[i-1][j+1])
                    c_flag = 0
        else:
            if i>=1:
                if state[i-1][j]!= 0 and state[i-1][j][0]=="P":
                    checkers.append(state[i-1][j])
                    c_flag = 0
                if i==3:
                    if state[i-1][j]==0 and state[i-2][j]!=0 and state[i-2][j][0]=="P":
                        checkers.append(state[i-2][j])
                        c_flag = 0

    elif turn ==1:
        if pawn_block==0:
            if (i <= 6 and j <= 6 and state[i+1][j+1]):
                if state[i + 1][j + 1][0] == "p":
                    checkers.append(state[i+1][j+1])
                    c_flag = 1
            if (i <= 6 and j >= 1 and state[i+1][j-1]):
                if state[i + 1][j - 1][0] == "p":
                    checkers.append(state[i+1][j-1])
                    c_flag = 1
        else:
            if i<=6:
                if state[i+1][j]!= 0 and state[i+1][j][0]=="p":
                    checkers.append(state[i+1][j])
                    c_flag = 1
                if i==4:
                    if state[i+1][j]==0 and state[i+2][j]!=0 and state[i+2][j][0]=="p":
                        checkers.append(state[i+2][j])
                        c_flag = 1

    return c_flag,checkers

def calid(oldrow, oldcol,newrow,newcol):
    
    global state,check_flag, candidates, white_flag, black_flag, castle
    
    if turn==0:
        koord = alive["k"].coord 
    else:
        koord = alive["K"].coord

    shadow = deepcopy(state)
    state[newrow][newcol] = state[oldrow][oldcol] 
    state[oldrow][oldcol] = 0    
    if len(candidates)>0:
        if white_flag!=0:
            if white_flag!=1 and oldcol==newcol-1:
                state[oldrow][newcol] = 0
            if white_flag!=8 and oldcol==newcol+1:
                state[oldrow][newcol] = 0
        elif black_flag!=0:
            if black_flag!=1 and oldcol==newcol-1:
                state[oldrow][newcol] = 0
            if black_flag!=8 and oldcol==newcol+1:
                state[oldrow][newcol] = 0
                
    
    check_flag = check_detect(koord)[0]
    
    if check_flag!=-1:
        newrow, newcol = oldrow,oldcol
   
    state = deepcopy(shadow)
    
    return [newrow,newcol]


def castle_detect(oldrow,oldcol,newrow,newcol):
    global check_flag, state,scale
    
    if turn == 0 and check_detect([7,4])[0]!=0:
        if castle[0][0] == 1 and newcol ==  oldcol+2 and state[7][5]==0 and state[7][6]==0 and check_detect([7,5])[0]!=0 and check_detect([7,6])[0]!=0:
            cid = alive[state[7][7]].cid
            canvas.move(cid,-2*scale,0)
            alive[state[7][7]].coord = [7,5]
            state[7][5] = state[7][7]
            state[7][7] = 0
        elif castle[0][1] == 1 and newcol ==  oldcol-2 and state[7][3]==0 and state[7][2]==0 and state[7][1]==0 and check_detect([7,3])[0]!=0 and check_detect([7,2])[0]!=0:
            cid = alive[state[7][0]].cid
            canvas.move(cid,3*scale,0)
            alive[state[7][0]].coord = [7,3]
            state[7][3] = state[7][0]
            state[7][0] = 0
        else:
            newrow,newcol = oldrow,oldcol

                
    elif turn == 1 and check_detect([0,4])[0]!=1:
        if castle[1][0] == 1 and newcol ==  oldcol+2 and state[0][5]==0 and state[0][6]==0 and check_detect([0,5])[0]!=1 and check_detect([0,6])[0]!=1:
            cid = alive[state[0][7]].cid
            canvas.move(cid,-2*scale,0)
            alive[state[0][7]].coord = [0,5]
            state[0][5] = state[0][7]
            state[0][7] = 0
        elif castle[1][1] == 1 and newcol ==  oldcol-2 and state[0][3]==0 and state[0][2]==0 and state[0][1]==0 and check_detect([0,3])[0]!=1 and check_detect([0,2])[0]!=1:
            cid = alive[state[0][0]].cid
            canvas.move(cid,3*scale,0)
            alive[state[0][0]].coord = [0,3]
            state[0][3] = state[0][0]
            state[0][0] = 0
        else:
            newrow,newcol = oldrow,oldcol

    return [newrow, newcol]

def escape_check(coord):
    global state,turn, castle

    if turn == 0:
        Dummy = Moves("k")
    if turn ==1:
        Dummy = Moves("K")
        
    castlecopy = deepcopy(castle)
    castle[turn] = [0,0]
    king_moves = Dummy.King(coord)
    king_moves.remove(coord)
    castle = castlecopy
    xk = state[coord[0]][coord[1]]
    state[coord[0]][coord[1]] = 0
    for i in king_moves:
        if check_detect(i)[0]!=turn:
                escapable = True
                break
    else:
        escapable = False
    state[coord[0]][coord[1]] = xk

    return escapable

def capture_check(enemy):
    global turn
    turn = 1-turn
    warriors = check_detect(enemy)[1]
    turn = 1-turn
    return warriors

def pinned(coord, enemy=None):
    global turn, state
    
    pinners = []
    turn = 1-turn
    friends = queen_span(coord)
    turn = 1-turn
    if enemy!=None:
        enex = state[enemy[0]][enemy[1]]
        state[enemy[0]][enemy[1]] = 0
    for i in friends:
        xf = state[i[0]][i[1]]
        state[i[0]][i[1]] = 0
        if check_detect(coord)[0]==turn:
            pinners.append(xf)
        state[i[0]][i[1]] = xf
    if enemy!=None:
        state[enemy[0]][enemy[1]] = enex
        
    return pinners

def queen_span(coord):
    global turn
    
    if turn==0:
        Dummy = Moves("q")
        enemy_set = ["Q","R","B","N","P","K"]
    else:
        Dummy = Moves("Q")
        enemy_set = ["q","r","b","n","p","k"]
    Dummy.available = []
    checkers = []
    Dummy.drive(coord)
    queen_available =  Dummy.available
    queen_available.remove(coord)
    for [i,j] in queen_available:
        if state[i][j]:
            if state[i][j][0] in enemy_set:
                checkers.append([i,j])
                
    return checkers

def block_check(coord,enemy):
    global turn, pawn_block
    
    x=0
    y=0
    if coord[0] < enemy[0]:
        x = 1
    if coord[0] > enemy[0]:
        x = -1
    if coord[1] < enemy[1]:
        y = 1
    if coord[1] > enemy[1]:
        y = -1
    block_sq=[]
    a=1
    while (coord[0]+a*x!=enemy[0] or coord[1]+a*y!=enemy[1]):
        block_sq.append([coord[0]+a*x,coord[1]+a*y])
        a+=1
    blockers= set()
    turn = 1-turn
    pawn_block = 1
    for bcoord in block_sq:
        blockers  |= set(check_detect(bcoord)[1])
    turn = 1-turn
    pawn_block = 0
    
    return list(blockers)
    
def checkmate(coord):
    global turn
    
    c_flag, checkers = check_detect(coord)
    if turn == c_flag:
        escapable = escape_check(coord)
        if not(escapable):
            print("# Can't Be Escaped")
            if len(checkers)>1:
                turn = -1
                print("# Can't Capture More Than One Checkers")
                print("# Checkmate")
            else:
                pinners = pinned(coord,alive[checkers[0]].coord)
                warriors = capture_check(alive[checkers[0]].coord)
                capturable = (len(set(warriors)-set(pinners))>0)
                if not(capturable):
                    print("# Can't Be Captured")
                    if checkers[0][0] in ["n","N","p","P"]:
                        turn = -1
                        print("# Can't Block Check of a Knight and Pawn")
                        print("# Checkmate")
                    else:
                        blockers = block_check(coord,alive[checkers[0]].coord)
                        blockable = (len(set(blockers)-set(pinners))>0)
                        if not(blockable):
                            print("# Can't  Be Blocked")
                            print("# Checkmate")
                            turn = -1
                        else:
                            print(" # Can Be Blocked")
                            pass
                else:
                    print("# Can Be Captured")
                    pass
        else:
            print(" # Can Be Escaped")
            pass
        
def stalemate(coord):
    global turn

    c_flag = check_detect(coord)[0]
    livers = []
    for i in alive.keys():
        if alive[i].color==turn and alive[i].category!="K":
            livers.append(i)

    if turn!=c_flag:
        escapable = escape_check(coord)
        if not(escapable):
            #print("# Can't Be Escaped" )
            pinners = pinned(coord)
            movers = set(livers)-set(pinners)
            for i in movers:
                Dummy = Moves(i[0])
                Dummy.drive(alive[i].coord)
                if len(Dummy.available)>0:
                    #print("# Not A Stalemate")
                    break
            else:
                turn=-1
                print("# Draw By Stalemate")
        else:
            #print("# Can Be Escaped" )
            pass

def insuff_mater():
    global turn
    whites = []
    white_sights = []
    blacks = []
    black_sights = []
    white_insuff = False
    black_insuff = False
    for i in alive.keys():
        if alive[i].color==0 and alive[i].category!="K":
            whites.append(alive[i].category)
            white_sights.append(alive[i].sight)
        elif alive[i].category!="K":
            blacks.append(alive[i].category)
            black_sights.append(alive[i].sight)

    if len(white_sights)>1:
        for i in white_sights:
            if white_sights[i]==0:
                break
            else:
                if white_sights[0]!=white_sights[i]:
                    break
        else:
            white_insuff = True
            
    if len(black_sights)>1:
        for i in black_sights:
            if black_sights[i]==0:
                break
            else:
                if black_sights[i]!=black_sights[0]:
                    black_insuff = False
                    break
        else:
            black_insuff = True

    if whites in [["B"],["N"],[]]:
        white_insuff = True
    if blacks in [["B"],["N"],[]]:
        black_insuff = True

    if white_insuff and black_insuff:
        turn = -1
        print("# Draw By Insuffient Materieal")
        
def main():
    pass

# Constants
bsize = 8
scale = 80
gap = 14
redc = 3
bar = 73
value = {"K":0,"Q":9.44,"R":5.55,"B":3.33,"N":3,"P":1}

#Flags
dragged_item = None
#current_coord = 0,0
turn = 0
white_flag = 0
black_flag = 0
candidates = []
check_flag = -1
pawn_block = 0
castle = [[1,1],[1,1]] # [0][0] : wshort, [0][1] : wlong, [1][0]: bshort, [1][1] : blong
n_moves = 0
fmrule = 0
capture_flag = 0

# Variables
state = [[0 for j in range(bsize)] for i in range(bsize)]
squares = [[ 0 for j in range(bsize)] for i in range(bsize)]
pimages = [[ 0 for j in range(bsize)] for i in range(bsize)]
promoted = []


#Starting Position
state[0] = ['R1', 'N1', 'B1', 'Q', 'K', 'B2', 'N2', 'R2']
state[1] = ["P1", "P2", 'P3', "P4", 'P5', 'P6', "P7", "P8"]
state[6] = ["p1", "p2", 'p3', 'p4', "p5", 'p6', "p7", "p8"]
state[7] = ['r1', 'n1', 'b1', 'q', 'k', 'b2', 'n2', 'r2']

alive = make(bsize,state)

freq = {}
dumstate = deepcopy(state)
dumstate = tuple(map(tuple,dumstate))
freq[dumstate] = 1



if __name__=="__main__":

    # Defining Root of Tkinter
    root = Tk()

    # Creating Canvas
    canvas = Canvas(root, width=scale*bsize, height=scale*bsize)
    canvas.grid(row=0,column=0,rowspan=bsize,columnspan=bsize)
        
    canvas.tag_bind('draggable', '<ButtonPress-1>', pick)
    canvas.tag_bind('draggable', '<B1-Motion>', drag)
    canvas.tag_bind('draggable', '<ButtonRelease-1>', release)

    # Promotion Imgaes

    q=ImageTk.PhotoImage(Image.open(f"C:\\Users\\prashant kumar\\Desktop\\chess\\images\\q.png").resize((60,60)))
    pq = Button(image=q,command = lambda: promo("q"),bg="pink")
    r=ImageTk.PhotoImage(Image.open(f"C:\\Users\\prashant kumar\\Desktop\\chess\\images\\r.png").resize((60,60)))
    pr = Button(image=r,command = lambda: promo("r"),bg="pink")
    bb=ImageTk.PhotoImage(Image.open(f"C:\\Users\\prashant kumar\\Desktop\\chess\\images\\b.png").resize((60,60)))
    pb = Button(image=bb,command = lambda: promo("b"),bg="pink")
    n=ImageTk.PhotoImage(Image.open(f"C:\\Users\\prashant kumar\\Desktop\\chess\\images\\n.png").resize((60,60)))
    pn = Button(image=n,command = lambda: promo("n"),bg="pink")

    Q=ImageTk.PhotoImage(Image.open(f"C:\\Users\\prashant kumar\\Desktop\\chess\\images\\qq.png").resize((60,60)))
    PQ = Button(image=Q,command = lambda: promo("Q"),bg="pink")
    R=ImageTk.PhotoImage(Image.open(f"C:\\Users\\prashant kumar\\Desktop\\chess\\images\\rr.png").resize((60,60)))
    PR = Button(image=R,command = lambda: promo("R"),bg="pink")
    B=ImageTk.PhotoImage(Image.open(f"C:\\Users\\prashant kumar\\Desktop\\chess\\images\\bb.png").resize((60,60)))
    PB = Button(image=B,command = lambda: promo("B"),bg="pink")
    N=ImageTk.PhotoImage(Image.open(f"C:\\Users\\prashant kumar\\Desktop\\chess\\images\\nn.png").resize((60,60)))
    PN = Button(image=N,command = lambda: promo("N"),bg="pink")
    # Call Statements
    print("#"*bar)
    build(bsize)
    deploy(bsize,state)
    display(state,bsize,gap,redc,bar)


    # Closing Root
    root.mainloop()

    main()
