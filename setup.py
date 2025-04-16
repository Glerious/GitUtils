from setuptools import setup
import main

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name=main.__name__,
   version=main.__version__,
   description='Utils modules for programming',
   long_description=long_description,
   author=main.__author__,
   author_email='jonascouturon2@gmail.com',
   url=main.__github__,
#    install_requires=['numpy', 'deprecated', 'functools'],
   py_modules=['maths', 'basics', 'space', 'jsonAPI']
)