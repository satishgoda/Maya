import maya.cmds as cmds

cmds.window()

cmds.flowLayout( columnSpacing=10 , wrap=True)

for selection in pm.selected():
    cmds.button(label=selection.name())

cmds.showWindow()
