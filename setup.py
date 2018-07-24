from setuptools import setup

setup(name='bigtiffp',
      version='0.1',
      description='Find out if a .tiff file has bigtiff enabled',
      url='http://github.com/pablo-munoz/bigtiffp',
      author='Pablo Munoz',
      author_email='pabloharomunoz@gmail.com',
      license='MIT',
      packages=['bigtiffp'],
      scripts=['bin/bigtiffp'],
      zip_safe=False)
      
