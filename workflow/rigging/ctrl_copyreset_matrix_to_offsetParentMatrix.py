import pymel.core as pm


def copy_matrix_to_offsetParentMatrix(control):
    try:
        control.matrix.connect(control.offsetParentMatrix)
    except Exception as e:
        print e
        print control.name(), "Cannot connect to offsetParentMatrix"

    try:
        control.matrix.disconnect(control.offsetParentMatrix)
    except Exception as e:
        print e
        print control.name(), "Cannot disconnect from offsetParentMatrix"


def reset_translate_rotate(control):
    channels = "translateX translateY translateZ rotateX rotateY rotateZ"

    for channel in channels.split():
        control.attr(channel).set(0)


if __name__ = "__main__":
controls = pm.selected()

if not controls:
    raise ValueError("Nothing selected")

for control in controls:
    copy_matrix_to_offsetParentMatrix(control)
    reset_translate_rotate(control)
