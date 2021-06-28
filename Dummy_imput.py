import open3d as o3d

def create_input_offline():
    mesh = o3d.io.read_triangle_mesh(r"tagged_pelvis.stl")
    mesh_digitised = o3d.io.read_triangle_mesh(r"tagged_pelvis_moved.stl")
    pointcloud = mesh.sample_points_poisson_disk(5000)
    pointcloud_digitised = mesh_digitised.sample_points_poisson_disk(5000)

    # o3d.visualization.draw_geometries([mesh])
    # o3d.visualization.draw_geometries([pointcloud])

    o3d.io.write_point_cloud("C:\Temp\CtBone.pcd", pointcloud)
    o3d.io.write_point_cloud("C:\Temp\localiserCombined.pcd", pointcloud_digitised)

import numpy as np
create_input_offline()
sourceFile = r"C:\Temp\boneMeshPelvis.pcd" #r"boneMeshPelvis.pcd"
targetFile = r"C:\Temp\digitisedpntsPelvis.pcd" #r"digitisedpntsPelvis.pcd"
pc_source = o3d.io.read_point_cloud(sourceFile)
pc_target = o3d.io.read_point_cloud(targetFile)

# create_input_offline()

with open(r"C:\Temp\boneMeshPelvis.pcd") as f:
    points = f.readlines()[10:]
    pointsCoordinate = np.zeros((len(points),3))
    for indexn, point in enumerate(points):
        coordinates = [float(i) for i in point.split()]
        for index3, coordinate in enumerate(coordinates):
            pointsCoordinate[(indexn,index3)] = coordinate

pc_source.points.clear()
for coordinates in pointsCoordinate:
    pc_source.points.append(coordinates)

o3d.visualization.draw_geometries([pc_source])
o3d.visualization.draw_geometries([pc_target])