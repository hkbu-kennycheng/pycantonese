#!usr/bin/env python3

from setuptools import (setup, find_packages)

setup(name="pycantonese",
    version="1.0dev",
    description="PyCantonese",
    url="http://pycantonese.github.io/",
    author="Jackson Lee",
    author_email="jsllee.phon@gmail.com",
    license="Apache License, Version 2.0",
    packages=find_packages(),
    keywords=['computational linguistics', 'natural language processing',
                'NLP', 'Cantonese', 'linguistics', 'corpora', 'speech',
                'language', 'Chinese', 'Jyutping', 'NLTK', 'tagging'],
    install_requires=["nltk"],

    package_data={
        "pycantonese": ["data/hkcancor/*"],
    },

    zip_safe=False,

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: Chinese (Traditional)',
        'Natural Language :: Cantonese',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: General',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic'
    ],
)
