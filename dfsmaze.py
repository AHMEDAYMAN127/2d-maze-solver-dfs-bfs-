import tkinter as tk
from collections import deque
#open txt file with pathing the name then every row in a list in a list
f =open(".txt")
s=f.read()
f.close()
s=s.splitlines()
rows=len(s)
cols=max(len(line) for  line in s)
start,goal=None,None
walls=[]
#walls so we can know if we are going to awall or into a available place 
for i in range(rows):
    cells=[]
    for j in range(cols):
        try:
            if s[i][j]=='A':
                start =(i,j)
                cells.append(False)
            elif s[i][j]=='B':
                goal =(i,j)
                cells.append(False)
            elif s[i][j]==" ":
                cells.append(False)
            else:
                cells.append(True)
        except IndexError:
            cells.append(False)
    walls.append(cells) 
#BFS algoarithm(FIFO) using deque and parent dict          
def BFS(start,goal,walls):
    rows=len(walls)
    cols=max(len(line) for  line in walls)
    visited=set()
    parent={}
    quque=deque()
    quque.append(start)
    visited=set([start])
    direct=[(-1,0),(1,0),(0,-1),(0,1)]
    while quque:
        x,y=quque.popleft()
        if(x,y)==goal:
            path=[]
            cur=goal
            while cur !=start:
                path.append(cur)
                cur=parent[cur]
            path.append(start)
            path.reverse()
            return path
        for dx,dy in direct:
            nx=dx+x
            ny=dy+y
            if 0 <=nx <rows and  0 <=ny <cols and not walls[nx][ny] and (nx,ny) not in visited:
                quque.append((nx,ny))
                parent[(nx,ny)]=(x,y)
                visited.add((nx,ny))
    return None
    
#DFS algoarithm(LIFO) using deque and parent dict
def dfs(start,goal,walls):
    rows=len(walls)
    cols=max(len(line) for  line in walls)
    visited=set()
    parent={}
    stack=deque()
    stack.append(start)
    direct=[(-1,0),(1,0),(0,-1),(0,1)]
    while stack:
        x,y=stack.pop()
        if(x,y)==goal:
            path=[]
            cur=goal
            while cur !=start:
                path.append(cur)
                cur=parent[cur]
            path.append(start)
            path.reverse()
            return path
        if(x,y) in visited:
            continue
        visited.add((x,y))
        for dx,dy in direct:
            nx,ny=x+dx,y+dy
            if 0<= nx <rows and 0 <=ny <cols and not walls[nx][ny] and (nx,ny) not in visited:
                stack.append((nx,ny))
                parent[(nx,ny)]=(x,y)
    return None
    
#simple gui two buttoms  for dfs and bfs with Ai help 
root = tk.Tk()
root.title("Maze Runner")
canvas = tk.Canvas(root, width=800, height=750)
canvas.pack()
CELL_SIZE=min(800//cols,750//rows)

def draw(path=None, step=None):
    canvas.delete("all")
    for i in range(rows):
        for j in range(cols):
            x1, y1 = j*CELL_SIZE, i*CELL_SIZE
            x2, y2 = x1+CELL_SIZE, y1+CELL_SIZE

            color = "white"
            if (i, j) == start:
                color = "green"
            elif (i, j) == goal:
                color = "red"
            elif walls[i][j]:
                color = "black"
            elif path and step is not None and (i,j) in path[:step] and (i,j) not in (start, goal):
                color = "yellow"

            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")
draw()  
def animate(path, step=1):
    if step <= len(path):
        draw(path, step)
        root.after(100, animate, path, step+1)  

def solvedfs():
    path = dfs(start, goal, walls)
    if path:
        # we can change animate and use draw only for fast show or decrease the time 
        animate(path)
def solvebfs():
    path = BFS(start, goal, walls)
    if path:
        animate(path)
     

btn1 = tk.Button(root, text="Solve DFS Step by Step", command=solvedfs)
btn1.pack(side=tk.LEFT)
btn2 = tk.Button(root, text="Solve BFS Step by Step", command=solvebfs)
btn2.pack(side=tk.RIGHT)


root.mainloop()
