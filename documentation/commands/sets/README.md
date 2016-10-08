```python
ObjectSet = pm.nodetypes.ObjectSet

filter(lambda oset: oset.getAnnotation() == 'someSet' ,pm.ls(sets=True))

oset = pm.selected(type='objectSet')[0]
oset.select()
oset.select(noExpand=True)
```


```
for oset in self.selectionSets:
    oset.setIcon("F:\\sss.png")

for oset in self.selectionSets:
    oset.unlock()
    oset.setAnnotation('sessionSelectionSet')
    oset.lock()
```

```python
selindex = self.setsView.selectedIndexes()[0]
selection = selindex.data(QtCore.Qt.UserRole)
selection._oset.unlock()
manager.removeSet(selection)    
manager.model.removeColumn(selindex.column())
pm.delete(selectionset._oset)
del(selectionset)
```

```python
setsByCreationTime = sorted(self.selectionSets, 
                            key=lambda os: os.attr('ctime').get()
                     )
```
