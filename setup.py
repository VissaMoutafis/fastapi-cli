from setuptools import setup, find_packages

setup(
    name='fastapi-cli',
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
            'fastapi-cli = fastapicli.scripts.base:cli',
        ]
    },
)