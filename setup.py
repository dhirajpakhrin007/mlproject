#library for making a project as a package
from setuptools import find_packages, setup
from typing import List

ignore_require = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    function returns the list of requirements
    '''
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
    
        if ignore_require in requirements:
            requirements.remove(ignore_require)
    
    return requirements 
        

        
    
    

setup(
    name='mlproject',
    version='0.0.1',
    author='Dhiraj',
    author_email='dhirajpakhrin95@gmail.com',
    packages=find_packages(),
    requires=get_requirements('requirements.txt')
)