#!/usr/bin/env python
#
# Setup prog for PACKAGE 
#
#

import commands
import os
import re
import sys

from PACKAGE import infoservice
release_version=infoservice.__version__

from distutils.core import setup
from distutils.command.install import install as install_org
from distutils.command.install_data import install_data as install_data_org

# Python version check. 
major, minor, release, st, num = sys.version_info
if major == 2:
    if not minor >= 4:
        print("Autopyfactory requires Python >= 2.4. Exitting.")
        sys.exit(0)

# ===========================================================
#                D A T A     F I L E S 
# ===========================================================

libexec_files = ['libexec/%s' %file for file in os.listdir('libexec') if os.path.isfile('libexec/%s' %file)]

systemd_files = [ 'etc/PACKAGE'
                 ]

etc_files = ['etc/PACKAGE.conf',
             ]

sysconfig_files = [
             'etc/sysconfig/PACKAGE',

]

logrotate_files = ['etc/logrotate/PACKAGE',]

#initd_files = ['/PACKAGE.init',
#               ]



# -----------------------------------------------------------

rpm_data_files=[('/usr/libexec', libexec_files),
                ('/etc/PACKAGE', etc_files),
                ('/etc/sysconfig', sysconfig_files),
                ('/etc/logrotate.d', logrotate_files),                                        
#                ('/etc/init.d', initd_files),
                ('/usr/lib/systemd/system', systemd_files),
                #('/usr/share/doc/PACKAGE', docs_files),                                        
               ]


home_data_files=[('etc', libexec_files),
                 ('etc', etc_files),
#                 ('etc', initd_files),
                 ('etc', sysconfig_files),
                ]

# -----------------------------------------------------------

def choose_data_files():
    rpminstall = True
    userinstall = False
     
    if 'bdist_rpm' in sys.argv:
        rpminstall = True

    elif 'install' in sys.argv:
        for a in sys.argv:
            if a.lower().startswith('--home'):
                rpminstall = False
                userinstall = True
                
    if rpminstall:
        return rpm_data_files
    elif userinstall:
        return home_data_files
    else:
        # Something probably went wrong, so punt
        return rpm_data_files
       
# ===========================================================

# setup for distutils
setup(
    name="PACKAGE",
    version=release_version,
    description='PACKAGE package',
    long_description='''This package contains the PACKAGE''',
    license='GPL',
    author='AUTHOR',
    author_email='EMAIL',
    maintainer='MAINTAINER',
    maintainer_email='MEMAIL',
    url='https://github.com/PACKAGE',
    packages=['service,
              ],
    scripts = [ # Utilities and main script
               'scripts/PACKAGE',
              ],
    
    data_files = choose_data_files()
)
