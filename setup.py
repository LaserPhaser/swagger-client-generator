from codecs import open
from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


def main():
    setup(
        name='swagger_client_generator',
        version='0.0.1',

        description='A library that generates clients for service to file or on a fly',
        long_description=long_description,
        author='Arseniy Antonov',
        author_email='arseny.antonov@gmail.com',

        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Build Tools',
            'Programming Language :: Python :: 3.6',
        ],
        packages=find_packages(),

        install_requires=['Jinja2==2.11.3',
                          ]
    )


if __name__ == "__main__":
    main()
