import pymel.core as pm

t = pm.selected()[0]

s = t.getShape()

s.instanceCount()

s.getAllPaths()

s.getInstances()

s.getParent()

Leaf = pm.PyNode('Leaf')

Leaf.getAllParents()

Leaf.getAllPaths()
