from setuptools import setup

VERSION = '0.1'

DESCRIPTION = "A Matplotlib normalize object that replicates DS9 image stretching"
NAME = "ds9norm"
AUTHOR = "Chris Beaumont"
AUTHOR_EMAIL = "cbeaumont@cfa.harvard.edu"
MAINTAINER = AUTHOR
MAINTAINER_EMAIL = AUTHOR_EMAIL
LICENSE = "MIT"
URL = "https://github.com/glue-viz/ds9norm"

try:
    import pypandoc
    LONG_DESCRIPTION = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    with open('README.md') as infile:
        LONG_DESCRIPTION=infile.read()

setup(name=NAME,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      version=VERSION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      url=URL,
      license=LICENSE,
      py_modules=['ds9norm'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Operating System :: OS Independent',
          'Topic :: Utilities'],
      )
