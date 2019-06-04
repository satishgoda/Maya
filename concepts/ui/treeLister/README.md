# What is treeLister?

treeLsiter is a Maya Python Commands command and it creates/edits/queries the tree lister control. 

More documentation is available at http://help.autodesk.com/cloudhelp/2018/ENU/Maya-Tech-Docs/CommandsPython/treeLister.html


# Wrapper

I have written a simple wrapper that lets me create treeLister widgets easily.


# API Usage
```python

tlw = TreeListWindow()
tlw.show()

# Adding Items

tlw.treeLister.add = ('Group1/item1', '', cmds.sphere)
tlw.treeLister.add = ('Group1/item2', '', cmds.sphere)

```
