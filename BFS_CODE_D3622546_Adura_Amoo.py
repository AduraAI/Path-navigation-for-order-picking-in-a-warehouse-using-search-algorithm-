# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 03:35:34 2024

@author: D3622546
"""

from pyamaze import maze,agent,textLabel,COLOR
from collections import deque
from timeit import timeit


def BFS(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    frontier = deque()
    frontier.append(start)
    bfsPath = {}
    explored = [start]
    bSearch=[]

    while len(frontier)>0:
        currCell=frontier.popleft()
        if currCell==m._goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell] = currCell
                bSearch.append(childCell)
    # print(f'{bfsPath}')
    fwdPath={}
    cell=m._goal
    while cell!=(m.rows,m.cols):
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return bSearch,bfsPath,fwdPath

if __name__=='__main__':
   
    m=maze(26,40)
    m.CreateMaze(2,13,pattern='v',theme=COLOR.light,loopPercent=100)
    
    bSearch,bfsPath,fwdPath=BFS(m)
    a=agent(m,footprints=True,color=COLOR.blue,filled=True)
    b=agent(m,footprints=True,color=COLOR.red, filled=False)
    c=agent(m,2,13,footprints=True,color=COLOR.yellow,filled=True,goal=(m.rows,m.cols))
   
            
    m.tracePath({a:bSearch},delay=100)
    m.tracePath({c:bfsPath},delay=100)
    m.tracePath({b:fwdPath},delay=100)
    
    l=textLabel(m,'BFS Path Length',len(fwdPath)+1)
    l=textLabel(m,'BFS Search Length',len(bSearch))
    t=timeit(stmt='BFS(m)',number=1000, globals=globals())
    textLabel(m,'BFS EXECUTION Time',t)

    m.run()