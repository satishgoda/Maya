slayout = pm.scrollLayout('form', childResizable=True)
for name in names:
    flayout = pm.frameLayout(collapsable=True, label=name)
    SC = pm.selectionConnection("{0}SC".format(name), object=selection)
    cb = pm.channelBox( "{0}CB".format(name), mlc=SC, height=175, useManips='standard')
