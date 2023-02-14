from setuptools import setup

setup(name = 'pyvoltic',
      url = 'https://github.com/leoloman/pyvoltic'.
      author = 'Leo Loman',
      author_email = 'leo.loman@outlook.com',
      packages = ['pyvoltic'],
      install_requires = ['numpy', 'math', 'networkx', 'matplotlib', 'scipy'],
      version='0.1',
      license='MIT',
      description='A framework for the Volz Miller equations',
      long_description=open('README.txt').read()
     )
      