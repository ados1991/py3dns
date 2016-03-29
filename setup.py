import sys,os

sys.path.insert(0,os.getcwd())

from distutils.core import setup

import DNS

setup(
        #-- Package description
        name = 'py3dns',
        license = 'Python License',
        version = DNS.__version__,
        description = 'Python 3 DNS library',
        long_description = """Python 3 DNS library:
""",
        author = 'Anthony Baxter and others', 
        author_email = 'py3dns-hackers@lists.launchpad.net ',
      maintainer="Scott Kitterman",
      maintainer_email="scott@kitterman.com",
      url = 'https://launchpad.net/py3dns',
      packages = ['DNS'], keywords = ['DNS'],
      classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python License (CNRI Python License)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: Name Service (DNS)',
        'Topic :: Software Development :: Libraries :: Python Modules'
      ]
)

