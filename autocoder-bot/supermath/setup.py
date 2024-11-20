from setuptools import setup, find_packages

setup(
    name='supermath',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    description='A simple package for basic math calculations',
    author='Your Name',
    author_email='your.email@example.com'
)
