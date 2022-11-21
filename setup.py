from setuptools import setup

setup(
    name='fastapicli',
    version='0.0.1',
    author='VissaMoutafis',
    packages=['fastapicli'],
    install_requires=[
        'Click',
        'fastapi[all]',
        'gitPython',
    ],
    entry_points={
        'console_scripts': [
            'fastapicli = fastapicli.scripts.base:cli',
        ]
    },
)