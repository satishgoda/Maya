file -r -type "mayaAscii"  -ignoreVersion -gn "house1" -dr 1 -mergeNamespacesOnClash false -namespace "house1" -options "v=0;" "asset/house/bbox.ma";
// Result: asset/house/bbox.ma // 
file -loadReferenceDepth "asPrefs" -loadReference "house1RN" "asset/house/bbox.ma";
// File read in  0.021 seconds. // 
// Result: asset/house/bbox.ma // 
proxyAdd "house1RN" "asset/house/low.ma" "lo";
