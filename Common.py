from open3d import *
import copy


def draw_registration_result(source, target, transformation):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    source_temp.paint_uniform_color([1, 0.706, 0])
    target_temp.paint_uniform_color([0, 0.651, 0.929])
    source_temp.transform(transformation)
    draw_geometries([source_temp, target_temp])


def write_result(reg_result):
    print("RESULT")
    print("RMSE ", reg_result.inlier_rmse)
    print("FITNESS ", reg_result.fitness)
    print("TRANSFORM")
    print(reg_result.transformation)


def read_pc(location):
    return read_point_cloud(location, format='xyz')