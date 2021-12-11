from setuptools import setup, find_packages

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
    install_requires=[
        'PyQt5>=5.8',
        'simplePyQt5 @ git+https://git@github.com/yjg30737/simplePyQt5.git@master'
    ]
)