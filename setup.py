from setuptools import setup
import main

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name=main.__name__,
   version='0.0.1',
   description='Utils module for programing',
   long_description=long_description,
   author=main.__author__,
   author_email='jonascouturon2@gmail.com',
   url="http://www.foopackage.example/",
   install_requires=['numpy'], #external packages as dependencies
)