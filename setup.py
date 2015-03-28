#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Yuval tisf Nativ'
__license__ = 'GPLv3'
__copyright__ = '2015, Yuval tisf Nativ'

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if __name__ == '__main__':
    if os.path.exists('MANIFEST'):
        os.remove('MANIFEST')

    long_desc = open('README.md').read() + '\n\n' + open('LICENSE.md').read()

    setup(name='PyQuick3',
        maintainer=__author__,
        maintainer_email='yuval@morirt.com',
        description="""PyQuick3 is another implementation of the Quick3 sorting algorithm.""",
        license=__license__,
        url='https://www.github.com/ytisf/pyQuick3',
        version="0.0.2 Beta",
        download_url='https://www.github.com/ytisf/pyQuick3',
        long_description=long_desc,
        packages=['pyQuick3'],
        install_requires=required,
        platforms='any',
        classifiers=(
                'Development Status :: 2 - Pre-Alpha',
                'Intended Audience :: Developers',
                'Intended Audience :: Science/Research',
                'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                'Topic :: Software Development',
                'Topic :: Scientific/Engineering',
                'Environment :: Console',
                'Operating System :: Microsoft :: Windows',
                'Operating System :: POSIX',
                'Operating System :: Unix',
                'Operating System :: MacOS',
                'Programming Language :: Python',
                'Programming Language :: Python :: 2.7',)
        )