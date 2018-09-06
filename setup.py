from setuptools import find_packages, setup

setup(
    name='DataBridge',
    version='1.2',
    author="Eric Zhao",
    author_email="eric@whimmly.com",
    include_package_data=True,
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    long_description=open('README.md').read(),
    url="git@github.com:whimmly/DataBridge",
    install_requires=[
        "pymongo",
        "neo4j-driver",
        "dill",
        "log4mongo"
    ],
)
