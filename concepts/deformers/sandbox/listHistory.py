import pymel.core as pm

transform = pm.selected()[0]

shape = transform.getShape()

shape.listHistory(interestLevel=0)

shape.listHistory(interestLevel=2, breadthFirst=True)

shape.listHistory(breadthFirst=True, type='geometryFilter')

shape.listHistory(breadthFirst=True, type='groupParts')

shape.listHistory(breadthFirst=True, type='shape')

shape.listHistory(breadthFirst=False, type='shape')
