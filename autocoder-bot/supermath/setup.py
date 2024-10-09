from setuptools import setup, find_packages

setup(
    name='supermath',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    description='A simple math calculation package',
    zip_safe=True,
)
