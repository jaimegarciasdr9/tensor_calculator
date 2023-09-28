from importlib.metadata import entry_points

from idna import package_data
from setuptools import setup, find_packages
from module_structure import __author__, __version__, __name__

VERSION = __version__
AUTHOR = __author__
NAME = __name__


# Main setup configuration
def install_requires():
    pass


setup(
    name="module_structure",
    version="0.1.0",
    description="My first professional project",
    author="Jaime García",
    author_email="jaimegarciasdr9@gmail.com",
    url="https://github.com/jaimegarciasdr9/module_structure",

    packages=find_packages,
    include_package_data=True,
    package_data=package_data,
    install_requires=install_requires,
    entry_points=entry_points,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

# Required packages (dependencies)
install_requires = [
    # List your project's dependencies here
]
