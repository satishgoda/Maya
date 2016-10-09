import pymel.core as pm

window = pm.window()
clayout = pm.columnLayout(rowSpacing=10, adjustableColumn=True)
pm.button()
pm.button()
pm.button()
pm.showWindow()

clayout.adjustableColumn(val=False)
clayout.adjustableColumn(val=True)

clayout.setRowSpacing(val=5)
clayout.setBackgroundColor(val=(1, 0, 0))

for child in clayout.children():
    child.setBackgroundColor(val=(0.5, 0.5, 0.5))
