import numpy as np

class RGBDSensor:
    """
    RGBD sensor (e.g., RealSense/Kinect) data reading and encapsulation.
    """
    def __init__(self, config=None):
        """
        Initialize the RGBD sensor.
        :param config: dict, optional, camera parameters or path to configuration file
        """
        self.config = config
        # TODO: Initialize hardware or data source here

    def read(self):
        """
        Read one frame of RGBD data.
        :return:
            rgb: ndarray, shape (H, W, 3)
            depth: ndarray, shape (H, W)
        """
        # TODO: Replace with real RGBD data reading code
        H, W = 480, 640
        rgb = (np.random.rand(H, W, 3) * 255).astype(np.uint8)
        depth = (np.random.rand(H, W) * 5000).astype(np.uint16)  # depth in mm
        return rgb, depth

    def close(self):
        """
        Release resources.
        """
        pass