pm.ls(references=True)

pm.ls(referencedNodes=True)

pm.ls(regex="*char_rig", referencedNodes=True)

from collections import OrderedDict

class MayaReference(object):
    def __init__(self, mayaNode):
        self._mayaNode = mayaNode
    
    @property
    def mayaNode(self):
        return self._mayaNode

    @property    
    def referencedFile(self):
        return self.mayaNode.referenceFile()
    
    @property
    def namespace(self):
        return pm.Namespace(pm.referenceQuery(self.mayaNode, namespace=True))

class MayaReferenceManager(OrderedDict):
    def __init__(self, *args, **kwargs):
        super(MayaReferenceManager, self).__init__(*args, **kwargs)
        self.loadFromSession()
    
    def loadFromSession(self):
        if self.keys():
            self.clear()
        for reference in pm.ls(references=True):
            self[reference.name()] = MayaReference(reference)

referenceManager = MayaReferenceManager()

yiRN = referenceManager['yiRN']

yiRN.namespace
yiRN.referencedFile.namespace
yiRN.referencedFile.namespaceExists()
yiRN.namespace.listNodes().index('{0}:char_rig'.format(yiRN.namespace))
