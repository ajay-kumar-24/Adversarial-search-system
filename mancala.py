'''
    Created on Oct 8, 2015
    
    @author: AJ
    '''
from sys import maxint
from sys import maxsize
import sys
import pdb
import pdb;
import copy;


class Mancala:
    task=''
    my_player=''
    player_1=[]
    player_2=[]
    mancala1=[]
    mancala2=[]
    cut_off=0
class Node(object):
    def __init__(self,board,depth,my_player,value):
        self.depth= depth
        self.board=board
        self.name='root'
        self.my_player=my_player
        self.next_player=0
        self.value=- float("inf")
        self.children=[]


flag=0
def max_list(list1,my_player,n):
    l = len(list1)-1
    ##print l
    k=[]
    n=(n-2)/2
    i=0
    list1=terminal_no(list1, my_player, n)
    maxi=[]
    while(l>=0):
        
        if (my_player==1):
            k=list1[i]
            maxi.append(k[n+1])
        else:
            k=list1[l]
            maxi.append(k[0])
        i=i+1
        l=l-1
    high=max(maxi)
    if(my_player!=1):
        maxi.reverse()
    index=maxi.index(high)
    return list1[index]

list3=None
max_node=0
f = open('traverse_log.txt', 'w')
g=open('next_state.txt','w')
def next_move(node,start,stones,no,n):
    i=0
    while(stones>0):
        i=i+1
        if(start==0 and node.my_player==1):
            start=1
        else:
            if((start==no) and node.my_player==2):
                start=start+2
            else:
                if((start==(n-1)) and node.my_player==2):
                    start=0
                else:
                    if((start+1)==(n-1)):
                        start=start+1
                    else:
                        
                        start=(start+1)%(n-1)

    node.board[start]=node.board[start]+1
    if(node.board[start]==1 and (start!=0 and start!= no+1) and stones-1 ==0):
        if(node.my_player==1 and (start >=0 and start< no+1)):
            
            node.board[no+1]=node.board[no+1]+1+node.board[n-start]
                node.board[n-start]=0
                node.board[start]=0
            else:
                if(node.my_player==2 and (start >no+1 and start <n)):
                    node.board[0]=node.board[0]+1+node.board[n-start]
                    node.board[start]=0
                    node.board[n-start]=0
    stones=stones-1
    if(stones==0):
        flag=0
        if(node.my_player==1):
            if(start==no+1):
                node.next_player=node.my_player
            else:
                node.next_player=2
            for x in range(1,no+1):
                if(node.board[x]!=0):
                    flag=flag+1
            if(flag==0):
                for x in range(no+2,n):
                    node.board[0]=node.board[0]+node.board[x]
    else:
        if(start==0):
            node.next_player=node.my_player
            else:
                node.next_player=1
        for x in range(no+2,n):
            if(node.board[x]!=0):
                flag=flag+1
            if(flag==0):
                for x in range(1,no+1):
                    node.board[no+1]=node.board[no+1]+node.board[x]


                        return node

def next_moves(node,n):
    no=(n-2)/2
    k=no
    ko=0
    if(node.name[0]=='r'):
        if(node.my_player==1):
            start=1
            names='B'
            ko=1
        else:
            start=n-1
            names='A'
            ko=2
    else:
        if(node.next_player==2):
            start=n-1
            names='A'
            ko=2
        else:
            start=1
            names='B'
            ko=1

total=[]
    i=2 
    while(k>0):
        temp=copy.deepcopy(node)
        stones=temp.board[start]
        temp.board[start]=0
        if(names=='A'):
            temp.my_player=2
        else:
            temp.my_player=1
        temp.name=names+str(i)
        tem=next_move(temp,start,stones,no,n)
        i=i+1
        if(tem.board!= node.board):
            
            total.append(tem)
        k=k-1
        if(ko==1):
            if(start+1==n-1):
                start=start+1
            else:
                start=(start+1)%(n-1)
    else:
        start=start-1
return total

def initialize(board,my_player):
    node= Node(board,0,my_player,'-Infinity')
    if (my_player==1):
        node.next_player=2
    else:
        node.next_player=1
    return node


def terminal(node):
    t=False
    n=len(node.board)
    no=(n-2)/2
    if(node.my_player==1):
        flag=0
        for x in range(1,no+1):
            if(node.board[x]!=0):
                flag=flag+1
        if(flag==0):
            t=True
    else:
        if(node.my_player==2):
            flag=0
            for x in range(no+2,n):
                if(node.board[x]!=0):
                    flag=flag+1
        if(flag==0):
            t=True
    return t

def evaluate(node):
    global myplayer
    eval=0
    n=len(node.board)
    n=(n-2)/2
    if(myplayer==1):
        eval=node.board[n+1]-node.board[0]
    else:
        eval=node.board[0]-node.board[n+1]
    return eval

