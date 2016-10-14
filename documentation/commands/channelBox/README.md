```python
torusSC = pm.selectionConnection("torusSC", object="pTorus1")

cmds.window()
cmds.formLayout( 'form')
dave = cmds.channelBox( 'dave', mlc=torusSC)
cmds.formLayout( 'form', e=True, af=(('dave', 'top', 0), ('dave', 'left', 0), ('dave', 'right', 0), ('dave', 'bottom', 0)) )
cmds.showWindow()

cmds.setKeyframe(torusSC, at=cmds.channelBox(dave, query=True, sma=True))
cmds.channelBox(dave, edit=True, fixedAttrList=['tx','ty'])
cmds.channelBox(dave, edit=True, fixedAttrList=[])
```


```python
def refreshCB(cb):
    pm.channelBox(cb, edit=True, fixedAttrList=[], update=True)
pm.channelBox(cbox, edit=True, fixedAttrList=[''], update=True)
pm.cmds.evalDeferred(pm.Callback(refreshCB, cbox))
```
