g, ip, isg, r = pm.ls(type='shadingEngine')

g.members()

r.members()

pm.select(clear=True)

pm.select(g.members())
pm.select(r.members(), add=True)

pm.select(clear=True)

g.inputs(type='shape')

r.inputs(type='shape')

r.asSelectionSet()

ss = g.asSelectionSet()

ss.getSelectionStrings()

os = ss.asObjectSet()

os.rename('greenSet')

pm.select(os)
