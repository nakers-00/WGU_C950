F:
Another algorithm that could be used is Kruskal's minimum spanning tree algorithm. This algorithm determines the
shortest path that connects all vertices of a graph. It would be paired with a weighted graph data structure
(discussed in part H) to determine the shortest path between packages on a given truck. This algorithm would be used to 
determine the path of least distance that visits all delivery addresses of the packages on a given truck.
This algorithm is different from the nearest neighbor algorithm used in my current implementation of this program in a
few key ways. First, it would use a different data structure, one that indicates the distances between package delivery
addresses. This algorithm also has different time and space complexities than the nearest neighbor algorithm. Kruskal's
algorithm has a space complexity of O(E + V) (E = number of edges, V = number of vertices) and a time complexity of
O(ElogE) (E = number of edges). The nearest neighbor algorithm used in my current program has a time complexity
of O(n^3).
(Lysecky, R., & Vahid, F. (2018, June). C950: # Data Structures and Algorithms II. zyBooks.)
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
This would pair particualrly well with Kruskal's minimum spanning tree algorithm discussed in part F because it will
provide the distances between each vertex and the algorithm can use that information to determine the overall shortest 
path.
(Lysecky, R., & Vahid, F. (2018, June). C950: # Data Structures and Algorithms II. zyBooks.)

