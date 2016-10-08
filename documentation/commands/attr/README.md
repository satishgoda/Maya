```python
cmds.addAttr(newSet.name(), ln='QColor', dt='string')
color = QtGui.QColor(newitem.color)
newSet.attr('QColor').set(color.name(), type='string')

cmds.addAttr(newSet.name(), ln='ctime')
ctime = newSet.attr('ctime')
ctime.set(time.time())
ctime.lock()
```
