import os
from setuptools import setup

__version__ = '0.0.1'


def read(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name)) as f:
        return f.read()


setup(
    name='jjb-discord',
    version=__version__,
    description='Jenkins Job Builder Discord Notifier',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/ettoreleandrotognoli/jjb-discord',
    download_url='https://github.com/ettoreleandrotognoli/jjb-discord/tree/v%s/' % __version__,
    author='Ettore Leandro Tognoli',
    author_email='ettoreleandrotognoli@gmail.com',
    license='Apache License 2.0',
    entry_points={
        'jenkins_jobs.publishers': [
            'discord-notifier = jjb_discord.discord_notifier:publisher'
        ]
    },
    packages=['jjb_discord'],
    install_requires=[
        'jenkins-job-builder',
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ]
)
