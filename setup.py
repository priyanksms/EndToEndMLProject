from setuptools import find_packages,setup
from typing import List

def get_requirements(filepath:str)-> List[str]:
      with open(filepath, 'r') as fileobj:
            requirements = fileobj.readlines()
      requirements = [requirement.strip('\n') for requirement in requirements]

      if('-e .' in requirements):
            requirements.remove('-e .')

      return requirements


setup(name='End To End Machine Learning Project',
      version='0.0.1',
      description='Python Distribution Utilities',
      author='Priyank Jain',
      author_email='priyank.jain@sms-group.com',
      url='https://www.python.org/sigs/distutils-sig/',
      packages = find_packages(),
      install_requires = get_requirements('requirements.txt')
     )

find_packages()