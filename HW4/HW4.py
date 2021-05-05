


N=[{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents":
["A"]}, {"name": "A", "parents": []}, {"name": "D", "parents":["C",
"F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]


res={}
visited = set()
childs=[]

def make_tree(data):
    for i in data:
        parents=i.values()[0]
        child=i.values()[1]
        for k in parents:
            try:
                res[k].append(child)
            except:
                res[k] = []
                res[k].append(child)


def dfs(visited, graph, node,childs):
    if node not in visited:
        visited.add(node)
        childs.append(node)
        try:
            for neighbour in graph[node]:
                dfs(visited, graph, neighbour, childs)
        except:
            pass


make_tree(N)

nodes=[]

for j in N:
   nodes.append(j.values()[1])
nodes.sort()

for j in nodes:
    node=j
    dfs(visited, res, node,childs)
    print(node+":"+str(len(childs)))
    childs=[]
    visited=set()


