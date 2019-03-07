from open3d import *
import numpy as np
import sys
import Estimate
import Refine
import Common


if __name__ == "__main__":
    try:
        #source is floating
        #target is rigid

        #sourceF#ile = "C:\Temp\CtBone.pcd"
        #targetFile = "C:\Temp\localiserCombined.pcd"
        #func_to_run = "1"

        sourceFile = sys.argv[1]
        targetFile = sys.argv[2]
        func_to_run = sys.argv[3]

        source_pc = Common.read_pc(sourceFile)
        target_pc = Common.read_pc(targetFile)

        if func_to_run == "1":
            Estimate.estimate_global_transform(source_pc, target_pc)
        elif func_to_run == "2":
            Refine.refine_local_transform(source_pc, target_pc, np.identity(4))
    except Exception as e:
        print("main crashed. Error: %s", e)
