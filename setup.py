import pypandoc

from setuptools import setup


long_description = pypandoc.convert('README.md', 'rst')

setup(
    name='py2c2p',
    version='0.0.1',
    description='A Python library for 2c2p API',
    long_description=long_description,
    url='https://github.com/sang-sakarin/py2c2p',
    author='sang_sakarin',
    author_email='sang_sakarin@outlook.com',
    license='sang_sakarin',
    scripts=[],
    keywords='2c2p 2c2p-python 2c2p-python-sdk',
    packages=['py2c2p'],
    install_requires=[],
)
