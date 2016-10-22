import maya.api.OpenMaya as om
oset = pm.sets(name='combined')
# Only look for sets with vertices
all(map(lambda member: isinstance(member, pm.MeshVertex), oset.members()))
setName = oset.name()
members = []
for member in oset.members():
    name = member.node().name()
    indices = member.indices()
    members.append((name, indices))
#pm.select('combined') # Selects the vertices
pm.select('combined', ne=True)
pm.delete()
for name, indices in members:
    for index in indices:
        pm.select('{0}.vtx[{1}]'.format(name, index), add=True)
pm.sets(name=setName)
pm.select(deselect=True)
pm.select(setName)
pm.select(setName, ne=True)
#ss = pm.nt.SelectionSet(pm.selected())
pm.select('combined')
slist = om.MGlobal.getActiveSelectionList()
selStrings = slist.getSelectionStrings()
pm.select(selStrings)
pm.select(deselect=True)
vtx_sets = pm.ls(regex="*_vtx_set", type='objectSet')
serialize = []

for vtx_set in vtx_sets:
    if not all(map(lambda member: isinstance(member, pm.MeshVertex), vtx_set.members())):
        print vtx_set, "should only contain vertices"
        print vtx_set.asSelectionSet().getSelectionStrings()
        continue
    sset = vtx_set.asSelectionSet()
    selStrings = sset.getSelectionStrings()
    serialize.append((vtx_set.name(), selStrings))

for vtx_set in vtx_sets:
    pm.select(vtx_set, replace=True)
    slist = om.MGlobal.getActiveSelectionList()
    selStrings = slist.getSelectionStrings()
    serialize.append((vtx_set.name(), selStrings))
pm.select(deselect=True)
for vtx_set_name, selstrings in serialize:
    pm.select(selstrings, replace=True)
    pm.sets(name=vtx_set_name)
pm.select(deselect=True)
