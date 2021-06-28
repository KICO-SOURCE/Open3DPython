import numpy as np
import sys
import Estimate
import Refine
import Common


if __name__ == "__main__":
    try:
        #source is floating
        #target is rigid

        # Define input file, this is done in Unity by writing out the .bat file as well
        # Only needed to run the script purely in python environment
        # sourceFile = r"C:\Users\alex\Desktop\P2P test\boneMeshPelvis.pcd"
        # targetFile = r"C:\Users\alex\Desktop\P2P test\digitisedpntsPelvis.pcd"
        # func_to_run = "1"

        # read the .pcd files as input.

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

