from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="smartcalc_mlops",
    version="0.1.0",
    author="sunilakiran",
    description="A Smart Calculator Python package with ML features built with MLOps best practices.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sunilakiran/smartcalc_mlops",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
