import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-banana", # Replace with your own username
    version="0.0.1",
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