def minimax(node,depth,max_player,prev_node,cut_off):
    global max_node
    
    if depth > cut_off or terminal(node):
        best_val=[0,None]
        best_val[0]= evaluate(node)
        
        node.value=best_val[0]
        f.write(node.name +','+value(node.depth)+','+ value(node.value)+'\n')
        if max_player:
            best_val[1]=prev_node.board
        else:
            best_val[1]=node.board
        
        return best_val

    else:
        if (depth==cut_off):
            best_val=[0,None]
            best_val[0]=evaluate(node)
            if max_player:
                best_val[1]=prev_node.board
            else:
                best_val[1]=node.board
        
        node.children=next_moves(node, len(node.board))

if max_player :
    best_val =  [-float("inf"),prev_node.board]
        f.write(node.name +','+value(node.depth)+','+ value(best_val[0])+'\n')
            for  child in node.children :
                t=False
                if(node.name[0]==child.name[0]):
                    child.depth=node.depth
                    d=child.depth
                    
                    if(child.my_player!=child.next_player):
                        d=child.depth+1
                    
                    if(max_node==child.next_player):
                        t=True
                    val = minimax(child, d, t,node,cut_off)
                    if val[0] > best_val[0]:
                        best_val[0] = val[0]
                        best_val[1] = copy.copy(val[1])
                
                else:
                    child.depth=node.depth+1
                    if(child.next_player!=child.my_player):
                        d=child.depth+1
                    else:
                        d=child.depth
                    if(max_node==child.next_player):
                        t=True
                    val=minimax(child,d,t,node,cut_off)  
                    if val[0] > best_val[0]:
                        best_val[0] = val[0]
                        best_val[1] = copy.copy(val[1])
                f.write(node.name +','+value(node.depth)+','+ value(best_val[0])+'\n')
                if(node.depth==0):
                    boards.append(child.board)
                        names.append(child.name)
                        mancalas.append(best_val[0])
    else:
        best_val =  [float("inf"),node.board]
            f.write(node.name +','+value(node.depth)+','+ value(best_val[0])+'\n')
            for child in node.children:
                t=False
                if(node.name[0]==child.name[0]):
                    child.depth=node.depth
                    
                    d=child.depth
                    if(max_node==child.next_player):
                        t=True
                    if(child.next_player!= child.my_player):
                        d=child.depth+1
                    val = minimax(child, d, t,node,cut_off)
                    
                    if val[0] < best_val[0]:
                        best_val[0] = val[0]
                        best_val[1] = node.board
        else:
            
            if(child.next_player!=child.my_player):
                child.depth=node.depth+1
                    d=child.depth+1
                    else:
                        
                        child.depth=node.depth+1
                        d=child.depth
            
                if(max_node==child.next_player):
                    t=True
                    
                    val=minimax(child,d,t,node,cut_off)
                    if val[0] < best_val[0]:
                        best_val[0] = val[0]
                        best_val[1] = node.board
                        f.write(node.name +','+value(node.depth)+','+ value(best_val[0])+'\n')
                        return best_val

def value(val):
    if(val== -float("inf")):
        v='-Infinity'
    else:
        if(val== float("inf")):
            v='Infinity'
        else:
            v=str(val)
    return v
boards=[]
names=[]
mancalas=[]
def alphabeta(node,depth,max_player,prev_node,cut_off,alpha,beta):
    global max_node    
    if depth > cut_off or terminal(node):
        best_val=[0,None]
        best_val[0]= evaluate(node)
        node.value=best_val[0]
        f.write(node.name +','+str(node.depth)+','+ value(node.value)+','+value(alpha)+','+value(beta)+'\n')
        if max_player:
            best_val[1]=prev_node.board
        else:
            best_val[1]=node.board
        return best_val
    else:
        if(depth==cut_off):
            best_val=[0,None]
            best_val[0]=evaluate(node)
            if max_player:
                best_val[1]=prev_node.board
            else:
                best_val[1]=node.board
