from PIL import Image, ImageDraw
import numpy as np
import cv2 

i = 0
imgprefix = "dijkstra"
NODESIZE = 16
LINESIZE = 5


def drawGraph(V,E):
    base = Image.new('RGBA', (1000,1000), (255,255,255,1))
    draw = ImageDraw.ImageDraw(base)

    for (u,v) in E:
        p1 = u.x, u.y
        p2 = v.x, v.y
        draw.line([p1,p2], (0,0,0), width=LINESIZE)

    for u in V[1:-1]:
        x1, x2 = u.x - (NODESIZE/2), u.x + (NODESIZE/2)
        y1, y2 = u.y - (NODESIZE/2), u.y + (NODESIZE/2)
        draw.ellipse(
            [(x1,y1), (x2,y2)],
            fill=(255,0,0)
            )
    for u in (V[0], V[-1]):
        x1, x2 = u.x - (NODESIZE/2), u.x + (NODESIZE/2)
        y1, y2 = u.y - (NODESIZE/2), u.y + (NODESIZE/2)
        draw.ellipse(
            [(x1,y1), (x2,y2)],
            fill=(0,255,0)
            )
    base.show()

def drawDijkstraGraph(V,E,path, active=None):
    """ Let path = [node,node,node...] """
    base = Image.new('RGBA', (1000,1000), (255,255,255,1))
    draw = ImageDraw.ImageDraw(base)

    for (u,v) in E:
        p1 = u.x, u.y
        p2 = v.x, v.y
        draw.line([p1,p2], (0,0,0), width=LINESIZE)

    for i in range(1, len(path)):
        u = path[i]
        v = path[i-1]
        p1 = u.x, u.y
        p2 = v.x, v.y
        draw.line([p1,p2], (0,0,255), width=LINESIZE)
    if active:
        p1 = active[0].x, active[0].y
        p2 = active[1].x, active[1].y
        draw.line([p1,p2], (255,0,255), width=LINESIZE)



    for u in V[1:-1]:
        x1, x2 = u.x - (NODESIZE/2), u.x + (NODESIZE/2)
        y1, y2 = u.y - (NODESIZE/2), u.y + (NODESIZE/2)
        draw.ellipse(
            [(x1,y1), (x2,y2)],
            fill=(255,0,0)
            )
    for u in (V[0], V[-1]):
        x1, x2 = u.x - (NODESIZE/2), u.x + (NODESIZE/2)
        y1, y2 = u.y - (NODESIZE/2), u.y + (NODESIZE/2)
        draw.ellipse(
            [(x1,y1), (x2,y2)],
            fill=(0,255,0)
            )
        
    # base.show()
    img = np.array(base)
    cv2.imshow("graph", img)
    cv2.waitKey(300)

