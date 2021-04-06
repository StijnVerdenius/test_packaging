import codecs
import os.path

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("src/example_pkg/version.py", "r", encoding="utf-8") as fh:
    version = fh.read().split(" = ")[-1]


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")



setuptools.setup(
    name="example-banana",  # Replace with your own username
    version=f"{version}",
    author="A Banana",
    author_email="ba@nana.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/StijnVerdenius/test_packaging",
    project_urls={
        "Bug Tracker": "https://github.com/StijnVerdenius/test_packaging",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
