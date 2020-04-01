import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shmailer-shchepin85",
    version="0.1.2",
    author="Vladimir Shchepin",
    author_email="shchepin85@gmail.com",
    description="shmailer project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shchepin85/shmailer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)