import pymel.core as pm

leafMeshes = pm.ls(regex='leaf.*', type='mesh')

for leafMesh in leafMeshes:
    print leafMesh.longName()
    for otherInstance in leafMesh.getOtherInstances():
        print "\t", otherInstance.longName()

"""
|Leaves|Leaf1|leaf1
	|Tree|group3|Leaf12|leaf1
	|Tree|group3|Leaf13|leaf1
	|Tree|group3|Leaf14|leaf1
	|Tree|group3|Leaf15|leaf1
|Leaves|Leaf2|leaf2
	|Tree|group2|Leaf8|leaf2
	|Tree|group2|Leaf9|leaf2
	|Tree|group2|Leaf10|leaf2
	|Tree|group2|Leaf11|leaf2
|Leaves|Leaf3|leaf3
	|Tree|group1|Leaf4|leaf3
	|Tree|group1|Leaf5|leaf3
	|Tree|group1|Leaf6|leaf3
	|Tree|group1|Leaf7|leaf3
"""
