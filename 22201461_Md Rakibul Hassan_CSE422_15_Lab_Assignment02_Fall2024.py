#CODE IS CONSTRUCTED  BY MD RAKIBUL HASSAN
#ID NUMBER IS : 22201461

import random
import math
class genalgo:
    def __init__(self,courses,timeslots,arrsize):
        self.course=courses
        self.timeslots=timeslots
        self.arrsize=arrsize 
        self.arr=[]
        self.newarr=[]

    def single_population(self): #random population generator
        self.st=""
        for i in range(self.arrsize):
            temp= random.randint(0,1)
            self.st+=str(temp)
        return self.st 
       
    def initial_population(self): #initially 10 population generated
        for st in range(10):
            self.arr.append(self.single_population())
        #print(self.arr) 

    def openalty(self):
        self.osum=0 #overlap penalty for single population
        self.peno=[]
        temp=0
        for population in self.arr:
            for index in range(self.arrsize):
               temp+=int(population[index])
               if (index+1)%self.course==0: #every three indexes
                 self.osum+= abs(temp -1) #ex- timeslot 1
                 temp=0

            self.peno.append(self.osum)
            self.osum=0   
        return self.peno #initial populations overlap penalty listed


        
    def cpenalty(self):
        self.penc=[]
        self.csum=0
        temp=0
        t=0

        for population in self.arr:
            for index in range(self.course):
                t=index 
                while t<self.arrsize:
                  temp+= int(population[t])
                  t+=3      #jumping to same courses every time
                            #(0,3,6....) #(1,4,7,....)
                self.csum+= abs(temp -1) 
                temp=0
            self.penc.append(self.csum)
            self.csum=0
        return self.penc

        
    def fitness(self):                              # formula = minus (overlap+cons)
        penc = self.cpenalty()
        peno = self.openalty()
        self.fit=[0]*len(peno)
        for i in range(len(peno)):
            self.fit[i]=-(peno[i]+penc[i])
        return self.fit
    
    def parents(self):                    #choosing two parent from ten parent in self.arr
        temp1=random.randint(0,9)
        temp2=random.randint(0,9)
        parent1= self.arr[temp1]
        parent2=self.arr[temp2]
        return parent1,parent2

    def crossover(self):                  #crossover and creating offspring
      self.newarr=[]
      for x in range(10):
        parent1,parent2=self.parents()
        temp= random.randint(1,7)
        off1= parent1[:temp:]+parent2[temp::]
        off2= parent1[temp::]+ parent2[:temp:]
        self.newarr.append(off1)
        self.newarr.append(off2)
      self.arr=self.newarr  #prev 10 initial populations overwritten by 20 offsprings
      #print(self.newarr)
      #print(len(self.newarr))

    def two_crossover(self):                  
        parent1,parent2=self.parents()
        print(parent1)
        print(parent2)
        point1 = random.randint(1,6)
        point2 = random.randint(point1+1,7)
        print(point1)
        print(point2)
        offs1 = parent1[:point1:]+ parent2[point1:point2+1:] + parent1[point2+1::]
        offs2 = parent2[:point1:]+ parent1[point1:point2+1:] + parent2[point2+1::]
        print(offs1)
        print(offs2)

    def mutation(self):
        for offspring in self.newarr:
            ind = random.randint(0,8)
            replace= random.randint(0,1)
            temp= offspring[:ind:] + str(replace) + offspring[ind+1::]
            i= self.newarr.index(offspring)
            self.newarr[i]=temp #overwriting pre-mutated string
        #print(self.newarr)

    def get_result(self):          #final result based on fitness [maximum]
        temp = self.fitness() #self.arr==self.newarr
        maxx= -(math.inf)
        for i in temp:
           maxx = max(maxx,int(i))
        ind = self.fit.index(maxx)
        print(self.arr[ind])
        print(maxx)


#Input handling
with open('input.txt', 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    courses,timeslots=lines[0].split(" ")
    courses=int(courses)
    timeslots=int(timeslots)
    arrsize= courses*timeslots

call = genalgo(courses,timeslots,arrsize)
call.initial_population()
#print(call.openalty())
#print(call.cpenalty())
#print(call.fitness())
call.crossover()
call.mutation()
#print(call.fitness())
call.get_result()
print("-----------------------------Two point crossover-------------------------------")
call.two_crossover()