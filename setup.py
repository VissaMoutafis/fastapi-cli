from setuptools import setup, find_packages

setup(
    name='fastapicli',
    version='0.0.0',
    author='VissaMoutafis',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'fastapi[all]',
        'gitPython'
    ],
    entry_points={
        'console_scripts': [
            'fastapi-cli = fastapicli.scripts.base:cli',
        ],
    },
)