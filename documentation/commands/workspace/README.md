Maya Workspaces

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
