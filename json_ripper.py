import collections
import json
import os
from pathlib import PureWindowsPath

some_actors = os.listdir('Clear_Actors')

actors = []

for actor in some_actors:
    with open(PureWindowsPath('Clear_Actors', actor), 'r', encoding='utf-8') as f:
        actors.append(json.load(f))

# for i in range(50):
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


bfs_graph = bfs(graph, actors[1]['actor_name'], actors[39]['actor_name'])
print(actors[1]['actor_name'])
print(actors[39]['actor_name'])

print(bfs_graph, )
# print(len(bfs_graph))
