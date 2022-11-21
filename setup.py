from setuptools import setup, find_packages

setup(
    name='fastapi-cli',
    version='0.0.1',
    author='VissaMoutafis',
    author_email='vissarionm2000@gmail.com'
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'fastapi[all]',
        'gitPython',
        'git+https://github.com/VissaMoutafis/fastapi-cli'
    ],
    entry_points={
        'console_scripts': [
            'fastapi-cli = fastapicli.scripts.base:cli',
        ],
    },
)