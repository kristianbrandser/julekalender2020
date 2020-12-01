
from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="julekalender2020",
    version="0.0.1",
    author="Kristian Brandser",
    author_email="kmb@knowit.no",
    description="A package for julekalender 2020 solutions",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/kristianbrandser/julekalender2020/",
    packages=find_packages(),
    install_requires=requirements_dev,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
