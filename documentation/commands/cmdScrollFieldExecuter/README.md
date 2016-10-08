http://help.autodesk.com/cloudhelp/2016/ENU/Maya-Tech-Docs/CommandsPython/cmdScrollFieldExecuter.html

```python
gLastFocusedCommandExecuter = eval("$temp=$gLastFocusedCommandExecuter")
cmds.cmdScrollFieldExecuter(gLastFocusedCommandExecuter, edit=True, insertText="Huh\n")
cmds.cmdScrollFieldExecuter(gLastFocusedCommandExecuter, edit=True, appendText="Oh Yeah\n")
```
