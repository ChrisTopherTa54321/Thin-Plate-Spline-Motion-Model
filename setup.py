from setuptools import setup, find_packages

setup(
    name='thin_plate_spline_motion',
    version='1.0',
    packages=find_packages(),
    package_data={'config': ['tpsmm/config/*'],},
    include_package_data=True,
    data_files=[('config', ['tpsmm/config/vox-256.yaml', 'tpsmm/config/ted-384.yaml'])],
    install_requires=["matplotlib",
                      "pyyaml",
                      "tqdm",
                      "scipy",
                      "imageio",
                      "scikit-image",
                      "torch",
                      "torchvision"]
)
