from setuptools import setup

setup(
    name='pycaptcha',
    version='0.1.0',
    packages=['pycaptcha'],
    install_requires=[
        'opencv-python',
        'keyring',
        'cryptography',
        'numpy',
    ],
)
