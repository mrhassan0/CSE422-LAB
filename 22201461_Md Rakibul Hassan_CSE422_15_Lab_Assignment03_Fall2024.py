#CODE IS CONSTRUCTED  BY MD RAKIBUL HASSAN
#ID NUMBER IS : 22201461

print("Problem:  Mortal Kombat ")
print()

import random

class MortalKombat:
    def __init__(self,branching_factor, depth): 
        self.branching_factor= branching_factor  
        self.depth =depth  

    def create_tree(self, curr_depth=0):
        if curr_depth >= self.depth:
            return random.choice([-1, 1]) #random leaf nodes values
        
        #create left and right children
        left_child =self.create_tree(curr_depth + 1)
        right_child= self.create_tree(curr_depth + 1)
        return [left_child, right_child]

    def alphabeta(self, node, depth, maximizing, alpha, beta):
        if depth== 0:
            return node
        if maximizing:  
            value = float('-inf')
            for child in node: # Explore both children
                value= max(value,self.alphabeta(child, depth -1,False, alpha,beta))
                alpha = max(alpha,value)
                if beta <=alpha:
                    break  # Pruning
            return value
        
        else:  
            value =float('inf')
            for child in node:
                value =min(value,self.alphabeta(child, depth-1,True,alpha,beta))
                beta =min(beta,value)
                if beta<=alpha:
                    break  # Pruning
            return value


# DRIVER CODE
starter = int(input("(0 = Scorpion, 1 = Sub-Zero): "))

branching_factor =2  # Binary tree
depth=5  
total_rounds=3 
results =[]

for i in range(total_rounds):
    # Create the game tree
    call = MortalKombat(branching_factor, depth)
    tree = call.create_tree()  #randomized tree in every round
    if starter == 1:
       maximizing=True    # Sub zero wins if final value is +1 , so he wants to maximize the value
       starter=0          # Alternate who starts in the next round
    else:
      maximizing=False    #Scorpion wins if final value is -1, so he wants to minimize the value
      starter=1

    rwinner = call.alphabeta(tree, depth, maximizing, float('-inf'), float('inf'))
    
    if rwinner== 1:
        results.append("Sub-Zero")
    else:
        results.append("Scorpion")
    
    
    

# Logical decision and printing #deciding game winner
swins = results.count("Scorpion")
subwins = results.count("Sub-Zero")
if swins >subwins:
  game_winner="Scorpion"                      
else:
  game_winner="Sub-Zero"

print(f"Game Winner: {game_winner}")
print(f"Total Rounds Played: {total_rounds}")
for j in range(1,total_rounds+1):
    print(f"Winner of Round {j}: {results[j-1]}")

print()
print("Problem: Games with Magic ")
print()

class pacman_game:
    def __init__(self, branching_factor, depth,leaf): 
        self.branching_factor= branching_factor  
        self.depth =depth  
        self.leaf= leaf
    
    def pacman_tree(self, curr_depth=0, i=0):
        # If at leaf node, return the value
        if curr_depth>= self.depth:
            return self.leaf[i]
        
        left_child= self.pacman_tree(curr_depth + 1, i*self.branching_factor)  #left child index = 0,2,4,6,....
        right_child=self.pacman_tree(curr_depth + 1, i *self.branching_factor+ 1) #right child index = 1,3,5,7.....
        
        return [left_child, right_child]
    
    def pacalphabeta(self, node, depth, maximizing, alpha, beta):
        if depth== 0:
            return node
        if maximizing:  
            value = float('-inf')
            for child in node: # Explore both children
                value =max(value, self.pacalphabeta(child, depth - 1, False, alpha, beta))
                alpha =max(alpha, value)
                if beta<= alpha:
                    break  # Pruning
            return value
        
        else:  
            value = float('inf')
            for child in node:
                value = min(value, self.pacalphabeta(child, depth - 1, True, alpha, beta))
                beta = min(beta, value)
                if beta <= alpha:
                    break  # Pruning
            return value
        
    def mod_alphabeta(self, node, depth, alpha): #only maximizing for magic situation 
        if depth ==0:
            return node
        value = float('-inf')
        
        for child in node:  # Explore both children
            value = max(value, self.mod_alphabeta(child, depth - 1, alpha))
            alpha = max(alpha, value)
        return value


#DRIVER CODE PACMAN GAME
cost = int(input('Enter value: '))
depth = 3
bfactor=2
leaf=[3, 6, 2, 3, 7, 1, 2, 0]
call = pacman_game(bfactor, depth,leaf )
pacmantree =call.pacman_tree()

genresult= call.pacalphabeta(pacmantree, depth, True, float('-inf'), float('inf'))

modresult= call.mod_alphabeta(pacmantree, depth, float('-inf'))-cost
modresult_left = call.mod_alphabeta(pacmantree[0], depth-1, float('-inf')) -cost
modresult_right = call.mod_alphabeta(pacmantree[1], depth-1, float('-inf')) -cost

if modresult==modresult_left:
    pos = 'left'
else:
    pos ='right'

if modresult<= genresult:
    print(f"The minimax value is {genresult}. Pacman does not use dark magic") 
else:
    print(f"The new minimax value is {modresult}. Pacman goes {pos} and uses dark magic")