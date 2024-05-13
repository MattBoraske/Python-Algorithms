```html
ALGORITHM          MST   SSSP   APSP   Greedy   DFS   BFS   DP  Union-Find   PQueue   SCC  Runtime
Djikstra's                X             X              X                      X             O((V+E)log(V))
Bellman-Ford              X                            X                                    O(VE)
Topological Sort                                 X                                          O(V+E)
Kruskal's           X                   X                        X            X             O(Elog(E))
Primm's             X                   X                                     X             O(Elog(V))  
Kosaraju's                                       X                                     X    O(V+E)
Floyd Warshall                   X                           X                              O(n^3)
0/1 Knapsack                                                 X                              O(nW) where W = capacity
Fractional Knapsack                     X                                     X             O(nlog(n))
Optimal Merge                           X                                     X             O(nlog(n))
Job Sequencing                          X                                                   O(nlog(n)) using sorting
```
