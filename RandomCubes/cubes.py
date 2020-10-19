#Tutorial : https://www.youtube.com/watch?v=eXFGeZZbMzQ
import maya.cmds as cmds
import random

#Gets the current cubes and deletes them if we want to run
#this script multiple times.

cubeList = cmds.ls('myCube*')
if len(cubeList) > 0:
    cmds.delete(cubeList)


result = cmds.polyCube(name='myCube#')
print(result)
#polyCube() returns mycube and polycube. Mycube is a tranform node
#which determines where in space it exists. Translation/rotation/scale
#polycube object includes it's actual data structures. Verticies, edges,
#faces and UVs.

transformName = result[0]

#Group all the cubes we create together
instanceGroupName = cmds.group(empty=True, name=transformName + '_instance_grp#')

for i in range(0,100):

    instanceResult = cmds.instance (transformName, name=transformName + '_instance#')

    #add cube to group
    cmds.parent(instanceResult, instanceGroupName)

    #print 'instanceResult: ' + str(instanceResult)

    #MOVE
    x = random.uniform(-10,10)
    y = random.uniform(0,20)
    z = random.uniform(-10,10)
    cmds.move(x,y,z, instanceResult)

    #ROTATE
    xRot = random.uniform(0,360)
    yRot = random.uniform(0,360)
    zRot = random.uniform(0,360)
    cmds.rotate(xRot,yRot,zRot,instanceResult)

    #SIZE CHANGE
    scalingFactor = random.uniform(0.3,1.5)
    cmds.scale(scalingFactor, scalingFactor, scalingFactor, instanceResult)

#hide original cube we transformed
cmds.hide(transformName)

    
