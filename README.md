# Path-Planning-
8-Puzzle Solver using BFS


8-Puzzle Problem

Install the following python packages
```
$ pip3 install pprint
$ pip3 install tqdm
$ pip3 install numpy
```
Steps to run
```
$ cd Path-Planning-8-puzzle/code
$ python3 eightPuzzle.py
```
(Please enter the input on the terminal after the following prompt:)

```
******Goal State*****
array([[1, 4, 7],
       [2, 5, 8],
       [3, 6, 0]])
```
Enter your eight puzzle numbers from 0-8 Example: 147508236 column-wise 


```
(The matrix for the above example will look like this)
1 5 2
4 0 3
7 8 6
```

```
******Goal State*****
array([[1, 8, 7],
       [2, 0, 6],
       [3, 4, 5]])
```
Enter your eight puzzle numbers from 0-8 Example: 217860345 column-wise


```
(The matrix for the above example will look like this)
2 8 3
1 6 4
7 0 5
```


"Visualization is only shown for the second goal state as the files are overwritten "

To Visualize the puzzle
```
$ python3 plot_path.py

```
