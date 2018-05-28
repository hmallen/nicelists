from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='nicemessages',
    version='0.1.dev',
    author='Hunter M. Allen',
    author_email='allenhm@gmail.com',
    license='MIT',
    packages=['nicemessages'],
    install_requires=[],
    description=('Parses Pymarketcap json (limited to this for now) and \
                  outputs formatted list of data for chat messages.'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hmallen/nicemessages',
    keywords=['json', 'slack', 'telegram', 'message', 'pymarketcap'],
    classifiers=(
        'Programming Language :: Python :: 3',
    ),
)
