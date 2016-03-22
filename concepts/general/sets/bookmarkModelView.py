MEL = """
select -noExpand `ls -sets`;
sets -query -text;
"""

for oset in cmds.ls(sets=True):
    cmds.select(oset, noExpand=True, replace=True)
    annotation = cmds.sets(query=True, text=True)
    if annotation == 'bookmarkModelView':
        print oset, annotation
