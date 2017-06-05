from setuptools import setup, find_packages
from codecs import open
from os import path

# python setup.py bdist_wheel
# python setup.py sdist

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='news',
    version='0.0.1',
    description='A simple Django app to create and publish short news feeds.',
    long_description=long_description,
    url="https://redmine.acdh.oeaw.ac.at/issues/8711",
    author="Peter Andorfer",
    author_email="peter.andorfer@oeaw.ac.at",
    license='MIT',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11'
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=['djangorestframework'],
)
