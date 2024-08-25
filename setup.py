from setuptools import setup, find_packages

setup(
    name="scac",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'scac=scac.scac:main',  # Points to the main function in scac.py
        ],
    },
    install_requires=[
        'pydub',
        'argparse',
    ],
    author="George Zambonin",
    description="A simple audio converter CLI tool.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/glucard/simpler-cli-audio-converter",  # Optional
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
