#!/usr/bin/python

from distutils.core import setup

setup(name='quarters',
      version='0.0.1',
      description='Arch Linux package build system',
      author='Thomas S Hatch',
      author_email='thatch45@gmail.com',
      url='https://github.com/thatch45/Quarters',
      packages=['quarters',
                'quarters/scm',
                'quarters/builder',
                'quarters/master'],
      scripts=['scripts/quartermaster',
               'scripts/quarterbuilder'],
      data_files=[('/etc/quarters',
                    ['conf/quarters.conf',
                     'conf/openssl.cnf',
                     ]),
                 ],
     )

