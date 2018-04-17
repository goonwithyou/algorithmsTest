# @Time    : 2018/4/17 10:03
# @Author  : cap
# @FileName: graph.py
# @Software: PyCharm Community Edition


class Node(object):
    """定义节点信息"""
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):
    """定义边信息,src和dest 为node对象"""
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()


class WeightedEdge(Edge):
    """定义边权重信息"""
    def __init__(self, src, dest, weight=1.0):
        self.src = src
        self.dest = dest
        self.weight = weight

    def getWeight(self):
        return self.weight

    def __str__(self):
        return self.src.getName() + '->(' + str(self.weight) + ')' + self.dest.getDestination()


class Digraph(object):
    """定义图信息，
    nodes为所有的节点表
    edge的key值为边的初始节点，value为列表，其值为边的所有子节点
    """
    def __init__(self):
        self.nodes = []
        self.edge = {}

    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplited node')
        else:
            self.nodes.append(node)
            self.edge[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in nodes!')
        self.edge[src].append(dest)

    def childrenOf(self, node):
        return self.edge[node]

    def hasNode(self, node):
        return node in self.nodes

    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.edge[src]:
                result = result + src.getName() + '->' + dest.getName() + '\n'
        return result[:-1]


class Graph(Digraph):
    """覆盖父类的addEge方法，添加双向边"""
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph(self, rev)


def printPath(path):
    """path为节点列表"""
    result = ""
    for p in path:
        result = result + str(p) + '->'
    return result[:-2]

def DFS(graph, start, end, path, shortest, toPrint=False):
    path = path + [start]
    if toPrint:
        print('Current DFS path:', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                if newPath != None:
                    shortest = newPath
    return shortest

def shortestPath(graph, start, end, toPrint=False):
    return DFS(graph, start, end, [], None, toPrint)

def BFS(graph, start, end, toPrint=False):
    initPath = [start]
    pathQueue = [initPath]
    if toPrint:
        print('Current BFS init path:', printPath(initPath))
    while len(pathQueue) != 0:
        tmpPath = pathQueue.pop(0)
        print('Current BFS path:', printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None

def testSP():
    nodes = []
    for name in range(6):
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0], nodes[1]))
    g.addEdge(Edge(nodes[1], nodes[2]))
    g.addEdge(Edge(nodes[2], nodes[3]))
    g.addEdge(Edge(nodes[2], nodes[4]))
    g.addEdge(Edge(nodes[3], nodes[4]))
    g.addEdge(Edge(nodes[3], nodes[5]))
    g.addEdge(Edge(nodes[0], nodes[2]))
    g.addEdge(Edge(nodes[1], nodes[0]))
    g.addEdge(Edge(nodes[3], nodes[1]))
    g.addEdge(Edge(nodes[4], nodes[0]))
    sp = shortestPath(g, nodes[0], nodes[5], toPrint=True)
    print('Shortest path is:', printPath(sp))

    BFS(g, nodes[0], nodes[5], toPrint=True)
