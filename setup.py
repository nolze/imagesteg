from setuptools import setup

setup(
    name='imgsteg',
    version="0.1.0",
    description='A simple steganography tool for images',
    long_description=open("README.md", "r").read(),
    long_description_content_type='text/markdown',
    url='https://github.com/nolze/imgsteg',
    author='nolze',
    author_email='nolze@archlinux.us',
    license='MIT',
    keywords='',
    packages=[
        "imgsteg",
        "imgsteg.ui",
    ],
    include_package_data=True,
    install_requires=[
        'bitstring >= 3.1',
        'bottle >= 0.12',
        'Pillow >= 5.3',
    ],
    entry_points={
        'console_scripts': [
            'imgsteg = imgsteg.__main__:main',
        ],
    },
)
