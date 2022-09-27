# GLPK Linear Programming
p1.py is the core part of this project. It can automatically output the lp file for solving the linear programming problem and automatically call the GLPK solution according to the characteristics of each point and edge of the Frucht graph and other requirements in the background. A corresponding lp file and output file are generated for each possibility.


# File description
p1.py
The main program, used to output n lp files that can be run by simple GLPK and call them on the command line.
By my own standards, this code is not elegant, but it is sufficient for a deadline with a time limit.

p2.py
The supplementary program, just output all 531,441 possibilities into a csv file.

cases.csv
Record all 531,441 possibilities, as the output of p2.py.
But it's too large to upload. You need to get this file through p2.py first.




# Optimization in Linear programing
In the Frucht graph.
You plan to build a building in each of the 12 locations, which can be a quarry, factory, or market.
There are three types of resources: gold, diamonds and jewelry. Every year, the same amount of resources are sent from the building to the building through the connections. But each connection has a limit: the sum of all resources sent through a connection each year cannot exceed 165 units (for example, if 100 units of gold are sent from a to b, then the amount of diamonds sent from b to a is at most 65).
You have 850 units of energy available every year. Energy is not transmitted through the network, but is available everywhere.

Every year a quarry produces 200 units of gold and 75 units of diamonds. This costs 100 units of energy.
Every year a factory uses 70 units of gold and 20 units of diamonds and produces 60 units of jewellery. This costs 300 units of energy.
The market sells gold, diamonds, and jewellery.

A unit of gold gives £150.
A unit of diamonds gives £200.
A unit of jewellery gives £1000.

Selling costs no energy. The sum of all revenues of all markets is called the total revenue.
Resources cannot be carried forward across the year. The quarries and factories do not need to use up all resources. You can decide to forward or destroy any number of resources. The forwarding and destruction of resources does not consume energy. You also don’t have to sell everything that is delivered to the market. You can forward these resources instead. Obviously, it does not make sense to forward jewelry through the market instead of selling it, but in principle it may be useful to forward gold or diamonds instead of selling them so that they can be converted into jewelry in the factory.
The operating efficiency of quarries and factories can be less than 100%. Their input, output, and energy use decline linearly.
