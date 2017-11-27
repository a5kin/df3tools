"""
A setuptools based setup module.

Adopted from:
https://github.com/pypa/sampleproject

"""

from setuptools import setup, find_packages
# from codecs import open
from os import path
# import glob

here = path.abspath(path.dirname(__file__))
# print(glob.glob(here + "/*"))
# with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
#    long_description = f.read()
long_description = """
df3tools
========

Command-line tools to convert POV-Ray density files (DF3) to a set of images
and vise versa.

"""

setup(
    name='df3tools',
    version='0.1.0',
    description='Tools to convert Pov-Ray DF3 files to set of images '
                'and vice versa',
    long_description=long_description,
    url='https://github.com/a5kin/df3tools',
    author='Andrey Zamaraev',
    author_email='a5kin@github.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Topic :: Artistic Software',
        'Topic :: Multimedia :: Graphics :: 3D Modeling',
        'Topic :: Multimedia :: Graphics :: 3D Rendering',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='povray pov-ray density file df3 commandline tools utils utility',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['Pillow'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    package_data={
        'df3tools': ['README.rst'],
    },
    data_files=[('df3tools', ['README.rst'])],
    entry_points={
        'console_scripts': [
            'df3split=df3tools.df3split:main',
            'df3combine=df3tools.df3combine:main',
        ],
    },
)
