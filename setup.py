from setuptools import setup, find_packages

setup(
    name='geez2ethiop',
    version='0.0.1a0',
    packages=find_packages(),
    install_requires=[
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'geez2ethiop = geez2ethiop.geez2ethiop:main'            
        ]
    }
)