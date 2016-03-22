pm.select(deselect=True)

cmds.isolateSelect(cmds.getPanel(withFocus=True), state=False)

cmds.isolateSelect(cmds.getPanel(withFocus=True), state=True)

mel.eval('useBookmark {0} {1} true'.format(cmds.getPanel(withFocus=True), 'Cylindrical'))

mel.eval('useBookmark {0} {1} true'.format(cmds.getPanel(withFocus=True), 'Planar'))

cmds.isolateSelect(cmds.getPanel(withFocus=True), state=False)

cmds.isolateSelect(cmds.getPanel(withFocus=True), state=True)

mel.eval('useBookmark {0} {1} false'.format(cmds.getPanel(withFocus=True), 'Cylindrical'))
