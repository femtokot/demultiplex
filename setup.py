from setuptools import setup, find_packages


setup(
    name='demult',
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['demult=demultiplex:demultiplex']
    },
    install_requires=['click'],
    zip_safe=False,
)
