from setuptools import setup

setup(
    name='project',
    version='0.3',
    description='Story-telling SHaring PLatform',
    author='Rory Sheridan',
    author_email='sheridan.rp@gmail.com',
    url='http://corona-tales.herokuapp.com/',
    packages=['project'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
