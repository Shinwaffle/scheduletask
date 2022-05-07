import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scheduletask",
    version="1.0.0",
    author="Shinwaffle",
    author_email="shinwaffle@gmail.com",
    description="Create google calendar events from the command line",
    long_description="I'm gonna add a longer description later",
    long_description_content_type="text/markdown",
    url="https://github.com/shinwaffle/scheduletask",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)