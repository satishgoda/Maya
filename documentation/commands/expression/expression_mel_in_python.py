import pymel.core as pm


try:
    cub = pm.PyNode('cub')
    cyl = pm.PyNode('cyl')
    sph = pm.PyNode('sph')
except pm.MayaNodeErro as mne:
    print mne
    raise

# expr = "{2} = 2* ({0} + {1})".format(
#                                 "cyl.tz",
#                                 "sph.tz",
#                                 "cub.ty"
#                                 )
# 

# expr = """
# {2} = 2 * ({0} + {1});
#     """.format(
#             "cyl.tz",
#             "sph.tz",
#             "cub.ty"
#         )
# 

expr = """
float $val1 = `getAttr {0}`;
float $val2 = `getAttr {1}`;

{2} = 2 * ($val1 + $val2);
    """.format(
            "cyl.tz",
            "sph.tz",
            "cub.ty"
        )

print expr

try:
    pm.expression(s=expr)
except RuntimeError as e:
    print e
