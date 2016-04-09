import maya.cmds as cmds

window = cmds.window( widthHeight=(400, 300) )
cmds.paneLayout()

activeList = cmds.selectionConnection( activeList=True )
cmds.spreadSheetEditor( mainListConnection=activeList )

cmds.showWindow( window )
