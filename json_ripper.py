import collections
import json
import os
import time
from pathlib import PureWindowsPath

some_actors = os.listdir('Clear_Actors')

actors = []

for actor in some_actors:
    with open(PureWindowsPath('Clear_Actors', actor), 'r', encoding='utf-8') as f:
        actors.append(json.load(f))

# for i in range(12):
#     with open(PureWindowsPath('Clear_Actors', some_actors[i]), 'r', encoding='utf-8') as f:
#         actors.append(json.load(f))

# graph = {}
# temp = False
# for i in range(len(actors)):
#     # actors[i]
#     graph[actors[i]['actor_href']] = []
#     for j in range(i+1, len(actors)):
#         for film in actors[i]['films']:
#             if film in actors[j]['films']:
#                 temp = film in actors[j]['films']
#                 # print(actors[j]['actor_name'])
#
# print(graph)
graph = {}
# temp = False
for i in range(len(actors)):
    graph[actors[i]['actor_name']] = set()
    for j in range(len(actors)):
        if actors[j]['actor_name'] != actors[i]['actor_name']:
            for film in actors[i]['films']:
                if film in actors[j]['films']:
                    # temp = film in actors[j]['films']
                    graph[actors[i]['actor_name']].add(actors[j]['actor_name'])


#
# print(graph)

def dfs_paths(graph_, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next_ in graph_[vertex].difference(set(path)):
            if next_ == goal:
                yield path + [next_]
            else:
                stack.append((next_, path + [next_]))


def bfs(graph_, root_1, root_2):
    visited, queue = set(), collections.deque([root_1])
    visited.add(root_1)
    previous = {}
    while queue:
        vertex = queue.popleft()
        for neighbour in graph_[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                previous[neighbour] = vertex
                if neighbour == root_2:
                    return previous

    return {}


root_1 = actors[1]['actor_name']
root_2 = actors[39]['actor_name']
t1 = time.time()
bfs_graph = bfs(graph, root_1, root_2)
t2 = time.time()
print(t2 - t1)
print(root_1)
print(root_2)
# print(bfs_graph, )

# for key in bfs_graph:
#     root =
temp = True
root = bfs_graph[root_2]
ls = [root_2]
while temp:
    ls.append(root)
    root = bfs_graph[root]

    temp = root_1 != root

ls.append(root_1)
ls.reverse()
print(ls)
