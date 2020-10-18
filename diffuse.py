from random import choice,random
npart=500                                                       #set to 500
side=21                                                         # Should be an odd number: trial with 21,31,41,51
perc=0                                                          # initialized counter
density = float(input("Pick value of 0 to 1 for density:"))     #density used to pick a value of 0 to 1 for the cells occupying the non-moving sqaures
maxsteps = 10000                                                #the maximum numbers the particle can move to percolate out of grid
steps = [(1,0),(-1,0),(0,1),(0,-1)]
grid=[[0 for x in range(side)] for y in range(side)]

for ipart in range(npart):
    # Start particle at center
    x,y = side//2,side//2
    for a in range(side):
        for b in range(side):
            if density > random():                               #if/ else statement setting cells to 1 if the statement is true if not perform the else
                grid[a][b] = 1
            else:
                grid[a][b] = 0
    # perform the random walk until particle departs
    for step in range(maxsteps):                                 #conversion of while 1 loop to maxsteps
        grid[x][y]=0                                             #Remove particle from current spot
        # Randomly move particle
        sx,sy = choice(steps)
        x += sx
        y += sy
        if x<0 or y<0 or x==side or y==side:
            perc += 1
            break
        if grid[x][y] == 1:
            x -= sx
            y -= sy
            grid[x][y] = 0
            continue
print(perc/npart)
