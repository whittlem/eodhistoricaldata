"""Setup file for PyPI"""

# To use a consistent encoding
from codecs import open
from os import path

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="eodhistoricaldata",
    version="0.1.0",
    description="EOD Historical Data Python Library (Unofficial)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://whittle.medium.com",
    author="Michael Whittle",
    author_email="michael@lifecycle-ps.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(include=["eodhistoricaldata"]),
    include_package_data=True,
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "whittlem=eodhistoricaldata.__main__:main",
        ]
    },
    setup_requires=["pytest-runner"],
    tests_require=["pytest==6.2.5"],
    test_suite="tests"
)