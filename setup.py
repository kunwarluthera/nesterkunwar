from setuptools import setup
import os 

def read(fname):
    return open(os.path.join(os.path.dirname(__file__),fname)).read()

setup(

    name = "nester-kunwar",
    version = "1.1.1",
    py_modules = ["nester-kunwar"],
    author = "Kunwar Shamsher Luthera",
    author_email = "kunwarluthera@gmail.com",
    url = "https://github.com/kunwarluthera/nester-kunwar",
    description = "This is first module for nested lines",
    long_description=read('README')

)