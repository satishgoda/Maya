"""
Comment Or Uncomment selected text in the ScriptEditor panel's text editor
"""

class Source(object):
    def __init__(self, text):
        self.lines = text.split('\n')

class SourceLineOp(object):
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return partial(instance, self.execute)
        
    def execute(self, line):
        raise NotImplementedError("Subclasses must implement this operation")

class CommentLineOp(SourceLineOp):
    def execute(self, line):
        return "#" + line

class UncommentLineOp(SourceLineOp):
    def execute(self, line):
        return line[1:] if line.startswith('#') else line

class ScriptEditor(object):
    comment = CommentLineOp()
    uncomment = UncommentLineOp()

    def __init__(self):
        self._editor = pm.mel.eval("$temp=$gLastFocusedCommandExecuter")
    
    @property
    def editor(self):
        return pm.ui.CmdScrollFieldExecuter(self._editor)

    def getSelectedSource(self):
        return Source(self.editor.getSelectedText())
 
    def replaceSelection(self, text):
        self.editor.insertText(text)
 
    def __call__(self, operation):
        source = self.getSelectedSource()
        for index, line in enumerate(source.lines):
            source.lines[index] = operation(line)
        self.replaceSelection("\n".join(source.lines))

se = ScriptEditor()
se.comment()
se.uncomment()
