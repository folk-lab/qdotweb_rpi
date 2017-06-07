from setuptools import setup

setup(name='qdotweb_rpi',
    version='0.1',
    install_requires = ['flask>=0.12.2', 'json'],
    description='A Flask wrapper for custom client control',
    url='https://github.com/folk-lab/qdotweb_rpi',
    author='Ro-ee Tal',
    license='MIT',
    packages=['qdotweb_rpi'])
