try:
    from PySide.QtGui import QWidget, QScrollArea, QLabel, QLineEdit
    from PySide.QtGui import QVBoxLayout, QHBoxLayout, QCheckBox
    from collections import OrderedDict
    
    import pymel.core as pm
    
    class CommandFlag(object):
        def __init__(self):
            self.longName = ''
            self.shortName = ''
            self.type = ''
            self.modes = ''
            self.description = ''
    
    class Command(object):
        def __init__(self, command):
            self.command = command
            self.description = ""
            self.flags = OrderedDict()
            self.modes = {'create': [], 'query': [], 'edit': [], 'undefined': []}
            self.derivedFrom = ''
        
        def addFlag(self, flag, buffer):
            flag.description = "\n".join(buffer)
            flag.longName = flag.longName.strip()
            self.flags[flag.longName] = flag
            if flag.modes:
                for mode in flag.modes:
                    self.modes[mode].append(flag.longName)
            else:
                self.modes['undefined'].append(flag.longName)
        
        @property
        def name(self):
            return self.command.__name__
    
    class CommandDocsParser(object):
        @classmethod
        def parse(cls, pymelcommand):
            buffer = []
            flag = None
            mode = 'description'
            command = Command(pymelcommand)
            
            docs = pymelcommand.__doc__
            
            if docs is None:
                raise Warning("No documentation exists")
                
            for line in map(str.strip, docs.splitlines()):
                if line.startswith('Flags'):
                    mode = 'flags'
                    command.description = "\n".join(buffer)
                    buffer = []
                elif mode == 'flags' and line.startswith('- '):
                    if flag is not None:
                        command.addFlag(flag, buffer)
                        buffer = []
                    flag = CommandFlag()
                    flag.longName, _, rest = line.partition(' ')[-1].partition(':')
                    flag.shortName, _, rest = rest.strip().partition(' ')
                    flag.type, _, modes = rest.strip().rpartition(' ')
                    modes = modes.strip('[]')
                    flag.modes = modes.split(',') if modes else None
                elif line.startswith('Derived from'):
                    command.addFlag(flag, buffer)
                    buffer = [line]
                    flag = None
                else:
                    buffer.append(line)
            
            command.derivedFrom = '\n'.join(buffer)
            
            return command
    
    
    class CommandDocsWidget(QScrollArea):
        def __init__(self, command, parent=None):
            super(CommandDocsWidget, self).__init__(parent)
            self.command = CommandDocsParser.parse(command)
            self._setupUi()
    
        def _setupUi(self):
            self.setWidgetResizable(True)
            
            self.docsWidget = QWidget()
            docsLayout = QVBoxLayout()
            self.docsWidget.setLayout(docsLayout)

            lblCmdName = QLabel("<h1>{0}</h1>".format(self.command.name))
            docsLayout.addWidget(lblCmdName)
            
            lblDesc = QLabel(self.command.description)
            docsLayout.addWidget(lblDesc)

            self.flagsWidget = QWidget()
            self.flagsWidget.setLayout(QVBoxLayout())
            docsLayout.addWidget(self.flagsWidget)
    
            self.setWidget(self.docsWidget)
            
            self.refreshDocs()
            
        def refreshDocs(self, modes=None):
            if modes:
                docsLayout = self.docsWidget.layout()
                docsLayout.removeWidget(self.flagsWidget)
                self.flagsWidget.hide()
                self.flagsWidget.deleteLater()
                self.flagsWidget = QWidget()
                self.flagsWidget.setLayout(QVBoxLayout())
                docsLayout.addWidget(self.flagsWidget)
                flags = []
                for mode in modes:
                    for name in self.command.modes[mode]:
                        flags.append(self.command.flags[name])
            else:
                flags = self.command.flags.values()
                docsLayout = self.docsWidget.layout()
                docsLayout.removeWidget(self.flagsWidget)
                self.flagsWidget.hide()
                self.flagsWidget.deleteLater()
                self.flagsWidget = QWidget()
                self.flagsWidget.setLayout(QVBoxLayout())
                docsLayout.addWidget(self.flagsWidget)

            flagsLayout = self.flagsWidget.layout()
            
            for flag in flags:
                lblFlag = QLabel("<h2>{0.longName} - {0.shortName} - {0.type}</h2>".format(flag))
                flagsLayout.addWidget(lblFlag)
                lblModes = QLabel("{0}".format(', '.join(flag.modes) if flag.modes else "Undefined"))
                flagsLayout.addWidget(lblModes)
                lblFlagDesc = QLabel(flag.description)
                flagsLayout.addWidget(lblFlagDesc)
        
    
    class CommandDocsDemoWidget(QWidget):
        def __init__(self, command=None, parent=None):
            super(CommandDocsDemoWidget, self).__init__(parent)
            self.commandDocsWidget = None
            self.command = command
            self.lastcommand = ''
            self._setupUi()
            self._setupSignals()
    
        def _setupUi(self):
            self.setMinimumWidth(800)
            self.setMinimumHeight(600)
            
            layout = QVBoxLayout()
            self.setLayout(layout)
    
            self.editPmCmd = QLineEdit()
            layout.addWidget(self.editPmCmd)
            
            self.modesWidget = QWidget()
            self.modesLayout = QHBoxLayout()
            self.modesWidget.setLayout(self.modesLayout)
            layout.addWidget(self.modesWidget)
            
            self.checkBoxes = []
            for mode in 'create query edit'.split():
                chkBox = QCheckBox(mode)
                chkBox.setProperty('mode', mode)
                self.checkBoxes.append(chkBox)

            for checkBox in self.checkBoxes:
                self.modesLayout.addWidget(checkBox)
                checkBox.setChecked(True)

            if self.command:
                self.updateDocs()
            else:
                layout.addStretch()
    
        def _setupSignals(self):
            self.editPmCmd.editingFinished.connect(self.generateDocs)
            for checkBox in self.checkBoxes:
                checkBox.stateChanged.connect(self.filterDocs)
    
        def generateDocs(self):
            commandstring = self.editPmCmd.text().strip()
            
            if not commandstring or commandstring == self.lastcommand:
                return
            
            self.lastcommand = commandstring
    
            try:
                self.command = eval("pm.{0}".format(commandstring))
                self.updateDocs()
            except Exception as e:
                print e

        def filterDocs(self, state):
            """Display the flags for the modes chosen."""
            self.modes = []
            
            for checkBox in self.checkBoxes:
                mode = checkBox.property('mode')
                if checkBox.isChecked():
                    self.modes.append(mode)
            
            if self.commandDocsWidget:
                self.commandDocsWidget.refreshDocs(self.modes)
    
        def updateDocs(self):
            layout = self.layout()
            
            if self.commandDocsWidget:
                layout.removeWidget(self.commandDocsWidget)
                self.commandDocsWidget.deleteLater()
            else:
                item = layout.takeAt(2)
                
                if item:
                    del item
            
            try:
                self.commandDocsWidget = CommandDocsWidget(self.command)
                layout.addWidget(self.commandDocsWidget)
            except Exception as e:
                self.commandDocsWidget = None
                layout.addStretch()
                print e

    cdw = CommandDocsDemoWidget()
    cdw.show()
except Exception as e:
    import traceback
    traceback.print_exc()
