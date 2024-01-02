import json
from setuptools import setup, find_packages

with open('README.md', "r") as f:
    long_description = f.read()

setup(
    name='pyresult',
    version='0.1.0',
    author='Christian Højsager',
    description='A result type and error handling library for Python',
    package_dir={'': "src"},
    packages=find_packages(where="src"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hoejsagerc/pyresult",
    author_email="",
    license="MIT",
    classifiers=[
        "license :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    install_requires=[],
    extras_require={
        "dev": [
            "twine>=4.0.2"
        ]
    },
    python_requires='>=3.9'
)
