import os
from setuptools import setup, find_packages
PACKAGES = find_packages()


NAME = "Stereo-Depth-Estimation-Network"
DESCRIPTION = "Estimate depth information from stereo images captured by cameras"
URL = "https://github.com/chengqianma/Stereo-Depth-Estimation-Network"
LICENSE = "MIT"
AUTHOR = "Chenqian Ma | Bingkun Li | Robert Chang"
AUTHOR_EMAIL = "cm74@uw.edu | bingkunl@uw.edu | zqw450397740@gmail.com"
VERSION = "__version__ 1.0"
PLATFORMS = "Ubuntu 16.04 LTS"
REQUIRES = ["numpy", "opencv", "pyqt5", "torch", "skimage"]

opts = dict(name=NAME,
            description=DESCRIPTION,
            url=URL,
            license=LICENSE,
            author=AUTHOR,
            author_email=AUTHOR_EMAIL,
            platforms=PLATFORMS,
            version=VERSION,
            packages=PACKAGES,
            requires=REQUIRES)


if __name__ == '__main__':
    setup(**opts)