from setuptools import setup, find_packages

setup(
    name='openwiz',
    version='0.2.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'openai',
        'pyyaml',
        'argparse',
        'click',
        'pytest'
    ],
    entry_points={
        'console_scripts': [
            'ow=src.cli:main',
        ],
    },
    author='Basith Ahmed',
    author_email='basithahmeddd@gmail.com',
    description='A CLI tool for generating code using the OpenAI API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/basith-ahmed/openwiz',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
