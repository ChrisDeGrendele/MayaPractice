#Tutorial followed from: https://www.youtube.com/watch?v=HKBegv3iDsQ

import maya.cmds as cmds
import random

# Get selected object

#Lists things that are selected.
selected_object = cmds.ls(selection=True)


#Get vertex position

vertex_position = []
new_vertex_positions = []

selected_vertices = cmds.ls(selected_object[0]+'.vtx[*]', flatten=True)
vertex_count = cmds.polyEvaluate(selected_object, vertex=True)

print(selected_vertices)

for vertex in selected_vertices:
    vertex_position.append(cmds.pointPosition(vertex))


#Randomize Vertex Positions

for vertex in vertex_position:
    x_rand = random.uniform(-0.02, 0.02)
    y_rand = random.uniform(-0.02, 0.02)
    z_rand = random.uniform(-0.02, 0.02)

    new_x = vertex[0] + x_rand
    new_y = vertex[1] + y_rand
    new_z = vertex[2] + z_rand
    
    new_vertex_positions.append([new_x, new_y, new_z])
    

#Assign new vertex positions
for i in range(vertex_count):
    cmds.xform(selected_vertices[i], translation=new_vertex_positions[i], worldSpace=True)

