__version__ = '0.5.1'

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

setup(name='retools',
      version=__version__,
      description='Redis Tools',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        ],
      keywords='cache redis queue lock',
      author="Ben Bangert",
      author_email="ben@groovie.org",
      url="http://readthedocs.org/docs/retools/",
      license="MIT",
      packages=find_packages(),
      use_2to3=True,
      test_suite="retools.tests",
      include_package_data=True,
      zip_safe=False,
      tests_require = ['pkginfo', 'Mock>=0.8rc2', 'nose',
                       'simplejson'],
      install_requires=[
          "setproctitle>=1.1.2",
          "redis>=2.9.0",
      ],
      entry_points="""
      [console_scripts]
      retools-worker = retools.queue:run_worker

      """
)
