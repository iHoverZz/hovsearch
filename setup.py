import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hovsearch", 
    version="0.0.1",
    author="iHoverZz",
    author_email="ihoverzz@gmail.com",
    description="hovsearch is a Python Module to download and search youtube videos.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iHoverZz/hovsearch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["urllib","requests", "youtube_dl"],
    include_package_data=True
)
