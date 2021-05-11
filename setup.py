from setuptools import setup
import os, re

with open("README.md", "r") as fh:
    long_description = fh.read()


def get_version() -> str:
    """Get __version__ from __init__.py file."""
    version_file = os.path.join(os.path.dirname(__file__), "kivytransitions", "__init__.py")
    version_file_data = open(version_file, "rt", encoding="utf-8").read()
    version_regex = r"(?<=^__version__ = ['\"])[^'\"]+(?=['\"]$)"
    try:
        version = re.findall(version_regex, version_file_data, re.M)[0]
        return version
    except IndexError:
        raise ValueError(f"Unable to find version string in {version_file}.")


setup(
    name="kivytransitions",
    version=get_version(),
    packages=["kivytransitions"],
    package_data={"kivytransitions": ["*.py", "transitions/*", "transitions/extra/*"],},
    # metadata to display on PyPI
    author="Shashi Ranjan",
    author_email="shashiranjankv@gmail.com",
    description="A variety of custom screen transitions for kivy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="transitions shaders kivy-application kivy python",
    url="https://github.com/shashi278/KivyShaderTransitions",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Android",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: OS Independent"
    ],
    install_requires=["kivy"],

    python_requires=">=3.6",
)