from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path: str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name="student-performance-prediction",
    version="0.0.1",
    author="Partha Chakraborty",
    author_email="parthac350@gmail.com",
    description="A package for predicting student performance using machine learning.",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)