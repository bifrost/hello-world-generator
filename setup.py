""" Setup file for the hello-world-generator package. """
from setuptools import find_packages, setup

with open("app/README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="hello-world-generator",
    version="0.0.1",
    description="A hello world generator",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bifrost/hello-world-generator",
    author="bifrost",
    author_email="dan@steenbjerg.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    extras_require={
        "dev": ["pytest>=7.4.3", "twine>=4.0.2", "pylint>=3.0.2", "black>=23.10.1", "wheel>=0.41.3"],
    },
    python_requires=">=3.12",
)
