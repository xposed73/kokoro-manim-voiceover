from setuptools import setup, find_packages

setup(
    name='kokoro-mv',
    version='0.1.0',
    author='Nadeem Akhtar Khan',
    author_email='nadeemak755@gmail.com',
    description='Library for generating voiceover in manim using Kokoro-82M model',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/xposed73/kokoro-mv',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
    install_requires=[
        # List your library dependencies here
    ],
)