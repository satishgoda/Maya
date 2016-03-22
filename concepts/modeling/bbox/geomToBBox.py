URL = "http://help.autodesk.com/cloudhelp/2016/ENU/Maya-Tech-Docs/CommandsPython/geomToBBox.html"

MEL = """
select -r pSphere1 ;

geomToBBox -name pSphere1 -nameSuffix _BBox -single -shaderColor 0.5 0.5 0.5 -keepOriginal

connectAttr -f BBoxLambert2.outColor BBoxSG2.surfaceShader;
sets -e -forceElement BBoxSG2;


select -tgl pSphere1_BBox ;

setAttr "pSphere1Shape_BBox.overrideEnabled" 1;
setAttr "pSphere1Shape_BBox.overrideLevelOfDetail" 1;
"""
