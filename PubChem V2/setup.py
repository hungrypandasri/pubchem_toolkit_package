"""Setup script for the pubchem_toolkit package."""

from setuptools import setup, find_packages

setup(
    name="pubchem_toolkit",
    version="0.0.2",  # Update version number to 0.0.2
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="Sriram Natarajan",
    author_email="hungrypandasriram@gmail.com",
    description="A toolkit for accessing PubChem database.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pubchem-toolkit",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
    ],
)
