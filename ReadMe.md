F:
F.1: 
One strength of the nearest neighbor algorithm is that it is simple and easy to implement. Since this project calls for
total mileage to be less than 140 miles there was no need to create a complex algorithm when nearest neighbor could
easily find a delivery route that satisfies the requirements. This simplicity made it easy to develop, as well as making
it easy for any future development to be done on this program. If a new programmer needed to work with my code it would
be easy to pick up and understand quickly. Another strength of this algorithm is that it can work with changing
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
time when its address will be updated. Since there are only 2 drivers but 3 trucks, only 2 trucks are active at any
given moment.

F.3:
Dijkstra's shortest path algorithm and the 2-opt algorithm could also be used for this project.

Dijkstra's shortest path is different from my algorithm, the nearest neighbor, because Dijkstra's algorithm starts at
a starting node in a graph and determines the shortest path to every other node from that starting node (Lysecky). 
Nearest neighbor simply finds the next closest delivery address to the current address, without considering the overall path.
Dijkstra's algorithm is more likely to find an optimal path. Dijkstra's algorithm would have to be modified slightly to 
yield a shortest path that passes through all delivery addresses, while the nearest neighbor will be able to find this 
by default. 

The 2-opt algorithm will take a route that already delivers all packages and then go back through the route and look at
every possible swap between two edges (Weru). It then swaps edges when it finds a swap that results in a shorter route. This
is different from the nearest neighbor algorithm because the nearest neighbor algorithm does not alter its route once it
finds one. A primary goal of the 2-opt algorithm revolves around eliminating edges that cross over each other in the 
route. The nearest neighbor algorithm does not do any sort of analysis of the route other than finding the closest 
address to the current address. 

(Lysecky, R., & Vahid, F. (2018, June). C950: # Data Structures and Algorithms II. zyBooks.
https://learn.zybooks.com/zybook/WGUC950Template2023)
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
Another thing I would change is simply the organization of the code. I would move all functions into the Functions.py
file to improve organization. The current setup has many functions within the main.py file; this is done so that it is 
clear what functions are used in the nearest neighbor algorithm. However, moving these functions into another file and 
calling them from main.py would lead to cleaner code.

H:
The hash table data structure that I used in this program meets all requirements for this scenario. It does not use an 
additional libraries or classes, and it has an insert function that takes package ID as input and uses that as a key 
to insert package information into the hash table at the correct location. The requirements list the package informaiton
that must be stored in the hash table and I accomplished this by storing package objects within the hash table. These
package objects already contain the package information. This allows for much easier access of the package information
during my nearest neighbor algorithm. The hash table that I created also has a look-up function that takes in a package
ID and returns a package object, which contains all the required package information in an easy-to-access format. 

H.1:
Other data structures that I could have used to store package information are a Binary Search Tree (BST) or an AVL tree.

H.1.a:
Unlike a hash table, a BST does not require collision handling because items are stored in a specific order. My hash 
table simply stores items based on their hash value, a BST will store items based on the value of their key relative to
other items. A BST is also more memory efficient than a hash table and will only take up as much memory as needed at 
any given moment. A hash table takes up as much memory as it allocates, even if it only uses a small portion of that
memory. A BST requires pointers certain other nodes, the hash table does not use pointers.  
A BST has an average time complexity of O(log n) for all operations. However, a simple BST does not have height balancing 
properties so this time complexity is not guaranteed. The worst case time complexity of a BST is O(n). The 
average time complexity of a hash table is O(1) and the worst case time complexity is O(n). Therefore, a hash table is 
probably better for this project.

An AVL tree is similar to a BST, but it has a height balance property that keeps the tree balanced to the least possible 
height after any insertion or removal. An AVL tree is different from a hash table in that it does not require collision 
handling, only rearrangement. Another difference is that an AVL tree guarantees O(log n) time complexity in all
operations. This is, however, not better than the average O(1) time complexity that is expected from a hash table. 
This O(1) time assumes perfect hashing and since I use chaining, a for-loop is needed to access data held in the chains.
This can lead to a worst-case time complexity of O(n). The hash table is still likely to be more efficient than an AVL 
tree because it will only have O(n) if the chains get increasingly long. However, having a guaranteed time complexity of
O(log n) may be beneficial in some cases.

(Lysecky, R., & Vahid, F. (2018, June). C950: # Data Structures and Algorithms II. zyBooks.
https://learn.zybooks.com/zybook/WGUC950Template2023)