node.children=next_moves(node, len(node.board))    
    if max_player :
        best_val =  [-float("inf"),prev_node.board]
            f.write(node.name +','+str(node.depth)+','+ value(best_val[0])+','+value(alpha)+','+value(beta)+'\n')
            global boards
            global names
            global mancalas
            for  child in node.children :
                t=False
                if(node.name[0]==child.name[0]):
                    child.depth=node.depth
                    d=child.depth
                    if(child.my_player!=child.next_player):
                        d=child.depth+1
                    
                    if(max_node==child.next_player):
                        t=True
                    val=alphabeta(child, d, t,node,cut_off,alpha,beta)
                    if(best_val[0]<val[0]):
                        best_val[1]=copy.copy(val[1])
                        best_val[0]=val[0]
                    
                    if(node.depth==0):
                        boards.append(child.board)
                        names.append(child.name)
                        mancalas.append(best_val[0])
                    
                    if(beta<=best_val[0]):
                        f.write(node.name +','+str(node.depth)+','+ value(best_val[0])+','+value(alpha)+','+value(beta)+'\n')
                        break
                    else:
                        alpha= max(best_val[0],alpha)
                        f.write(node.name +','+str(node.depth)+','+ value(best_val[0])+','+value(alpha)+','+value(beta)+'\n')    
                else: 
                    child.depth=node.depth+1
                    if(child.next_player!=child.my_player):
                        d=child.depth+1
                    else:
                        d=child.depth
                    if(max_node==child.next_player):
                        t=True
                    
                    
                    val=alphabeta(child, d, t,node,cut_off,alpha,beta)
                    if(best_val[0]<val[0]):
                        best_val[1]=copy.copy(val[1])
                        best_val[0]=val[0]
                    if(beta<=best_val[0]):
                        f.write(node.name +','+str(node.depth)+','+ value(best_val[0])+','+value(alpha)+','+value(beta)+'\n')
                        break
                    else:
                        alpha= max(best_val[0],alpha)
                        f.write(node.name +','+str(node.depth)+','+ value(best_val[0])+','+value(alpha)+','+value(beta)+'\n')
                if(node.depth==0):
                    boards.append(child.board)
                        names.append(child.name)
                        mancalas.append(best_val[0])
        return best_val
        else:
            best_val =  [float("inf"),prev_node.board]
            f.write(node.name +','+str(node.depth)+','+ value(best_val[0])+','+value(alpha)+','+value(beta)+'\n')
            for child in node.children:
                t=False
                if(node.name[0]==child.name[0]):
                    child.depth=node.depth
                    d=child.depth                    
                    if(max_node==child.next_player):
                        t=True
                    if(child.next_player!= child.my_player):
                        d=child.depth+1                    
                    val=alphabeta(child, d, t,node,cut_off,alpha,beta)
                    if(best_val[0]>val[0]):
                        best_val[1]=node.board
                        best_val[0]=val[0]
                    if best_val[0]<= alpha :
                        f.write(node.name +','+str(node.depth)+','+ value(best_val[0])+','+value(alpha)+','+value(beta)+'\n')  
                        break
                    else:
                        beta=min(beta,best_val[0])
                        f.write(node.name +','+str(node.depth)+','+ value(best_val[0])+','+value(alpha)+','+value(beta)+'\n')
        
        
        else:            
            if(child.next_player!=child.my_player):
                child.depth=node.depth+1
                    d=child.depth+1
                    else:
                        
                        child.depth=node.depth+1
                        d=child.depth
                        if(max_node==child.next_player):
                            t=True
                            val=alphabeta(child, d, t,node,cut_off,alpha,beta)
                            if(best_val[0]>val[0]):
                                best_val[1]=node.board
                                best_val[0]=val[0]
                                if best_val[0]<= alpha :
                                    f.write(node.name +','+str(node.depth)+','+ value(best_val[0])+','+value(alpha)+','+value(beta)+'\n')
                                    break
                                else:
                                    beta=min(beta,best_val[0])
                                    f.write(node.name +','+str(node.depth)+','+ value(best_val[0])+','+value(alpha)+','+value(beta)+'\n')
                            return best_val
                                return best_val


def moves(board,my_player,start,stones,no,n):
    
    while(stones>0):
        if(start==0 and my_player==1):
            start=1
        else:
            if((start==no) and my_player==2):
                start=start+2
            else:
                if((start==(n-1)) and my_player==2):
                    start=0
                else:
                    if((start+1)==(n-1)):
                        start=start+1
                    else:
                        
                        start=(start+1)%(n-1)
    board[start]=board[start]+1
    if(board[start]==1 and (start!=0 and start!= no+1) and stones-1 ==0):
        if(my_player==1):
            board[no+1]=board[no+1]+1+board[n-start]
                board[n-start]=0
                    board[start]=0
            else:
                board[0]=board[0]+1+board[n-start]
                    board[start]=0
                    board[n-start]=0
    stones=stones-1
if(stones==0):
    if(my_player==2):
        if(start==0):
            board=best_max_move(board, my_player, n,0,0)        
        else:
            if(start==no+1):
                board=best_max_move(board, my_player, n,0,0)
return board

def possible_moves(board,my_player,n):
    no=(n-2)/2
    k=no
    if(my_player==1):
        start=1
    else:
        start=n-1
    total=[]
    while(k>0):
        temp=copy.copy(board)
        stones=temp[start]
        temp[start]=0
        total.append(moves(temp,my_player,start,stones,no,n))
        k=k-1
        if(my_player==1):
            if(start+1==n-1):
                start=start+1
            else:
                start=(start+1)%(n-1)
        else:
            start=start-1
    return total

