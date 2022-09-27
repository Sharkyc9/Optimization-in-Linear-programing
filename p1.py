import os
import re
import csv
#glpsol --lp a2.lp -o output.txt
graph = {
    1: [2, 3, 4],
    2: [1, 5, 6],
    3: [1, 7, 8],
    4: [1, 8, 9],
    5: [2, 6, 9],
    6: [2, 5, 12],
    7: [3, 8, 11],
    8: [3, 4, 7],
    9: [4, 5, 10],
    10: [9, 11, 12],
    11: [7, 10, 12],
    12: [6, 10, 11],

}
optimal=329388
#construct the dict
with open('a2.csv') as f:
    reader = csv.reader(f)
    rows = list(reader)

pos_list=rows[optimal]
key_list =[]
for i in range(1,13):
    key_list.append(i)
b=dict(zip(key_list,pos_list))
print(b)

i="_"

#analyze the placement and store the position
s = ""
quarry = []
factory = []
market = []
for vertex in b:
     if b[vertex] =="quarry":
       quarry.append(vertex)
     elif b[vertex] == "factory":
       factory.append(vertex)
     elif b[vertex] == "market":
       market.append(vertex)



f = open("a2.lp", "w")
f.write("Subject To\n")
f.write("\n")


s = ""
quarry = []
factory = []
market = []
for vertex in b:
     if b[vertex] =="quarry":
       quarry.append(vertex)
     elif b[vertex] == "factory":
       factory.append(vertex)
     elif b[vertex] == "market":
       market.append(vertex)



#max fuction
#all the input - output is the sold items from market
def declaremax():
     global g_sold
     global d_sold
     global j_sold
     g_sold = ""
     d_sold = ""
     j_sold = ""

     s = "Maximize\n"
     for from_vertex in market:
        for neighbor in graph[from_vertex]:
          if neighbor in market :
              s +=""
          else:
            s += "150g" + str(neighbor) + i + str(from_vertex) + " - " + "150g" + str(from_vertex) + i + str(neighbor) + " + " \
                   + "200d" + str(neighbor) + i + str(from_vertex) + " - " + "200d" + str(from_vertex) + i + str(neighbor) + " + " \
                   + "1000j" + str(neighbor) + i + str(from_vertex)

            # accumulate the sold
            g_sold += "g" + str(neighbor) + i + str(from_vertex) + " - " + "g" + str(from_vertex) + i + str(neighbor)
            d_sold += "d" + str(neighbor) + i + str(from_vertex) + " - " + "d" + str(from_vertex) + i + str(neighbor)
            j_sold += "j" + str(neighbor) + i + str(from_vertex)

            if from_vertex == market[- 1] and neighbor == graph[from_vertex][- 1]:
                s += "\n"

            else:
                s += " + "
                g_sold += " + "
                d_sold += " + "
                j_sold += " + "



     f.write(s)


#restrict the efficiencies by energy
# a represent efficiencies
def efficiencies():
    s = ""
    for vertex in b:
        f.write("a"+ str(vertex)+"<= 1\n")
        if vertex != 1:
            s += " + "
        if b[vertex] == "quarry":

            s += "100a" + str(vertex)
        elif b[vertex] == "factory":

            s += "300a" + str(vertex)
        elif b[vertex] == "market":

            s += "0a"+ str(vertex)
    s += "<= 850\n"
    f.write(s)


#restrict the connection units
def road():
    s = ""
    for from_vertex in graph:
        for to_vertex in graph[from_vertex]:
            s = "x" + str(from_vertex)+i + str(to_vertex) + " >= 0\n"
            f.write(s)
            s = "x" + str(from_vertex)+i + str(to_vertex) + " + "+"x" + str(to_vertex)+i + str(from_vertex)+" <= 165\n"
            f.write(s)

    #every road x has a equalation denmonstrate the relationship between three elements
    #g is gold, d is diamonds, j is for jewellery
    for from_vertex in graph:
        for to_vertex in graph[from_vertex]:
         s += "g"+str(from_vertex)+i+str(to_vertex)+" + "+"d"+str(from_vertex)+i+str(to_vertex)+" + "+"j"+str(from_vertex)+i+str(to_vertex)+" - "+"x"+str(from_vertex)+i+str(to_vertex)+" = "+"0\n"

    f.write(s)




# all the stuff that quarry produced is
# output - input
def quarrylimitation():
    s = ""  # store the gold
    t = ""  # store the diamonds

    for from_vertex in quarry:
        for neighbor in graph[from_vertex]:
            s += "g" + str(from_vertex) +i+ str(neighbor) + " - " + "g" + str(neighbor) +i+ str(from_vertex)
            t += "d" + str(from_vertex) +i+ str(neighbor) + " - " + "d" + str(neighbor) +i+ str(from_vertex)

            # if it is last line
            if  neighbor == graph[from_vertex][len(graph[from_vertex]) - 1]:
              s += " - "+"200a"+str(from_vertex)+" = 0"+ "\n"
              t += " - "+"75a"+str(from_vertex)+" = 0"+"\n"

            else:
              s += " + "
              t += " + "

    f.write(s)
    f.write(t)



def factorylimit():
    s = ""  # store the gold
    t = ""  # store the diamonds
    w = ""  # store the jewellery

    for from_vertex in factory:
        for neighbor in graph[from_vertex]:
            s += "g" + str(neighbor) +i+ str(from_vertex)+ " - "+ "g" + str(from_vertex)+i + str(neighbor)
            t += "d" + str(neighbor) +i+ str(from_vertex)+ " - "+ "d" + str(from_vertex)+i + str(neighbor)
            w += "j" + str(from_vertex) +i+ str(neighbor)+ " - "+ "j" + str(neighbor)+i + str(from_vertex)

            if neighbor == graph[from_vertex][len(graph[from_vertex]) - 1]:
                s += " - " + "70a" + str(from_vertex) + " = 0"+"\n"
                t += " - " + "20a" + str(from_vertex) + " = 0"+"\n"
                w += " - " + "60a" + str(from_vertex) + " = 0"+"\n"

            else:
                s += " + "
                t += " + "
                w += " + "

    f.write(s)
    f.write(t)
    f.write(w)

#all the things sold should be less or equal to the overall produce
#allsold +used -all produce <=0
def overalllimit():
    g_pro= ""
    d_pro = ""
    j_pro = ""
    for vertex in quarry:
        g_pro +="200a"+str(vertex)
        d_pro += "75a" + str(vertex)
        if vertex != quarry[len(quarry)-1]:
            g_pro += " - "
            d_pro += " - "

    for vertex in factory:
        j_pro += "60a" + str(vertex)

        if vertex != factory[-1]:

            j_pro  += " - "


    gold= g_sold +" - "+g_pro+"<=0 \n"
    diamonds = d_sold  + " - " + d_pro + "<=0 \n"
    jewellery = j_sold + " - " + j_pro + "<=0 \n"

    f.write(gold)
    f.write(diamonds)
    f.write(jewellery)






#process the code
f = open("a2.lp", "w")
declaremax()
f.write("Subject To\n")
efficiencies()
road()
quarrylimitation()
factorylimit()
overalllimit()

f.write("End\n")
f.close()

