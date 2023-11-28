from pathlib import Path

from setuptools import find_packages, setup

# # allow setup.py to be run from any path
# os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-cached',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['django>=3.2'],
    license='MIT',
    description='Caching decorator for Django',
    long_description=(Path(__file__).parent / 'README.md').read_text(),
    long_description_content_type="text/markdown",
    url='https://github.com/c0ntribut0r/django-cached',
    keywords='requests api',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
