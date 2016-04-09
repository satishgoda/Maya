import maya.cmds as cmds

cmds.window()

cmds.columnLayout()

cmds.rowColumnLayout( numberOfColumns=1)
cmds.intSliderGrp( field=True, label='Radius', 
                   min=1, max=10, step=1,
                   columnWidth3=[50, 50, 100],
                    columnAlign3=['left', 'left', 'left'],
                    adjustableColumn3=3)
cmds.intSliderGrp( field=True, label='Height', 
                    min=1, max=100, value=3, step=1, 
                    columnWidth3=[50, 50, 100],
                    columnAlign3=['left', 'left', 'left'],
                    adjustableColumn3=3)

cmds.rowColumnLayout( numberOfColumns=2, 
                      columnSpacing=[(2, 77)], 
                      columnWidth=[(2, 100)])
cmds.text(label='Users')
cmds.intSlider()

cmds.showWindow()
