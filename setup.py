
from setuptools import setup, find_packages
from os import path
base_dir = path.abspath(path.dirname(__file__))
setup(
  name = 'Raxhub',        
  packages = ['Raxhub'],
  include_package_data=True,
  version = '1.2',    
  license='MIT',     
  description = 'Raxhub Logo Generator', 
  author = 'Mr Rax',                  
  author_email = 'freefire.akshaygangwar@gmail.com',     
  url = 'https://github.com/akshayxt/Raxhub',   
  download_url = 'https://github.com/akshayxt/Raxhub/archive/1.2.tar.gz',    
  keywords = ['Raxhub', 'logo', 'generator'], 
  install_requires=[           
          'pillow',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
