def enableIsolateSelect():
    melState = "false" if pm.isolateSelect('modelPanel4', query=True, state=True) else "true"
    pm.mel.eval("enableIsolateSelect {} {}".format("modelPanel4", melState))

def _onContextMenu(self, pos):
    menu = QtGui.QMenu()
    toggleIsolateSelectAction = menu.addAction("")
    if pm.isolateSelect('modelPanel4', query=True, state=True):
        toggleIsolateSelectAction.setText("Exit Isolate Mode")
    else:
        toggleIsolateSelectAction.setText("Enter Isolate Mode")

    toggleIsolateSelectAction.triggered.connect(enableIsolateSelect)
    
    pos.setY(pos.y()+20)
    menu.exec_(self.mapToGlobal(pos))
