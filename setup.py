from setuptools import setup, find_packages

setup(name = 'pyvoltic',
      url = 'https://github.com/leoloman/pyvoltic',
      author = 'Leo Loman',
      author_email = 'leo.loman@outlook.com',
      # packages = find_packages(where = 'pyvoltic'),
      packages = ['pyvoltic', 'pyvoltic.classes', 'pyvoltic.models','pyvoltic.probability_generating_functions',
      'pyvoltic.vizualisations','pyvoltic.results'],
      install_requires = ['numpy', 'networkx', 'matplotlib', 'scipy'],
      version='0.1',
      python_requires = '>=3.7',
      classifiers = ['Programming Langyage :: Python'],
      license='MIT',
      description='A framework for the Edge Based Compartmental Model (Volz Miller) equations',
      long_description=open('README.md').read()
)      