from setuptools import setup, find_packages

setup(name='musicgame',
      version='1.0',
      description='play line music',
      author='Fijon',
      author_email="huiqiangxu@msn.cn",
      packages=find_packages(),
      include_package_data=True,
      platforms="any",
      install_requires=[],

      scripts=[],
      entry_points={
          'console_scripts': [
              'test = test.help:main'
          ]
      })
