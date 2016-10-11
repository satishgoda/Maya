window = pm.ui.Window()
slayout = pm.ui.ScrollLayout(parent=window,
                             childResizable=True)
selected = pm.selected()
for selection in selected:
    flayout = pm.ui.FrameLayout(selection.name(),parent=slayout)
    SCO = "{0}SC".format(selection.name())
    SC = pm.selectionConnection(SCO, object=selection, parent=window)
    cb = pm.ui.ChannelBox("{0}CB".format(selection.name()), mlc=SC,
                        height=175, parent=flayout,
                        useManips='standard')
window.show()

window.delete()
