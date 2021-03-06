Maya Projects

* http://help.autodesk.com/view/MAYAUL/2017/ENU/?guid=GUID-D5CA162A-0956-49C6-9FAC-2F73DCF03409
* http://help.autodesk.com/cloudhelp/2017/ENU/Maya-Tech-Docs/Commands/workspace.html

```
workspace -query -fn
// Result: /home/sgoda/maya/projects/default/scenes/pipeline2/rigging/char/bishop //

workspace -query -l
// Result: workspace.mel bishop.v0001 //

workspace -query -listWorkspaces
// Result: default default/scenes/pipeline2/rigging/char/alfred default/scenes/pipeline2/rigging/char/bishop //

workspace -query -listFullWorkspaces
// Result: /home/sgoda/maya/projects/default /home/sgoda/maya/projects/default/scenes/pipeline2/rigging/char/alfred /home/sgoda/maya/projects/default/scenes/pipeline2/rigging/char/bishop // 

workspace -query -directory
// Result: /home/sgoda/maya/projects/default/scenes/pipeline2/rigging/char/bishop/ // 

workspace -query -variableList

workspace -variable foo bar

workspace -query -variableList

workspace -query -variableEntry foo

workspace -saveWorkspace
```

```
//Maya 2017 Project Definition

workspace -fr "fluidCache" "cache/nCache/fluid";
workspace -fr "images" "images";
workspace -fr "DXF_FBX" "data";
workspace -fr "offlineEdit" "scenes/edits";
workspace -fr "furShadowMap" "renderData/fur/furShadowMap";
workspace -fr "iprImages" "renderData/iprImages";
workspace -fr "FBX" "data";
workspace -fr "renderData" "renderData";
workspace -fr "scripts" "scripts";
workspace -fr "fileCache" "cache/nCache";
workspace -fr "eps" "data";
workspace -fr "DAE_FBX" "data";
workspace -fr "shaders" "renderData/shaders";
workspace -fr "3dPaintTextures" "sourceimages/3dPaintTextures";
workspace -fr "translatorData" "data";
workspace -fr "mel" "scripts";
workspace -fr "furFiles" "renderData/fur/furFiles";
workspace -fr "OBJ" "data";
workspace -fr "particles" "cache/particles";
workspace -fr "scene" "scenes";
workspace -fr "FBX export" "data";
workspace -fr "furEqualMap" "renderData/fur/furEqualMap";
workspace -fr "sourceImages" "sourceimages";
workspace -fr "furImages" "renderData/fur/furImages";
workspace -fr "clips" "clips";
workspace -fr "BIF" "data";
workspace -fr "DAE_FBX export" "data";
workspace -fr "depth" "renderData/depth";
workspace -fr "sceneAssembly" "sceneAssembly";
workspace -fr "teClipExports" "Time Editor/Clip Exports";
workspace -fr "DXF_FBX export" "data";
workspace -fr "ASS" "data";
workspace -fr "movie" "movies";
workspace -fr "ASS Export" "data";
workspace -fr "audio" "sound";
workspace -fr "bifrostCache" "cache/bifrost";
workspace -fr "autoSave" "autosave";
workspace -fr "mayaAscii" "scenes";
workspace -fr "move" "data";
workspace -fr "Alembic" "data";
workspace -fr "sound" "sound";
workspace -fr "diskCache" "data";
workspace -fr "illustrator" "data";
workspace -fr "mayaBinary" "scenes";
workspace -fr "templates" "assets";
workspace -fr "OBJexport" "data";
workspace -fr "furAttrMap" "renderData/fur/furAttrMap";
workspace -fr "timeEditor" "Time Editor";
workspace -v "foo" "bar";
```
