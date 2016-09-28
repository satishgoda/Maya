panel = pm.getPanel(wf=True)

qtpanel = panel.asQtObject()

sew = qtpanel.children()[-1]
sewl = sew.layout()
seww = sewl.itemAt(1).widget()
sewww = seww.children()[-1]

splitter = sewww.children()[1]

splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)

sc = splitter.widget(0)
se = splitter.widget(1)

splitter.insertWidget(0, se)

save = splitter.saveState()
#str(save)

splitter.restoreState(save)

sc = splitter.widget(0)
se = splitter.widget(1)
splitter.insertWidget(0, se)

qtpanel.focusWidget().hide()

fw = qtpanel.focusWidget()

fw.children()[0].hide()
fw.children()[0].show()

fw.children()[3].hide()
fw.children()[3].show()

te = fw.children()[0]

te.hide()
