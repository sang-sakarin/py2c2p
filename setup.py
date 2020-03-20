from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='py2c2p',
    version='0.0.2',
    description='A Python library for 2c2p API',
    long_description=readme(),
    long_description_content_type="text/markdown",
    url='https://github.com/sang-sakarin/py2c2p',
    author='sang_sakarin',
    author_email='sang_sakarin@outlook.com',
    license='sang_sakarin',
    scripts=[],
    keywords='2c2p 2c2p-python 2c2p-python-sdk',
    packages=['py2c2p'],
    install_requires=['requests'],
)
