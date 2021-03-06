from setuptools import setup

setup(name='simplebank',
      version='0.0.1',
      description='An API for Simple Bank',
      long_description='View balances, create and manage goals, and manage transactions.',
      url='https://github.com/nicolewhite/simplebank',
      author='Nicole White',
      author_email='nmwhite0131@gmail.com',
      license='MIT',
      packages=['simplebank'],
      install_requires=[
        'python-dateutil==2.6.0',
        'requests==2.12.1',
      ],
      zip_safe=False)
