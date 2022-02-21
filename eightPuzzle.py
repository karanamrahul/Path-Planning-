
import numpy as np
from queue_ds import Queue
import pprint
from tqdm import tqdm 



actions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

def is_legal_pos(input_state,i,j):
        num_rows = len(input_state)
        num_cols = len(input_state[0])
        return 0 <= i < num_rows and 0 <= j < num_cols 



def is_solvable(input_state):
    input_state=input_state.flatten()
    count = 0
    for i in range(0,9):
        for j in range(i+1,9):
            if input_state[j] != 0 and input_state[i] != 0 and input_state[i] > input_state[j]:
                count+=1
    return count % 2 == 0

def get_path(dict_path, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = dict_path[current]
    path.append(start)
    path.reverse()
    return path

def get_input_state():
    print("******Goal State*****")
    pprint.pprint(goal)
    a=input("Enter your eight puzzle numbers from 0-8 Example:410256378 column-wise \n")
    b=[int(i) for i in a]
    b=np.asarray(b).reshape((3,3)).T
    if is_solvable(b) or True:
        print("Input Array :\n ",b)
        return b
    else:
        print("[WARNING] Please change your matrix, this puzzle is insolvable")
  

def get_blank_pos(state):
        return np.argwhere(state == 0)[0]

def gen_nodes_info(predecessors,path_dict):
    node_dict={}
    for node_index,node in enumerate(predecessors):
        node_dict[tuple(node)] =  node_index+1

    path=get_path(path_dict,tuple(input_state.T.flatten()),tuple(goal.flatten()))
    print("Child Node:--> 0 --> Parent Node: root")
    for l in path[1:]:
        print("Child Node:-->",node_dict[l],"-->","Parent Node:",node_dict[path_dict[l]])


def gen_nodesinfo(predecessors,path_dict):
    result='Node_index\t Parent_Node_index'
    result+="\n0\troot"
    node_dict={}
    for node_index,node in enumerate(predecessors):
        node_dict[tuple(node)] =  node_index+1

    path=get_path(path_dict,tuple(input_state.T.flatten()),tuple(goal.flatten()))
    for l in path[1:]:
        result +="\n"+str(node_dict[l])+"\t\t\t"+str(node_dict[path_dict[l]])
    return result

def ActionMove(currentNode,state,predecessors):
        result=[]
        i,j=get_blank_pos(state)
        for action in ['left','right','up','down']:

                new_state=state.copy()
                row_offset, col_offset = actions[action]

                if is_legal_pos(state,i + row_offset, j + col_offset):
                    newNode = new_state[i + row_offset][ j + col_offset]
                    new_state[i,j],new_state[i + row_offset][ j + col_offset] = newNode,currentNode
                    if  list(new_state.flatten()) not in predecessors:
                        result.append((new_state))
        return result


q = Queue()

#input_state = np.array([[1,4,7],[5,0,8],[2,3,6]])  # Input-3 Test-Case:1
#input_state = np.array([[4,7,0],[1,2,8],[3,5,6]])  # Input-2 Test-Case:2
#input_state = np.array([[4,0,7],[1,2,5],[3,6,8]])  # Input-1
#input_state=np.array([[3,7,1],[0,8,2],[5,6,4]])    # Input-5
#input_state=np.array([[8,2,3],[6,5,0],[7,4,1]])    # Input-4


def bfs(input_state,goal):
    
    q.enqueue(input_state.T)
    predecessors=[]
    path_dict = {tuple(input_state.flatten()): 0 }
    counter=0
    while not q.is_empty():

            inp= q.dequeue()
            
            if(list(inp.flatten()) == list(goal.flatten())):
                predecessors.append(list(inp.flatten()))
                print("[INFO]  Puzzle Solved ")
                print(inp.T)
                print("*************************")
                print("         PATH            ")
                print("   Start --> Goal       ")
                print("***********************\n")
                print("Start-->",get_path(path_dict,tuple(input_state.T.flatten()),tuple(goal.flatten())),"-->Goal")
                break

            result=ActionMove(0,inp,predecessors)
            predecessors.append(list(inp.flatten()))
            for val in result:
                    q.enqueue(val)
                    counter+=1
                    print("iteration:",counter)
                    path_dict[tuple(val.flatten())] = tuple(inp.flatten())                

    gen_nodes_info(predecessors,path_dict)


    def write_file(filename,content):
        with open(filename,'w') as f:
            f.write(content)



        
    res = ''
    for x in range (len(predecessors)):
        res+=' '.join(map(str, predecessors[x]))+'\n'
    write_file('Nodes.txt',res)



    res=''
    shor_path=get_path(path_dict,tuple(input_state.T.flatten()),tuple(goal.flatten()))
    for x in range (len(shor_path)):
        res+=' '.join(map(str, shor_path[x]))+'\n'
    write_file('nodePath.txt',res)

    result=gen_nodesinfo(predecessors,path_dict)
    print(result)
    write_file('NodesInfo.txt',result)

goal=np.array([[1,4,7],[2,5,8],[3,6,0]])
input_state=get_input_state()

bfs(input_state,goal)
goal=np.array([[1,8,7],[2,0,6],[3,4,5]])
input_state=get_input_state()

bfs(input_state,goal)