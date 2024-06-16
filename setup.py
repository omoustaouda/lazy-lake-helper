from setuptools import setup, find_packages

setup(
    name='lazy-lake-helper',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'python-telegram-bot',
        'schedule',
        'python-dotenv',
        'sqlalchemy',
    ],
)
