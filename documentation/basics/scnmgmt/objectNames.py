
pm.ls(regex="pSphere[\d]+")

'''
# Result: [nt.Transform(u'group1|pSphere1'),
 nt.Transform(u'group1|pSphere2'),
 nt.Transform(u'|pSphere1'),
 nt.Transform(u'|pSphere2')] # 
'''

pm.ls(regex="pSphere1")

'''
# Result: [nt.Transform(u'group1|pSphere1'), nt.Transform(u'|pSphere1')] # 
'''

pm.ls(regex="*SphereShape.*", type='shape')

'''
# Result: [nt.Mesh(u'|pSphere1|pSphereShape1'),
 nt.Mesh(u'group1|pSphere1|pSphereShape1'),
 nt.Mesh(u'|pSphere2|pSphereShape2'),
 nt.Mesh(u'group1|pSphere2|pSphereShape2')] 
'''
