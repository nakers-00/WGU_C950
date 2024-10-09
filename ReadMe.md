F:
F.1: 
One strength of the nearest neighbor algorithm is that it is simple and easy to implement. Since this project calls for
total mileage to be less than 140 miles there was no need to create a complex algorithm when nearest neighbor could
easily find a delivery route that satisfies the requirements. This simplicity made it easy to develop, as well as making
it easy for any future development to be done on this program. If a new programmer needed to work with my code it would
be easy to pick up and understand quickly. Another strength of this algorithm is that it that it can work with changing
data. If new packages were added with different delivery addresses then this algorithm could be used for those packages
without any change to its code; as long as the distance table was provided for the new addresses. Another strength is 
that this algorithm does not need data to be ordered or input in any special way. As long as the distances between 
addresses are provided, the algorithm can find the closest address from a given current address. Even though this is not
guaranteed to yield the optimal route, it is a simple and effective way to find an adequate route for this problem.

F.2:
My algorithm meets the requirements of this scenario because it delivers all packages in 115 miles, which is under 
140 miles, and all time deadlines are met. All special notes are followed and packages are loaded onto the correct 
truck when specified and delivered with the correct other packages when specified. The packages that are delayed on
flights do not depart from the hub until after they arrive on the flight and package 9 does not depart until after the 
time when its address will be updated. 

F.3:
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
The hash table data structure that I used in this program meets all requirements for this scenario. It does not use an 
additional libraries or classes, and it has an insert function that takes package ID as input and uses that as a key 
to insert package information into the hash table at the correct location. The requirements list the package informaiton
that must be stored in the hash table and I accomplished this by storing package objects within the hash table. These
package objects already contain the package information. This allows for much easier access of the package information
during my nearest neighbor algorithm. The hash table that I created also has a look-up function that takes in a package
ID and returns a package object, which contains all the required package information in an easy-to-access format. 

Another data structure that I could use is a weighted graph. This data structure would store package information along
with information about the distances between the delivery addresses of each package. This would allow for easy access
to package information as well as information about their distances. This would negate some of the need for the delivery
algorithm to calculate the distances between packages, because that information would be stored with the package info.

(Lysecky, R., & Vahid, F. (2018, June). C950: # Data Structures and Algorithms II. zyBooks.)

