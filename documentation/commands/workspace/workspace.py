import os

import maya.cmds as cmds

import pymel.core as pm

path_ws = pm.pathClass( cmds.workspace(query=True, fullName=True) )

mel_ws = path_ws / 'workspace.mel'
os.system("gvim " + mel_ws)

os.system("nautilus {}".format(path_ws))