def termin(list1,my_player,n):
    li=list1
    if(my_player ==1):
        flag=0
        for x in range(1,n+1):
            if(li[x]!=0):
                
                flag=flag+1
        if(flag==0):
            for x in range (n+2,2*n+2):
                li[x]=0
                x=x+1
    else:
        if(my_player==2):
            flag=0
            for x in range(n+2,2*n+2):
                if(li[x]!=0):
                    flag=flag+1
        if(flag==0):
            for x in range (1,n+1):
                li[x]=0
                x=x+1

    list1=li
    
    return list1

def terminal_no(list1,my_player,n):
    l=len(list1)
    for i in range (0,l) :
        li=list1[i]
        if li== None :
            continue
        if(my_player ==1):
            flag=0
            for x in range(1,n+1):
                if(li[x]!=0):
                    
                    flag=flag+1
            if(flag==0):
                for x in range (n+2,2*n+2):
                    li[0]=li[0]+li[x]
                    li[x]=0
                    x=x+1
        else:
            if(my_player==2):
                flag=0
                for x in range(n+2,2*n+2):
                    if(li[x]!=0):
                        flag=flag+1
            if(flag==0):
                for x in range (1,n+1):
                    li[n+1]=li[n+1]+li[x]
                    li[x]=0
                    x=x+1
                    list1[i]=li
                    i=i+1
        return list1

def end_state(final,no,n):
    
    
    a1=final[0]    
    a2=final[no]
    p2=final[no+1:]
    p1=final[1:no]
    p2.reverse()
    i=n-1
    s=''
    while i>=no+1 :
        s=s+str(final[i])
        if(i!=no+1):
            s=s+' '
        i=i-1
    i=1
    t=''
    while i<no :
        t=t+str(final[i])
        if(i!=no+1):
            t=t+' '
        i=i+1
    g.write(s)
    g.write('\n')
    g.write(t+'\n')
    g.write(str(a1)+'\n')
    g.write(str(a2)+'\n')
def best_max_move(board,my_player,n,type,board_max):
    list1=[]
    final=[]
    no=(n-2)/2 +1
    list1=possible_moves(board, my_player, n)
    return max_list(list1,my_player,n)

def minmax(man,k):
    
    global max_node
    my_player=man.my_player
    max_node=man.my_player
    node=initialize(k, my_player)
    f.write('Node,Depth,Value\n')
    val= minimax(node, node.depth, True,node,man.cut_off)
    n=len(val[1])
    no=(n-2)/2
    val[1]=termin(val[1], man.my_player, no)
    end_state(val[1], no+1, n)

def alphbet(man,k):
    global max_node
    my_player=man.my_player
    max_node=man.my_player
    
    node=initialize(k, my_player)
    f.write('Node,Depth,Value,Alpha,Beta'+'\n')
    val= alphabeta(node, node.depth, True,node,man.cut_off,-float('inf'),float('inf'))
    n=len(val[1])
    no=(n-2)/2
    val[1]=termin(val[1], man.my_player, no)
    end_state(val[1], no+1, n)
    global boards
    global mancalas
    global names

def greedy(man,type,board_max):
    n=len(man.player_1)
    greed= Mancala()
    s=man.player_2
    s.reverse()
    s=[int(i) for i in s]
    s1=man.player_1
    p=[]
    p=man.mancala2+man.player_1+man.mancala1+s
    output=[]
    k=p
    l=n
    global list3
    temp=copy.copy(k)
    best=[]    
    final= best_max_move(temp,man.my_player,2*l+2,type,board_max)
    end_state(final, l+1, 2*l+2)

global myplayer

def main():
    man= Mancala()
    f= open(sys.argv[2],'r+')
    man.task=f.readline()
    man.my_player=int(f.readline())
    global myplayer
    myplayer= man.my_player
    man.cut_off=int(f.readline())
    player=f.readline()
    man.player_2=player.split()
    man.player_2=[int(i) for i in man.player_2]
    player=f.readline()
    man.player_1=player.split()
    man.player_1=[int(i) for i in man.player_1]
    man.mancala1=f.readline().split()
    man.mancala1=[int(i) for i in man.mancala1]
    man.mancala2=f.readline().split()
    man.mancala2=[int(i) for i in man.mancala2]
    n=len(man.player_1)
    greed= Mancala()
    s=man.player_2
    s.reverse()
    s=[int(i) for i in s]
    s1=man.player_1
    p=[]
    p=man.mancala2+man.player_1+man.mancala1+s
    output=[]
    k=p
    if(int(man.task)==1):
        greedy(man,1,0)
    else:
        if(int(man.task)==2):
            minmax(man, k)
        else:
            
            alphbet(man,k)

main()