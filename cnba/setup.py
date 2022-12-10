from setuptools import find_packages, setup

setup(
    name="cnba",
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'click',
        'pandas',
        'statsmodels',
        'scipy',
        'console_logging',
        'tqdm'
    ],
    entry_points='''
    [console_scripts]
    cnba=cnba:main
    '''

)