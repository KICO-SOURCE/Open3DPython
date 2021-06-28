import open3d as o3d
import numpy as np
import copy


def draw_registration_result(source, target, transformation):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    source_temp.paint_uniform_color([1, 0.706, 0])
    target_temp.paint_uniform_color([0, 0.651, 0.929])
    source_temp.transform(transformation)
    o3d.visualization.draw_geometries([source_temp, target_temp])


def write_result(reg_result):
    print("RESULT")
    print("RMSE ", reg_result.inlier_rmse)
    print("FITNESS ", reg_result.fitness)
    print("TRANSFORM")
    print(reg_result.transformation)


def read_pc(location):
    pointCloud = o3d.io.read_point_cloud(location)
    with open(location) as f:
        points = f.readlines()[10:]
        pointsCoordinate = np.zeros((len(points), 3))
        for indexn, point in enumerate(points):
            coordinates = [float(i) for i in point.split()]
            for index3, coordinate in enumerate(coordinates):
                pointsCoordinate[(indexn, index3)] = coordinate

    pointCloud.points.clear()
    for coordinates in pointsCoordinate:
        pointCloud.points.append(coordinates)

    return pointCloud