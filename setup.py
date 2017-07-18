#! /usr/bin/python
# $Id: setup.py,v 1.3 2012/03/05 04:54:01 nanard Exp $
#
# python script to build the libnatpmp module under unix

from setuptools import setup, Extension
from setuptools.command import build_ext
import subprocess

EXT = ['libnatpmp.a']

class make_then_build_ext(build_ext.build_ext):
      def run(self):
            subprocess.check_call(['make'] + EXT)
            build_ext.build_ext.run(self)

setup(name="libnatpmp", version="1.0",
      cmdclass={'build_ext': make_then_build_ext},
      ext_modules=[
        Extension(name="libnatpmp", sources=["libnatpmpmodule.c"],
                  extra_objects=EXT,
                  define_macros=[('ENABLE_STRNATPMPERR', None)]
        )]
     )

