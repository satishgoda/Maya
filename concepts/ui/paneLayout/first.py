import maya.cmds as cmds

window = cmds.window()

pl = cmds.paneLayout( configuration='horizontal2' )

cmds.button()

cl = cmds.columnLayout()
b1 = cmds.button()
b2 = cmds.button()
b3 = cmds.button()

cmds.showWindow()

cmds.deleteUI(cl)

cl = cmds.columnLayout(parent=pl)
b1 = cmds.button(parent=cl)
b2 = cmds.button(parent=cl)
b3 = cmds.button(parent=cl)
