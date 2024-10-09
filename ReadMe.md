F:
F.1: 
Two Strengths

F.2:
Meets requirements - Delivers packages in 115 miles, which is under 140 miles, and all time deadlines are met. All special notes are followed
and packages are loaded onto the correct truck when specified and delivered with the correct other packages when specified.
The packages that are delayed on flights do not depart the hub until after they arrive on the flight.

Dijkstra's shortest path algorithm and the 2-opt algorithm could also be used for this project.
Dijkstra's shortest path is different from my algorithm, the nearest neighbor, because Dijkstra's algorithm starts at
a starting node in a graph and determines the shortest path to every other node from that starting node (Lysecky). 
Nearest neighbor simply finds the next closest delivery address to the current address, without considering the overall path.
Dijkstra's algorithm is more likely to find an optimal path.

The 2-opt algorithm will take a route that already delivers all packages and then go back through the route and look at
every possible swaps between two edges (Weru). It then swaps edges when it finds a swap that results in a shorter route. This
is different from the nearest neighbor algorithm because the nearest neighbor algorithm does not alter its route once it
finds one. A primary goal of the 2-opt algorithm revolves around eliminating edges that cross over each other in the 
route. The nearest neighbor algorithm does not do any sort of analysis of the route other than finding the closest 
address to the current address. 

(Lysecky, R., & Vahid, F. (2018, June). C950: # Data Structures and Algorithms II. zyBooks.)
(Weru, Lawrence. “11 Animated Algorithms for the Traveling Salesman Problem.” STEM Lounge, STEM Lounge, 
24 Aug. 2021, stemlounge.com/animated-algorithms-for-the-traveling-salesman-problem/.)

G:
If I were to do this project again I would use a graphical user interface rather than a 
command line interface. I would use the FreeSimpleGUI library because it is something with
which I have experience. This addition would improve the user experience and make it easier 
to find information about packages.
I would also create an algorithm to predetermine which packages are closest to each other and 
load them onto trucks based on that information. This would decrease the distance travelled by
the trucks because they would not have to travel as far between deliveries. This was not necessary
for this current project because my nearest neighbor algorithm was able to easily determine a delivery
path under the required mileage. 

H:
Another data structure that I could use is a weighted graph. This data structure would store package information along
with information about the distances between the delivery addresses of each package. This would allow for easy access
to package information as well as information about their distances. This would negate some of the need for the delivery
algorithm to calculate the distances between packages, because that information would be stored with the package info.

(Lysecky, R., & Vahid, F. (2018, June). C950: # Data Structures and Algorithms II. zyBooks.)

