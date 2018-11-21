# -*- coding: utf8 -*-

from setuptools import setup, find_packages



__version__ = "0.0.3"

install_requires = [
    "requests",
    "pyyaml"
]

setup(
    name="robotli_init",
    version=__version__,
    install_requires=install_requires,
    author="lipo",
    author_email="15510520668@163.com",
    maintainer="lipo",
    maintainer_email="15510520668@163.com",
    packages= find_packages(),
    include_package_data=True,
    description="Use for init robot",
    platforms="any",
    entry_points={
        "console_scripts": [
            "robotli-client = robotli_init.robotli_client.server:main"
        ]
    }
)