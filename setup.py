from setuptools import setup, find_packages

setup(
    name="MY_DJANGO_PROJECT", 
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Django>=4.0",
    ],
    entry_points={
        "console_scripts": [
            "project-manage = manage:main",  
        ],
    },
)
