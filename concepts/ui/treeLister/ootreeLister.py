import maya.cmds as cmds

class CommandEditQueryMixin(object):
    def initWith(self, **kwargs):
        for attr, value in kwargs.iteritems():
            self.__dict__[attr] = value

    def __getattr__(self, name):
        kwargs = {name: True}
        return self.command(self.wid, query=True, **kwargs)

    def __setattr__(self, name, value):
        kwargs = {name: value}
        self.command(self.wid, edit=True, **kwargs)    

class TreeLister(CommandEditQueryMixin):
    """cmds.treeLister"""
    command = cmds.treeLister
    def __new__(cls, *args, **kwargs):
        kwargs['wid'] = cmds.treeLister()
        self = super(cls, cls).__new__(cls)
        self.initWith(**kwargs)
        return self

class TreeListWindow(CommandEditQueryMixin):
    command = cmds.window
    def __new__(cls, *args, **kwargs):
        kwargs['wid'] = cmds.window(width=300)
        kwargs['form'] = cmds.formLayout()
        kwargs['treeLister'] = TreeLister()
        self = super(cls, cls).__new__(cls)
        self.initWith(**kwargs)
        return self
    
    def __init__(self):
        tl = self.treeLister.wid
        cmds.formLayout(self.form, edit=True, 
                        af = ((tl, 'top', 0), (tl, 'left', 0), (tl, 'bottom', 0), (tl, 'right', 0)))
    def show(self):
        cmds.showWindow(self.wid)
