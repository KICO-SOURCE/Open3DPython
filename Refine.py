import open3d as o3d
import numpy as np
import Common
import parameters

reg = o3d.pipelines.registration

def refine_registration(source, target, globalTrans):
    #estimate_normals(source, KDTreeSearchParamHybrid(radius=parameters.normal_search_radius, max_nn=30)) #30
    #estimate_normals(target, KDTreeSearchParamHybrid(radius=parameters.normal_search_radius, max_nn=30)) #30
    Common.draw_registration_result(source, target, np.identity(4))
    result = reg.registration_icp(source, target, parameters.local_icp_distance_threshold, globalTrans, reg.TransformationEstimationPointToPoint())
    Common.draw_registration_result(source, target, result.transformation)
    return result


def refine_local_transform(sourcePCD, targetPCD, estimated_trans):
    my_result = refine_registration(sourcePCD, targetPCD, estimated_trans)
    Common.write_result(my_result)




