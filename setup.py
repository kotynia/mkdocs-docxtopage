import os.path
import setuptools
from setuptools import setup

def read(name):
    mydir = os.path.abspath(os.path.dirname(__file__))
    return open(os.path.join(mydir, name)).read()


setuptools.setup(
    name='mkdocs-docxtopage',
    version='1.0.0',
    packages=['mkdocs_docxtopage'],
    url='https://github.com/kotynia/mkdocs-docxtopage',
    license='Apache',
    author='Marcin Kotynia',
    author_email='marcin@kotynia.com',
    description='A mkdocs plugin that converts docx files to markdown file with html contents.',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    install_requires=['mkdocs'],

    # The following rows are important to register your plugin.
    # The format is "(plugin name) = (plugin folder):(class name)"
    # Without them, mkdocs will not be able to recognize it.
    entry_points={
        'mkdocs.plugins': [
            'exclude = mkdocs_docxtopage:Exclude',
        ]
    },
)
