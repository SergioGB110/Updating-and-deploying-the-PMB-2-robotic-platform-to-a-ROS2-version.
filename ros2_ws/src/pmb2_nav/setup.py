from setuptools import setup
import os
from glob import glob

package_name = 'pmb2_nav'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],

    data_files=[
        # registro del paquete
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),

        ('share/' + package_name, ['package.xml']),

        # Cambiado
        #----------------------------------------------------------
        (os.path.join('share', package_name, 'launch'),
            glob('pmb2_nav/launch/*')),

        (os.path.join('share', package_name, 'config'),
            glob('pmb2_nav/config/*')),

        (os.path.join('share', package_name, 'maps'),
            glob('pmb2_nav/maps/*')),
       #----------------------------------------------------------
    ],

    install_requires=['setuptools'],
    zip_safe=True,

    maintainer='sergio',
    maintainer_email='sergio@todo.todo',
    description='PMB2 Nav2 package',
    license='TODO',

    tests_require=['pytest'],

    entry_points={
        'console_scripts': [],
    },
)