from setuptools import setup, find_packages

setup(
    name='supermath',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    description='A simple math operations package',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/supermath',
)
