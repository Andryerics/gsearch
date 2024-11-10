from setuptools import setup, find_packages

setup(
    name="gsearch",  
    version="1.0.0",  
    description="Search with Google",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Andryerics",
    author_email="andryerics@gmail.com",
    url="https://github.com/andryerica1/Gsearch",  
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
