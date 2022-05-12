def draw_triangle(r):
    for i in range(r):
        print(' '*(r-i-1)+'*'*(2*i+1))

draw_triangle(8)