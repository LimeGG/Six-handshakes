import json
import os
from pathlib import PureWindowsPath

some_actors = os.listdir('Clear_Actors')

actors = []

for actor in some_actors:
    with open(PureWindowsPath('Clear_Actors', actor), 'r', encoding='utf-8') as f:
        actors.append(json.load(f))

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
temp = False
for i in range(len(actors)):
    graph[actors[i]['actor_name']] = []
    for j in range(len(actors)):
        if actors[j]['actor_name'] != actors[i]['actor_name']:
            for film in actors[i]['films']:
                if film in actors[j]['films']:
                    temp = film in actors[j]['films']
                    graph[actors[i]['actor_name']].append(actors[j]['actor_name'])


#
# print(graph)

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


print(list(dfs_paths(graph, actors[1]['actor_name'], actors[2]['actor_name']))[0])
