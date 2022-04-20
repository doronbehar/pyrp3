from distutils.core import setup
from pathlib import Path

from PyRedPitaya import __version__

setup(
    name="PyRedPitaya",
    version=__version__,
    description="Python utilities for redpitaya",
    author="Pierre Cladé",
    author_email="pierre.clade@upmc.fr",
    maintainer="Bastian Leykauf",
    maintainer_email="leykauf@physik.hu-berlin,de",
    long_description=(Path(__file__).parent / "README.rst").read_text(),
    long_description_content_type="text/rst",
    packages=["PyRedPitaya", "PyRedPitaya.enum"],
    install_requires=["myhdl", "rpyc", "cached_property", "numpy"],
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=["redpitaya", "FPGA", "zynq"],
)
