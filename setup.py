from setuptools import setup

setup(
    name = "server_docker",
    version = '0.0.1',
    author = 'Saionara',
    description = '',
    license= 'GNU',
    install_requires ='flask',
    entry_points = {
        'console_scripts':[
            'ser_docker = main:main'
        ]
    }
)