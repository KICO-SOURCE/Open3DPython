import open3d as o3d
import numpy as np

import Common
import parameters

geo = o3d.geometry
reg = o3d.pipelines.registration

def preprocess_point_cloud(pcd):
    pcd_down = geo.PointCloud.voxel_down_sample(pcd, parameters.voxel_size)
    pcd_down.estimate_normals(geo.KDTreeSearchParamHybrid(radius=parameters.normal_search_radius, max_nn=30))
    pcd_fpfh = reg.compute_fpfh_feature(pcd_down, geo.KDTreeSearchParamHybrid(radius=parameters.feature_search_radius, max_nn=100))
    return pcd_down, pcd_fpfh


def execute_global_registration(source_down, target_down, source_fpfh, target_fpfh):
    result = reg.registration_ransac_based_on_feature_matching(
            source_down, target_down, source_fpfh, target_fpfh, True,
            parameters.global_icp_distance_threshold,
            reg.TransformationEstimationPointToPoint(), 4,
            [reg.CorrespondenceCheckerBasedOnEdgeLength(0.6),
             reg.CorrespondenceCheckerBasedOnDistance(parameters.global_icp_distance_threshold)],
            reg.RANSACConvergenceCriteria(4000000, parameters.ransac_feature_match_threshold))
    return result


def execute_fast_global_registration(source_down, target_down, source_fpfh, target_fpfh, voxel_size):
    distance_threshold = voxel_size * 0.5
    result = reg.registration_fast_based_on_feature_matching(source_down, target_down, source_fpfh, target_fpfh,
            reg.FastGlobalRegistrationOption(division_factor = 1000,                    #1.4
                                         use_absolute_scale = 0,                        #0
                                         decrease_mu = 100,                               #1
                                         maximum_correspondence_distance = 5,    #0.025
                                         iteration_number = 64,                         #64
                                         tuple_scale = 0.65,                        #0.95
                                         maximum_tuple_count = 1000))                   #1000
    return result


def estimate_global_transform(source_point_cloud, target_point_cloud):
    source_down, source_fpfh = preprocess_point_cloud(source_point_cloud)
    target_down, target_fpfh = preprocess_point_cloud(target_point_cloud)
    #Common.draw_registration_result(source_down, target_down, np.identity(4))
    myResults = execute_global_registration(source_down, target_down, source_fpfh, target_fpfh)
    iterations = 1
    tempResult = execute_global_registration(source_down, target_down, source_fpfh, target_fpfh)
    while myResults.inlier_rmse - tempResult.inlier_rmse > 0.01:
        iterations = iterations+1
        tempResult = execute_global_registration(source_down, target_down, source_fpfh,
                                                 target_fpfh)
        #Common.draw_registration_result(source_down, target_down, myResults.transformation)
    Common.write_result(myResults)
    print (f"Number of Iterations:  {iterations}")


