#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
from setuptools.command.install import install as _install

import pylsa

class install(_install):
    def run(self):
        try:
            import cmmnbuild_dep_manager
            mgr = cmmnbuild_dep_manager.Manager()
            mgr.install('pylsa')
            print('registered pylsa with cmmnbuild_dep_manager')
        except ImportError:
            pass
        _install.run(self)

setuptools.setup(
    name='pylsa',
    version=pylsa.__version__,
    description='A Python wrapping of LSA API',
    author='Riccardo De Maria',
    author_email='riccardo.de.maria@cern.ch',
    url='https://github.com/rdemaria/pylsa',
    packages=['pylsa'],
    package_dir={'pylsa': 'pylsa'},
    install_requires=['JPype1>=0.6.1',
                      'cmmnbuild-dep-manager>=2.1.0' ],
    cmdclass={ 'install': install },
)

