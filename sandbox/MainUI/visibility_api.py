class VisibilityState(object):
    @classmethod
    def _updateState(cls, state):
        raise NotImplementedError("This operation must be implemented in a concrete derived class ")
    
    @classmethod
    def show(cls):
        cls._update(1)

    @classmethod
    def hide(cls):
        cls._update(0)
        
    @classmethod
    def toggle(cls):
        if cls.isVisible():
            cls.hide()
        else:
            cls.show()

    @classmethod
    def isVisible(cls):
        return cmds.optionVar(query=cls.optionVar) 

    @classmethod
    def _update(cls, state):
        cls._updateOptionVar(state)
        cls._updateState(state)

    @classmethod
    def _updateOptionVar(cls, state):
        cmds.optionVar(intValue=[cls.optionVar, state])
    
class MainMenuBar(VisibilityState):
    optionVar = "mainWindowMenubarVis"
    
    @classmethod
    def _updateState(cls, state):
        window = mel.eval("$temp=$gMainWindow")
        cmds.window(window, edit=True, menuBarVisible=state)

class MainShelfTabs(VisibilityState):
    optionVar = "shelfTabsVisible"
    
    @classmethod
    def _updateState(cls, state):
        shelf = mel.eval("$temp=$gShelfTopLevel")
        cmds.shelfTabLayout(shelf, edit=True, tabsVisible=state)

class PanelMenuBars(VisibilityState):
    optionVar = "allowMenusInPanels"
    
    @classmethod
    def _updateState(cls, state):
        mel.eval("toggleMenuBarsInAllPanels({0})".format(state))
