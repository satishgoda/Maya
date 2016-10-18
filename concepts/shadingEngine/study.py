shader_assignment = []

for shadingEngine in renderPartition.inputs():
    if not shadingEngine.members():
        continue
    if shadingEngine.name() == 'initialShadingGroup':
        continue
    
    nameSE = shadingEngine.name()
    nameSH = shadingEngine.surfaceShader.inputs()[0].name()
    shader_assignment.append([nameSE, 
                              nameSH,
                              shadingEngine.listHistory(pruneDagObjects=True),
                              shadingEngine.asSelectionSet().getSelectionStrings()])

if not shading_network_dir.exists():
    shading_network_dir.makedirs()

for nameSG, nameSH, shading_network, objects in shader_assignment:
    pm.select(deselect=True)
    pm.select(shading_network, noExpand=True)
    shading_network_path = shading_network_dir / nameSG + '.ma'
    pm.exportSelected(shading_network_path)

for mesh in pm.ls(type='mesh'):
    pm.select(mesh, replace=True)
    pm.hyperShade(assign='lambert1')

for shadingEngine in renderPartition.inputs():
    if shadingEngine.name() in ('initialShadingGroup', 'initialParticleSE'):
        continue
    if not shadingEngine.members():
        shading_network = shadingEngine.listHistory(pruneDagObjects=True)
        pm.select(shading_network, noExpand=True, replace=True)
        pm.delete()

for snfile in shading_network_dir.listdir():
    nodes = pm.importFile(snfile)
    newNodes.append((snfile.namebase, nodes))

for nameSG, nameSH, shading_network, objects in shader_assignment:
    for object in objects:
        pm.select(object, replace=True)
        pm.hyperShade(assign=nameSH)
