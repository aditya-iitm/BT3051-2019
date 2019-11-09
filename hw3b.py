#Header Information

def maze(MazeMatrix,start,finish):
    #MazeMatrix is a binary matrix (2D list of lists)
    #start & finish are tuples containing the starting and finishing point indices e.MazeGraph. (1,1) & (5,5)
    
    #import statements, function body
    
    def MazeMatrix2Graph(MazeMatrix):
        #MazeMatrix is a binary matrix (2D list of lists)
        MazeGraph =nx.Graph()
        length, breadth = len(MazeMatrix), len(MazeMatrix[0])
        maze = [x+[0] for x in MazeMatrix] + [[0]*(breadth+1)]
        for i in range(length):
            for j in range(breadth):
                if maze[i][j] == 1 and maze[i][j+1] == 1:
                    MazeGraph.add_edge((i,j),(i,j+1))
                if maze[i][j] == 1 and maze[i+1][j] == 1:
                    MazeGraph.add_edge((i,j),(i+1,j))
                
        return MazeGraph #a networkx graph whose nodes represent the '1's in the input matrix. node labels are tuples.
    
    def MazeAnswerBFS(MazeGraph,start,finish):
        #MazeGraph is a networkx graph 
        bfsList = [start]
        path = [end]
        tracker = {}
        for i in range(len(MazeGraph)):

            if end in bfsList:
                break
            else:
                temp = [n for n in list(MazeGraph[bfsList[i]]) if n not in bfsList]
                bfsList += temp
                for each in temp:
                    tracker[each] = bfsList[i]
        while path[-1] != start:
                path.append(tracker[path[-1]])

        shortest_path = list(reversed(path))
                
        return shortest_path #list of tuples containing indices of the points in the answer
    
    def MazeComponentsDFS(MazeGraph):
        #MazeGraph is a networkx graph
        
        #function body  
        
        return components #list of lists, each containing tuples of the indices of points in that component
    
    #function body
    
    print(a)
    print('\n')
    print(b)
    #a is the output of MazeAnswerBFS and b is the output of MazeComponentsDFS

if __name__ == '__main__':
    #DO NOT MODIFY THE FOLLOWING
    hw3bmaze=    [[1,0,1,1,0,1],
                  [1,1,0,0,0,0],
                  [0,1,0,1,1,1],
                  [0,1,1,1,0,1],
                  [1,0,0,1,1,1],
                  [1,1,0,0,0,1],
                  [0,0,1,1,0,1]]
    
    hw3bstart=(0,0)
    hw3bfinish=(6,5)
    print(maze(hw3bmaze,hw3bstart,hw3bfinish))
    
#output for this example should be:
#[(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5), (6, 5)]
#[[(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5), (6, 5), (3, 5), (2, 5), (2, 4), (2, 3)], [(0, 2), (0, 3)], [(0, 5)], [(4, 0), (5, 0), (5, 1)], [(6, 2), (6, 3)]]
