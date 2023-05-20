from distutils.core import setup
from setuptools import find_packages


setup(
    name='adviceslip-python',
    version='1.0',
    packages=['AdviceSlip'],
    license='MIT',
    long_description='Python wrapper for `Advice Slip` API at https://api.adviceslip.com/',
    install_requires=['requests'],
    url='https://github.com/SakthiLKoff/adviceslip-python',
    author='Sakthi LK'
)