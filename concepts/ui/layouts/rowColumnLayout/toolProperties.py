import maya.cmds as cmds

try:
    cmds.deleteUI(propsWindow)
except Exception as e:
    print e

tool = createCylinder

propsWindow = cmds.window(title=tool.name)

cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 0), columnWidth=[(1, 100), (2, 250)] )

propsUI = []
for prop in tool.properties:
    cmds.text(label=prop.capitalize())
    propUI = cmds.textField()
    propsUI.append(propUI)

def executeTool(tool, propsWindow, propsUI):
    def _doExec(incoming):
        values = []
        for propName, propUI in zip(tool.properties, propsUI):
            propValue = cmds.textField(propUI, query=True, text=True)
            values.append(propValue)
        tool.execute(values)
        cmds.deleteUI(propsWindow)
    return _doExec

execButton = cmds.button(label='execute', command=executeTool(tool, propsWindow, propsUI))

cmds.showWindow(propsWindow)
