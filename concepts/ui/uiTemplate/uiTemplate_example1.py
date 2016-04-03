import maya.cmds as cmds

if cmds.uiTemplate( 'ExampleTemplate', exists=True ):
	cmds.deleteUI( 'ExampleTemplate', uiTemplate=True )


cmds.uiTemplate('ExampleTemplate')
cmds.frameLayout(defineTemplate='ExampleTemplate', 
                 borderVisible=True, labelVisible=True,
                 collapsable=True, collapse=False)
cmds.button(defineTemplate='ExampleTemplate', width=100, height=15)


window = cmds.window()
cmds.setUITemplate( 'ExampleTemplate', pushTemplate=True)

cmds.columnLayout()

l1 = cmds.frameLayout(label='Numbers', collapse=True)
cmds.columnLayout()

for number in ('One', 'Two', 'Three'):
    cmds.button(label=number)

cmds.setParent( '..' )
cmds.setParent( '..' )

l2 = cmds.frameLayout(label='Colors')
cmds.columnLayout()

for color in ('Red', 'Green', 'Blue'):
    cmds.button(label=color)

cmds.setParent( '..' )
cmds.setParent( '..' )

cmds.setUITemplate( popTemplate=True )


dockControl = cmds.dockControl(content=window, area='left', allowedArea=('right', 'left'))


try:
    cmds.deleteUI(window)
    cmds.deleteUI(dockControl)
except RuntimeError as e:
    print e
