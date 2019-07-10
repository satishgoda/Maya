# References

- https://help.autodesk.com/cloudhelp/2018/ENU/Maya-Tech-Docs/CommandsPython/checkBox.html
- https://help.autodesk.com/cloudhelp/2018/ENU/Maya-Tech-Docs/PyMel/generated/classes/pymel.core.uitypes/pymel.core.uitypes.CheckBox.html

# Code

```python
import maya.cmds as cmds

window = cmds.window('window', width=150)
cmds.columnLayout( adjustableColumn=True )
cmds.checkBox( label='One' )
cmds.checkBox( label='Two' )
cmds.checkBox( label='Three' )
cmds.checkBox( label='Four' )
cmds.showWindow( window )
```

```python
import pymel.core as pm

win = pm.window(title="My Window")
layout = pm.columnLayout()
chkBox = pm.checkBox(label="My Checkbox", value=True, parent=layout)
btn = pm.button(label="My Button", parent=layout)

def buttonPressed(*args):
    if chkBox.getValue():
        print "Check box is CHECKED!"
        btn.setLabel("Uncheck")
    else:
        print "Check box is UNCHECKED!"
        btn.setLabel("Check")

btn.setCommand(buttonPressed)
win.show()
```
