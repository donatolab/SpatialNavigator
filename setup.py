import os

from setuptools import find_packages, setup

install_requires = [
    line.rstrip()
    for line in open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
]

setup(
    name="SpatialNavigator",
    install_requires=install_requires,
    version="0.0.1",
    description="Determining spatial selectivity and attributes of individual cells",
    url="https://github.com/donatolab/SpatialNavigator",
    license="MIT",
    packages=find_packages(),
    zip_safe=False,
)