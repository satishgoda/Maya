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
