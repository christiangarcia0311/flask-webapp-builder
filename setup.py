from setuptools import setup, find_packages


with open('README.md', 'r', encoding='utf-8') as file:
  description = file.read()
setup(
    name='flask-webapp-builder',
    version='1.2.0',
    packages=find_packages(),
    author='Christian Garcia',
    author_email='iyaniyan03112003@gmail.com',
    description='A Flask Webapp Builder is designed to generate a basic fully flask project structure. Including the directory folders and files also run-server script to execute the webapp server.',
    long_description=description,
    long_description_content_type='text/markdown',
    url='https://github.com/christiangarcia0311/flask-webapp-builder',
    license='MIT',
    entry_points={
        'console_scripts': [
            'build-flask-webapp = FlaskWebApp.build_flask_webapp:main',
        ],
    },
    install_requires=[
        'Flask',
    ],
    include_package_data=True,
    package_data={
        'FlaskWebApp': [
            'data_assets/logo.png',
            'data_assets/icon.jpg',
            'data_assets/Rubik-Regular.ttf',
        ],
    },
    classifiers= [ 
      'Programming Language :: Python :: 3',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
      'Topic :: Software Development :: Libraries :: Python Modules',
      ],
)
