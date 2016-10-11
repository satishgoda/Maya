class ViewportIsolateSelectAction(QtGui.QAction):
    def __init__(self, *args, **kwargs):
        super(ViewportIsolateSelectAction, self).__init__(*args, **kwargs)
        text = "Exit" if self.getCurrentState() else "Enter"
        self.setText("{0} Isolate Select Mode".format(text))
        self.triggered.connect(self.execute)
    
    def execute(self):
        melState = "false" if self.getCurrentState() else "true"
        pm.mel.eval("enableIsolateSelect {0} {1}".format("modelPanel4", melState))        
    
    def getCurrentState(self):
        return pm.isolateSelect('modelPanel4', query=True, state=True)
