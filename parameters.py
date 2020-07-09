c = 1

if c == 1:
    voxel_size = 0.5 #0.5 #2
    normal_search_radius = 1 #1 #3
    feature_search_radius = 4 #2.5
    local_icp_distance_threshold =15
    global_icp_distance_threshold = 2
    global_icp_repeat = 1 #5  #40
    ransac_feature_match_threshold = 10000 #10000 #50000


if c == 2:
    voxel_size = 3 #0.5 #2
    normal_search_radius = 3 #1 #3
    feature_search_radius = 3#2.5
    local_icp_distance_threshold = 0.1
    global_icp_distance_threshold = 0.75
    global_icp_repeat = 30 #5  #40
    ransac_feature_match_threshold = 100000 #10000 #50000