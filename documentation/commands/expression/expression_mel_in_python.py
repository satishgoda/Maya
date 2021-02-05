import pymel.core as pm

cub = pm.PyNode('cub')

if cub.ty.isConnectable() and cub.ty.isConnected():
    cub.ty.disconnect()

cyl = pm.PyNode('cyl')
sph = pm.PyNode('sph')

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
# cub

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
#     pm.expression(s=expr,
#                   attribute='cub.ty',
#                   object='cub',
#                   alwaysEvaluate=True)
# 
    expr_node = pm.expression(s=expr,
                  attribute='cub.ty',
                  object='cub',
                  alwaysEvaluate=True,
                  animated=1)

except RuntimeError as e:
    print e
