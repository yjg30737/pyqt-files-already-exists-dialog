import codecs
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='pyqt-files-already-exists-dialog',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt files already exists dialog. Like "These files already exist, '
                'Would you add files except for these? (Yes/No)"',
    url='https://github.com/yjg30737/pyqt-files-already-exists-dialog.git',
    long_description_content_type='text/markdown',
    long_description=long_description,
    install_requires=[
        'PyQt5>=5.8',
        'simplePyQt5>=0.0.1'
    ]
)