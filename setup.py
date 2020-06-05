import setuptools

setuptools.setup(name='optimal-foraging',
      version='0.1dev',
      description='Genetic algorithm to determine evolutionary competitiveness of gregarization in locusts',
      author='Yoni Maltsman',
      author_email='jmaltsman@hmc.edu',
      url='https://github.com/ymaltsman/optimal-foraging',
      long_description=open('README.md').read(), 
      packages=setuptools.find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3",
        ],
      python_requires=">=3.6"
     )
