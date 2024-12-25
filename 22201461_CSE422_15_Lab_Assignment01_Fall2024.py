#CODE IS CONSTRUCTED  BY MD RAKIBUL HASSAN
#ID NUMBER IS : 22201461

import heapq

class AStar:
    def __init__(self, heuristic, adj, st, end):
        self.heuristic = heuristic  
        self.adj = adj  
        self.st =st  
        self.end= end 
        self.pqueue= [[self.heuristic[st], st, 0]]  # finalcost, current_node, pathcost
        self.parent= {}  

    def calc(self, pathcost, node):
        return pathcost + self.heuristic[node]

    def algorithm(self):
        visited = set()
        while self.pqueue:
            finalcost, current, pathcost = heapq.heappop(self.pqueue)  
            visited.add(current)
            if current == self.end:
                return self.Astarpath(current,pathcost)

            if current in self.adj:
                for neighbor, cost in self.adj[current]:
                    if neighbor not in visited:
                        newpathcost = pathcost + cost  # New cost updated
                        finalcost = self.calc(newpathcost, neighbor)  # finalcost = pathcost+heuristic
                        heapq.heappush(self.pqueue, [finalcost, neighbor, newpathcost])
                        self.parent[neighbor] =current  # Track the path
        
        return "NO PATH FOUND"  # Return if no path is found
        

    def Astarpath(self, node,cost): #backtracking to find path
        path=[]
        while node in self.parent:
            path.append(node)
            node =self.parent[node]
        path.append(self.st)
        path.reverse()
        return path,cost

####------------------------------------------------------------------####
#DRIVER CODE#
####------------------------------------------------------------------####

# Extracting data from the input file
with open('a.txt', 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    heuristic = {}
    adj = {} # {parent:(neighbouring children,true_cost)}
    
    for line in lines:
        temp = line.split(" ")
        heuristic[temp[0]]= int(temp[1]) #{Arad:366, Zerind:374....} #column wise
        neighbors=[]
        for i in range(2,len(temp), 2):
            neighbors.append((temp[i], int(temp[i+1]))) #[(neighbouring children,true_cost)]
        adj[temp[0]]= neighbors

# Input handling
start_node = input("Enter starting point: ")
end_node = input("Enter Destination: ")

#function call and return
call = AStar(heuristic, adj, start_node, end_node)
path,cost = call.algorithm()

#Output handling
sentence = " -> ".join(path) #list to string
print(f"Path: {sentence}")
print(f"Total distance: {cost} km")

        
