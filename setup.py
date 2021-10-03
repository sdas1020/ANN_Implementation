from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="sdas1020",
    description="A small package for dvc ml pipeline demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sdas1020/ANN_Implementation.git",
    author_email="surajit10@gmail.comm",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        'tensorflow',
        'matplotlib',
        'seaborn',
        'numpy',
        'pandas'
    ]
)